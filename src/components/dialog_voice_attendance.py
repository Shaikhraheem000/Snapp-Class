from datetime import datetime

import pandas as pd
import streamlit as st

from src.components.dialog_attendance_results import show_attendance_results
from src.database.config import supabase
from src.pipelines.voice_pipeline import process_bulk_audio


@st.dialog("Voice Attendance Report")
def voice_attendance_dialog(selected_subject_id):
    st.write("Record students speaking for attendance. The system will match voices against enrolled students.")
    audio_data = st.audio_input("Record attendance audio")

    if st.button("Analyze Audio", width='stretch', type='primary', icon=':material/analytics:'):
        if not audio_data:
            st.warning("Please record audio before analyzing.")
            return

        with st.spinner("Processing audio for attendance..."):
            enrolled_res = (
                supabase.table('subject_students')
                .select('*,students(*)')
                .eq('subject_id', selected_subject_id)
                .execute()
            )
            enrolled_students = enrolled_res.data

            if not enrolled_students:
                st.warning('No student enrolled in this course')
                return

            candidates_dict = {
                int(node['students']['student_id']): node['students']['voice_embedding']
                for node in enrolled_students
                if node.get('students') and node['students'].get('voice_embedding')
            }

            if not candidates_dict:
                st.warning('No voice data available for enrolled students')
                return

            detected_scores = process_bulk_audio(audio_data.read(), candidates_dict)
            results, attendance_to_log = [], []
            current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

            for node in enrolled_students:
                student = node['students']
                student_id = int(student['student_id'])
                score = detected_scores.get(student_id)
                is_present = score is not None

                results.append({
                    'Name': student['name'],
                    "Id": student_id,
                    "Source": f"Voice match ({score:.2f})" if is_present else "-",
                    "Status": "✅Present" if is_present else "❌Absent",
                })

                attendance_to_log.append({
                    "student_id": student_id,
                    "subject_id": selected_subject_id,
                    "timestamp": current_timestamp,
                    "is_present": is_present,
                })

            st.session_state.voice_attendance_results = (
                pd.DataFrame(results),
                attendance_to_log,
            )

    if st.session_state.get('voice_attendance_results'):
        st.divider()
        df_results, logs = st.session_state.voice_attendance_results
        show_attendance_results(df_results, logs)

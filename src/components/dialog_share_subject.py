import streamlit as st
import segno
import io

@st.dialog('Share "Subject Enrollment" Link')
def share_subject_dialog(subject_name, subject_code):
    app_domain = "snapclass.streamlit.app"
    enroll_link = f"{app_domain}?join-code={subject_code}"

    st.header("Scan to Join")
    Qr =segno.make(enroll_link)
    out = io.BytesIO()
    Qr.save(out,kind='png',scale=10,border=1)
    col1,col2 =st.columns(2)
    with col1:
        st.markdown("### Copy Link")
        st.code(enroll_link,language='text')
        st.code(subject_code,language='text')
        st.info("Copy this link to share on WhatsApp or Email")

    with col2:
        st.markdown("### Scan to Join ")
        st.image(out.getvalue(),caption='QR CODE for class joining')
  

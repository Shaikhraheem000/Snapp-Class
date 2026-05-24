# SnapClass

AI-Powered Smart Attendance Management System for Classrooms

SnapClass is a full-stack AI-based attendance management platform that allows teachers to create courses, enroll students, and automatically mark attendance using facial recognition and optional voice recognition.

The platform is designed to simplify classroom attendance workflows through biometric verification, QR-based enrollment, and intelligent attendance tracking.

---

# Live Demo

## Main Application
https://snappclass.streamlit.app/

## Landing Page
https://snap-class-landing-page-zeta.vercel.app/

## Landing Page Repository
https://github.com/Shaikhraheem000/SnapClass-LandingPage

---

# Features

## Teacher Features

- Teacher registration and login
- Create and manage subjects/courses
- Generate course enrollment links
- Generate QR codes for student enrollment
- View attendance records
- Confirm attendance before saving

## Student Features

- Student registration with Face ID
- Optional voice enrollment
- Join courses using:
  - Subject code
  - Shareable link
  - QR code
- View enrolled subjects
- Track attendance statistics

## AI Attendance Features

- Face recognition-based attendance
- Voice recognition-based attendance
- Classroom image upload support
- Attendance validation before submission
- Biometric attendance workflow

---

# Tech Stack

## Frontend
- Streamlit

## Backend & Database
- Supabase
- PostgreSQL

## AI / Machine Learning
- Dlib
- face_recognition_models
- scikit-learn
- Librosa
- Resemblyzer

## Data Processing
- Pandas
- NumPy

## Language
- Python

---

# Project Architecture

```text
User Interface (Streamlit)
        ↓
AI Recognition Pipelines
(Face + Voice Processing)
        ↓
Supabase Database
(PostgreSQL)
        ↓
Attendance Management System
```

---

# Project Structure

```text
Snapp-Class/
│
├── app.py
├── requirements.txt
│
├── src/
│   ├── components/
│   ├── database/
│   ├── pipelines/
│   ├── screens/
│   └── ui/
│
└── .streamlit/
    └── secrets.toml
```

---

# Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/Shaikhraheem000/Snapp-Class.git
cd Snapp-Class
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a file:

```text
.streamlit/secrets.toml
```

Add:

```toml
SUPABASE_URL = "your_supabase_project_url"
SUPABASE_KEY = "your_supabase_anon_key"
APP_URL = "https://snappclass.streamlit.app"
```

---

## 5. Run the Application

```bash
streamlit run app.py
```

---

# Database Tables

The application uses the following Supabase tables:

- `teachers`
- `students`
- `subjects`
- `subject_students`
- `attendance_logs`

Ensure proper Row Level Security (RLS) policies are configured for:

- SELECT
- INSERT
- UPDATE
- DELETE

---

# Attendance Workflow

## Face Recognition Attendance

1. Teacher uploads classroom image
2. System extracts facial embeddings
3. Faces are matched with registered students
4. Attendance candidates are generated
5. Teacher confirms attendance
6. Records are saved to database

---

## Voice Recognition Attendance

1. Student voice embeddings are stored during enrollment
2. Uploaded audio is processed
3. Voice embeddings are compared
4. Matching students are identified
5. Attendance is recorded after validation

---

# Deployment

The project is deployed using:

- Streamlit Community Cloud
- Vercel

## Deployment Checklist

- Push project to GitHub
- Add secrets in Streamlit Cloud
- Set `app.py` as main file
- Configure Supabase credentials
- Verify QR/share links use deployed app URL

---

# Security & Privacy Notes

This project is developed for educational and learning purposes.

Biometric systems require additional production-grade security measures such as:

- Encrypted biometric storage
- Strong authentication systems
- Secure API handling
- Privacy compliance
- Anti-spoofing protection
- Secure access policies

For production deployment, additional security hardening is strongly recommended.

---

# Future Improvements

- Real-time webcam attendance
- Anti-spoofing detection
- Attendance analytics dashboard
- PDF/Excel export support
- Mobile responsiveness improvements
- Multi-classroom support
- FastAPI backend migration
- Improved authentication system

---

# Author

## Shaikh Raheem

GitHub:
https://github.com/Shaikhraheem000

---

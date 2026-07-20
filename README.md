# 🛡️ SecurePass — Passwordless Biometric Authentication

## 📌 Project Overview

**SecurePass** is a Passwordless Biometric Authentication System developed as a **Final Year B.Tech Computer Science & Engineering project**.

The system provides an alternative to traditional password-based authentication by enabling users to register and authenticate using **facial recognition** and **voice-based biometric verification**.

SecurePass also includes an **Admin Dashboard** for user management, authentication history, and report generation, providing a complete biometric authentication and monitoring solution.

---

## 🎯 Project Objectives

- 🔐 Reduce dependency on traditional password-based authentication
- 😀 Enable facial biometric registration and authentication
- 🎤 Implement voice-based biometric registration and authentication
- 👥 Provide centralized user management through an Admin Dashboard
- 📜 Maintain authentication and login history
- 📊 Generate reports for administrative analysis
- 💾 Manage application data using SQLite

---

## ✨ Key Features

### 😀 Face Authentication

- Face Registration
- Face Login
- Face Detection and Recognition
- Biometric-based user verification

### 🎤 Voice Authentication

- Voice Registration
- Voice Login
- Voice feature processing
- Voice-based identity verification

### 📊 Admin Dashboard

- View registered users
- Manage user information
- Monitor authentication activity
- View login history

### 📄 Report Generation

- Generate PDF reports
- Generate Excel reports
- Export application and user-related information

### 🔒 Authentication System

- Passwordless authentication workflow
- Multi-biometric authentication support
- Authentication history tracking
- User registration and management

---

## 🛠️ Technologies Used

### 🌐 Frontend

- HTML5
- CSS3
- JavaScript

### ⚙️ Backend

- Python
- Flask
- Flask-CORS

### 🗄️ Database

- SQLite

### 🤖 Computer Vision & Face Processing

- OpenCV
- Face Recognition
- Dlib

### 🎙️ Voice Processing

- Librosa
- SoundDevice
- NumPy
- SciPy

### 📊 Data & Report Generation

- Pandas
- ReportLab
- OpenPyXL

---

## 📂 Project Structure

```text
Passwordless-Biometric-Auth/
│
├── admin/          # Admin dashboard components
├── database/       # Database-related files
├── face/           # Face authentication modules
├── face_data/      # Registered face data
├── frontend/       # Frontend application files
├── recordings/     # Voice recordings
├── reports/        # Generated reports
├── voice/          # Voice authentication modules
│
├── app.py          # Flask application entry point
├── config.py       # Application configuration
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/lavanya-0005/Passwordless-Biometric-Auth.git
```

### 2. Navigate to the Project Directory

```bash
cd Passwordless-Biometric-Auth
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Flask Backend

```bash
python app.py
```

### 5. Launch the Frontend

Open the frontend `index.html` file using **Live Server** or another local web server.

---

## 🔄 System Workflow

```text
User Registration
       ↓
Choose Biometric Method
       ↓
Face / Voice Registration
       ↓
Biometric Data Processing
       ↓
User Authentication
       ↓
Identity Verification
       ↓
Authentication Result
       ↓
Login History & Admin Monitoring
```

---

## 💡 Skills Demonstrated

- Python Application Development
- Flask Backend Development
- REST API Integration
- Biometric Authentication Concepts
- Computer Vision
- Face Recognition
- Voice Processing
- Database Management
- Frontend Development
- Report Generation
- Full-Stack Application Development

---

## 🔗 Project Link

💻 **[View Source Code](https://github.com/lavanya-0005/Passwordless-Biometric-Auth)**

---

## 🔐 Security & Privacy

Biometric authentication systems handle sensitive user data. This project is intended primarily for **academic and educational purposes**.

For production deployment, additional security measures should be implemented, including:

- Encryption of stored biometric data
- Secure communication using HTTPS
- Strong access controls
- Secure API authentication
- Biometric template protection
- Privacy and data-retention policies

---

## 🔮 Future Enhancements

- 🔑 Add WebAuthn and Passkey support
- 📱 Improve mobile responsiveness
- ☁️ Add secure cloud deployment
- 🔒 Implement encrypted biometric storage
- 📧 Add authentication notifications
- 📊 Enhance the Admin Dashboard with analytics
- 🛡️ Add additional security and anti-spoofing mechanisms

---

## 👩‍💻 Author

### Lavanya Balaga

**B.Tech — Computer Science & Engineering**

💼 **LinkedIn:** [Lavanya Balaga](https://www.linkedin.com/in/lavanya-balaga-807ab2320)

📧 **Email:** [balagalavanya21@gmail.com](mailto:balagalavanya21@gmail.com)

---

<p align="center">
  🔐 Building Secure and Intelligent Authentication Systems
</p>

<p align="center">
  ⭐ If you find this project interesting, consider giving the repository a star!
</p>

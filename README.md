# Passwordless Biometric Authentication System 🔐

## Description
The Passwordless Biometric Authentication System is a secure authentication application that replaces traditional password-based login systems with biometric verification.  
Instead of using passwords, users are authenticated using biometric data such as face recognition or voice recognition, improving security and user convenience.

This system helps reduce common security risks such as phishing attacks, password theft, and brute-force attacks.

---

## Objectives
- Remove dependency on traditional passwords
- Enhance system security using biometric authentication
- Improve user experience with faster login
- Prevent unauthorized access

---

## Features
- Passwordless user authentication
- Biometric-based user registration and login
- Secure and efficient authentication process
- Reduced risk of password-related attacks
- User-friendly interface

---

## Technologies Used
- **Programming Language:** Python  
- **Framework:** Flask  
- **Libraries:** OpenCV, NumPy, Machine Learning libraries  
- **Frontend:** HTML, CSS  
- **Version Control:** Git, GitHub  

---

## Project Structure

Passwordless-Biometric-Auth/

│

├── app.py

├── frontend

  └── index.html / script.js 

├── voice

│ └── __pychace__ / voice_login.py / voice_register.py

└── README.md


---

# 📘 1. Problem Statement

Traditional authentication systems rely heavily on passwords, which are difficult to remember and easy to compromise. Users often reuse passwords across multiple platforms, making systems vulnerable to phishing, brute-force attacks, and credential theft. This project addresses these issues by implementing a passwordless biometric authentication mechanism that ensures higher security and better user experience.


---

# 💡 2. Proposed Solution

The proposed system replaces passwords with biometric authentication. During registration, a user’s biometric data is captured and securely stored. During login, the system verifies the live biometric input against stored data to authenticate the user. This approach improves security, reduces human error, and eliminates password management issues.


---

# 🧠 3. System Architecture

- **1.The system consists of the following components:**

- **2.User Interface for registration and login**

- **3.Biometric data capture module**

- **4.Feature extraction and preprocessing module**

- **5.Authentication and verification module**

- **6.Database for storing biometric templates**


---
# 🔄 4. Workflow

- **1. User registers using biometric data**

- **2.Biometric features are extracted and stored securely**

- **3.User attempts to log in**

- **4.Live biometric data is captured**

- **5.System compares live data with stored data**

- **6.Access is granted or denied based on verification result**


---

# 📌 5. Conclusion

The Passwordless Biometric Authentication System provides a secure and efficient alternative to traditional password-based authentication systems. By leveraging biometric verification, the system improves security, enhances user experience, and reduces the risks associated with password management.

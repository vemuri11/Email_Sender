# 📧 Email Sender Using Python

A simple Python project to send emails via **SMTP** (Simple Mail Transfer Protocol).  
You can send **single emails** or **bulk emails** directly from the command line.

---

## 🚀 Features
- Send **single email** to one recipient
- Send **bulk emails** to multiple recipients at once
- Command-line input for subject, body, and recipients
- Lightweight and easy-to-use

---

## 🛠️ Requirements
- Python 3.x
- `smtplib` (comes pre-installed with Python)


## ⚡ Usage

### 1.Run the program:
- python main.py

### 2.Enter the details:
- Subject
- Body
- Choose 1 (Single email) or 2 (Bulk email)
- Provide recipient(s)

## 📂 Project Structure
### email_sender/
- │── main.py              # Main driver program
- │── singleEmailSend.py   # Handles single email sending
- │── bulkEmailSend.py     # Handles bulk email sending

### 🎯 Example Output
smtplib is available!
Enter subject: Successfully smtp created and email sent.
Enter body: Email sent
Select your operation:
1. Single email sender
2. Bulk email sender
Enter emails separated by comma: test1@gmail.com, test2@gmail.com
Successfully email sent!

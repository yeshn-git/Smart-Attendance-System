# 📸 Smart Attendance System using Face Recognition

A real-time automated attendance system built with Python and Computer Vision. This application uses the camera to recognize registered faces, marks their attendance in a MySQL database, and prevents duplicate entries for the day. It also includes an export feature to generate daily attendance reports in Excel/CSV format.

## 🚀 Features
* **Real-Time Face Recognition:** Identifies students instantly using the `face_recognition` library.
* **Duplicate Prevention:** Intelligent logic ensures a student is only marked present once per day.
* **Database Integration:** Stores student details and attendance logs securely in MySQL.
* **Excel Export:** Generates downloadable `.csv` reports for administrators.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Computer Vision:** OpenCV, dlib, Face Recognition
* **Database:** MySQL 8.0
* **Data Handling:** Pandas

## 📂 Project Structure
* `add_student.py` → Script to register a new student and capture their face.
* `train_faces.py` → Encodes the saved images into mathematical data for the AI.
* `main.py` → The core application that runs the camera and marks attendance.
* `generate_report.py` → Exports the database logs to a CSV file.
* `mark_attendance.py` → Helper logic for database interactions.

## ⚙️ Setup & Installation

### 1. Prerequisites
* Python 3.x
* MySQL Server & Workbench
* CMake (Required for compiling dlib)
* Visual Studio Build Tools (C++ Desktop Development)

### 2. Install Python Libraries
```bash
pip install cmake
pip install dlib
pip install face-recognition opencv-python mysql-connector-python pandas
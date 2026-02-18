# 📸 Smart Attendance System (Enterprise Edition)

A full-stack Biometric Attendance System built with **Python**, **OpenCV**, and **MySQL**.
It features a **Modern GUI Dashboard**, **Multi-Subject Support**, and **Automated Excel Reporting**.

## 🚀 Features
* **Real-time Face Recognition:** Uses HOG + Linear SVM for 99% accuracy.
* **Live Attendance Logging:** Prevents duplicate entries using logic gates.
* **Database Integration:** Stores records in MySQL with Subject/Session tracking.
* **Admin Dashboard:** Dark-mode GUI built with Tkinter.
* **Excel Export:** Generates formatted daily reports filtered by subject.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Computer Vision:** OpenCV, face_recognition, dlib
* **GUI:** Tkinter (Custom Styled)
* **Database:** MySQL Connector
* **Data Processing:** Pandas, OpenPyXL

## ⚙️ Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/yeshn-git/Smart-Attendance-System.git](https://github.com/yeshn-git/Smart-Attendance-System.git)
    cd Smart-Attendance-System
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup Database (MySQL)**
    Open MySQL Workbench and run:
    ```sql
    CREATE DATABASE attendance_system;
    USE attendance_system;

    CREATE TABLE students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        roll_number VARCHAR(20) UNIQUE,
        face_encoding BLOB
    );

    CREATE TABLE attendance_logs (
        log_id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT,
        check_in_time DATETIME,
        status VARCHAR(20),
        subject VARCHAR(50),
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    );
    ```

## 🖥️ How to Run

1.  **Start the Dashboard**
    ```bash
    python app.py
    ```
2.  **Select a Subject** (e.g., "CS_DataStructures") from the dropdown.
3.  Click **[ START ATTENDANCE ]** to launch the camera.
4.  Press **'q'** to close the camera.
5.  Click **[ EXPORT EXCEL REPORT ]** to get the daily log.

## 📂 Project Structure
* `app.py` - The Main GUI Dashboard.
* `main.py` - The Core Face Recognition Logic.
* `generate_report.py` - The Excel Export Engine.
* `add_student.py` - Utility to register new faces.
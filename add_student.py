import cv2
import mysql.connector
import os

# --- CONFIGURATION ---
DB_PASSWORD = "YOUR_DB_PASSWORD"  
SAVE_FOLDER = "student_images"

# Ensure the folder exists
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

def add_student():
    # 1. Get Student Details
    print("--- REGISTER NEW STUDENT ---")
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number (e.g., CSE-002): ")

    # 2. Open Camera
    cap = cv2.VideoCapture(0)
    print("Position your face in the frame. Press 's' to SAVE and quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Camera not working")
            break
        
        # Show video
        cv2.imshow("Register Student - Press 's' to Capture", frame)

        
        if cv2.waitKey(1) & 0xFF == ord('s'):
            # Generate a unique filename
            img_name = f"{roll_no}.jpg"
            full_path = os.path.join(SAVE_FOLDER, img_name)
            
            # Save the image locally
            cv2.imwrite(full_path, frame)
            print(f"✅ Image saved at: {full_path}")
            
            # Save to Database
            save_to_db(name, roll_no)
            break
    
    cap.release()
    cv2.destroyAllWindows()

def save_to_db(name, roll_no):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR_DB_PASSWORD",
            database="attendance_system"
        )
        cursor = conn.cursor()
        
        # SQL Query to insert data
        sql = "INSERT INTO students (name, roll_number) VALUES (%s, %s)"
        val = (name, roll_no)
        
        cursor.execute(sql, val)
        conn.commit() # saves changes
        
        print(f"✅ Student {name} registered in Database successfully!")
        
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"❌ Database Error: {err}")

if __name__ == "__main__":
    add_student()
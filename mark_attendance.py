import mysql.connector
from datetime import datetime

# --- CONFIG ---
DB_PASSWORD = "YOUR_DB_PASSWORD"  

def mark_present(roll_no):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=DB_PASSWORD,
            database="attendance_system"
        )
        cursor = conn.cursor()

        # 1. Finds the Student ID from the Roll Number
        cursor.execute("SELECT student_id, name FROM students WHERE roll_number = %s", (roll_no,))
        student = cursor.fetchone()

        if not student:
            print(f"❌ Error: No student found with Roll No {roll_no}")
            return

        student_id = student[0]
        student_name = student[1]

        # 2. Checks if already marked present TODAY
        # We check for any record where student_id matches AND date is today
        query = """
            SELECT * FROM attendance_logs 
            WHERE student_id = %s AND DATE(check_in_time) = CURDATE()
        """
        cursor.execute(query, (student_id,))
        existing_log = cursor.fetchone()

        if existing_log:
            #print(f"⚠️ {student_name} is ALREADY marked present today.")
            pass
        else:
            # 3. Insert the log
            insert_query = "INSERT INTO attendance_logs (student_id, status) VALUES (%s, 'Present')"
            cursor.execute(insert_query, (student_id,))
            conn.commit()
            
            # Get current time for display
            now = datetime.now().strftime("%H:%M:%S")
            print(f"✅ Success: {student_name} marked PRESENT at {now}")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"❌ Database Error: {err}")

# --- TEST AREA ---
if __name__ == "__main__":
    test_roll = input("Enter Roll No to mark present (e.g., CSE-101): ")
    mark_present(test_roll)
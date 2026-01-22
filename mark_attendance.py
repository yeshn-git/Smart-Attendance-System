import mysql.connector
from datetime import datetime

# --- CONFIG ---
DB_PASSWORD = "YOUR_DB_PASSWORD"  # <--- Make sure this is correct

def mark_present(name, subject): # <--- Added 'subject' parameter
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=DB_PASSWORD,
            database="attendance_system"
        )
        cursor = conn.cursor()

        # 1. Find the Student ID
        # We search by roll_number because your files are named 'CSE-101.jpg'
        cursor.execute("SELECT student_id, roll_number FROM students WHERE roll_number = %s", (name,))
        student = cursor.fetchone()

        if student:
            student_id = student[0]
            roll_number = student[1]

            # 2. CHECK DUPLICATE (Updated Logic)
            # We now check if they are present for THIS SPECIFIC SUBJECT on this day.
            check_query = """
                SELECT * FROM attendance_logs 
                WHERE student_id = %s AND DATE(check_in_time) = %s AND subject = %s
            """
            cursor.execute(check_query, (student_id, current_date, subject))
            existing_log = cursor.fetchone()

            if existing_log:
                pass # Already marked for this subject
            else:
                # 3. INSERT LOG (With Subject)
                insert_query = """
                    INSERT INTO attendance_logs (student_id, check_in_time, status, subject) 
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insert_query, (student_id, now, 'Present', subject))
                conn.commit()
                print(f"✅ {name} marked PRESENT for {subject} at {current_time}")

        else:
            print(f"❌ Error: Student '{name}' not found in database.")

    except mysql.connector.Error as err:
        print(f"❌ Database Error: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()
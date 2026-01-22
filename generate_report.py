import mysql.connector
import pandas as pd
from datetime import datetime

# --- CONFIG ---
DB_PASSWORD = "YOUR_DB_PASSWORD"

def export_attendance():
    try:
        # 1. Connect to Database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=DB_PASSWORD,
            database="attendance_system"
        )
        
        # 2. SQL Query to join Students + Logs
        # We want Name (from Students table) and Time (from Logs table)
        query = """
            SELECT 
                students.name, 
                students.roll_number, 
                attendance_logs.check_in_time, 
                attendance_logs.status
            FROM attendance_logs
            INNER JOIN students ON attendance_logs.student_id = students.student_id
        """
        
        # 3. Read into Pandas (The Data Science Library)
        df = pd.read_sql(query, conn)
        
        if df.empty:
            print("⚠️ No attendance records found to export.")
        else:
            # 4. Save to Excel/CSV
            filename = f"Attendance_Report_{datetime.now().strftime('%Y-%m-%d')}.csv"
            df.to_csv(filename, index=False)
            print("------------------------------------------------")
            print(f"✅ Report generated successfully: {filename}")
            print("------------------------------------------------")
            print(df) 

        conn.close()

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")

if __name__ == "__main__":
    export_attendance()
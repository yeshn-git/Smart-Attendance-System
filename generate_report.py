import mysql.connector
import pandas as pd
from datetime import datetime
import warnings

# --- 1. SILENCE THE WARNINGS ---
# This tells Python: "I know I'm not using SQLAlchemy, stop complaining."
warnings.filterwarnings('ignore')

# --- CONFIG ---
DB_PASSWORD = "1Y2E3S4H" 

def export_attendance(subject_filter="All"):
    conn = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password= "1Y2E3S4H",
            database="attendance_system"
        )
        
        # 2. Base Query
        query = """
        SELECT 
            s.name, 
            s.roll_number, 
            a.subject, 
            DATE_FORMAT(a.check_in_time, '%Y-%m-%d %H:%i:%s') as time, 
            a.status
        FROM attendance_logs a
        JOIN students s ON a.student_id = s.student_id
        """
        
        # 3. Apply Filter (Using Direct String Injection)
        # We manually put the subject into the string to avoid the parameter error
        if subject_filter != "Select Subject" and subject_filter != "All":
            query += f" WHERE a.subject = '{subject_filter}'"
            
        query += " ORDER BY a.check_in_time DESC"
        
        # 4. Create DataFrame (Note: No 'params=' argument here!)
        df = pd.read_sql(query, conn)
        
        if df.empty:
            return "No records found for this subject."

        # 5. Generate Filename
        current_date = datetime.now().strftime("%Y-%m-%d")
        clean_subject = subject_filter.replace(" ", "_") if subject_filter != "Select Subject" else "Full_Report"
        filename = f"{clean_subject}_{current_date}.xlsx"
        
        # 6. Export with Formatting
        with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
            workbook = writer.book
            worksheet = writer.sheets['Sheet1']
            
            header_format = workbook.add_format({
                'bold': True, 'text_wrap': True,
                'fg_color': '#2c3e50', 'font_color': 'white', 'border': 1
            })
            
            for col_num, value in enumerate(df.columns.values):
                worksheet.write(0, col_num, value, header_format)
                worksheet.set_column(col_num, col_num, 25)
        
        return f"✅ Report saved: {filename}"

    except Exception as e:
        return f"❌ Error: {e}"
    finally:
        if conn and conn.is_connected():
            conn.close()

# Test block
if __name__ == "__main__":
    print(export_attendance("All"))
import mysql.connector

def test_connection():
    print("Attempting to connect to the database...")
    
    try:
        # Establish the connection
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR_DB_PASSWORD",  # <--- CHANGE THIS!
            database="attendance_system"
        )

        if conn.is_connected():
            print("------------------------------------------------")
            print("✅ SUCCESS: Python is connected to MySQL!")
            print("------------------------------------------------")
            
            # tries to fetch the dummy student we added
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            records = cursor.fetchall()
            
            print(f"Found {len(records)} student(s) in the database:")
            for row in records:
                print(row)
                
            cursor.close()
            conn.close()
            
    except mysql.connector.Error as err:
        print(f"❌ ERROR: {err}")

if __name__ == "__main__":
    test_connection()
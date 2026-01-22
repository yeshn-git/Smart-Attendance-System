import tkinter as tk
from tkinter import ttk, messagebox
import main
import generate_report  

def start_attendance():
    selected_subject = subject_combobox.get()
    if selected_subject == "Select Subject":
        messagebox.showwarning("Warning", "Please select a subject first!")
        return
    
    try:
        # Start the camera with the selected subject
        main.start_recognition(selected_subject)
    except Exception as e:
        messagebox.showerror("Error", f"Camera crashed: {e}")

def generate_excel():
    # 1. Get the subject currently showing in the dropdown
    current_subject = subject_combobox.get()
    
    # 2. Call the report function AND PASS THE SUBJECT
    result = generate_report.export_attendance(current_subject)
    
    # 3. Show the result
    if "Error" in result:
        messagebox.showerror("Report Error", result)
    else:
        messagebox.showinfo("Success", result)

# --- GUI SETUP ---
root = tk.Tk()
root.title("Smart Attendance System - Enterprise Edition")
root.geometry("500x400") # Made it slightly taller for the new button
root.configure(bg="#2c3e50")

# Header
tk.Label(root, text="📷 Smart Attendance Dashboard", 
         font=("Helvetica", 18, "bold"), bg="#2c3e50", fg="white").pack(pady=20)

# Dropdown Section
frame = tk.Frame(root, bg="#2c3e50")
frame.pack(pady=10)
tk.Label(frame, text="Current Session:", font=("Arial", 12), 
         bg="#2c3e50", fg="white").pack(side=tk.LEFT, padx=10)

subjects = ["Maths_101", "Physics_202", "CS_DataStructures", "CS_DBMS"]
subject_combobox = ttk.Combobox(frame, values=subjects, state="readonly", width=20)
subject_combobox.set("Select Subject")
subject_combobox.pack(side=tk.LEFT)

# Start Button (Green)
tk.Button(root, text="START ATTENDANCE", command=start_attendance,
          font=("Arial", 12, "bold"), bg="#27ae60", fg="white",
          width=25, height=2).pack(pady=20)

# Export Button (Orange) - THE NEW ADDITION
tk.Button(root, text="📄 EXPORT EXCEL REPORT", command=generate_excel,
          font=("Arial", 12, "bold"), bg="#e67e22", fg="white",
          width=25, height=2).pack(pady=5)

# Footer
tk.Label(root, text="System Ready", font=("Arial", 10), 
         bg="#2c3e50", fg="#bdc3c7").pack(side=tk.BOTTOM, pady=10)

root.mainloop()
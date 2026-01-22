import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
import os

# --- IMPORT YOUR FUNCTIONS ---
# This connects the buttons to your existing code
try:
    from add_student import add_student
    from train_faces import find_encodings
    from main import start_recognition
    from generate_report import export_attendance
except ImportError as e:
    print(f"❌ Error importing modules: {e}")
    print("Make sure all your .py files are in the same folder!")

# --- GUI LOGIC ---
def run_register():
    # We open the terminal for registration because it needs text input (Name/ID)
    os.system('start cmd /k "python add_student.py"') 

def run_train():
    try:
        find_encodings()
        messagebox.showinfo("Success", "✅ AI Training Complete!")
    except Exception as e:
        messagebox.showerror("Error", f"Training failed: {e}")

def run_attendance():
    try:
        start_recognition()
    except Exception as e:
        messagebox.showerror("Error", f"Camera failed: {e}")

def run_export():
    try:
        export_attendance()
        messagebox.showinfo("Success", "✅ Excel Report Generated!")
    except Exception as e:
        messagebox.showerror("Error", f"Export failed: {e}")

# --- SETUP WINDOW ---
root = tk.Tk()
root.title("Smart Attendance System")
root.geometry("400x500")
root.configure(bg="#f0f0f0")

# Custom Font
title_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
btn_font = tkfont.Font(family="Helvetica", size=12)

# Title
header = tk.Label(root, text="Smart Attendance\nDashboard", font=title_font, bg="#f0f0f0", fg="#333")
header.pack(pady=30)

# Buttons (Styled)
def create_btn(text, command, color):
    return tk.Button(root, text=text, command=command, font=btn_font, 
                     bg=color, fg="white", width=20, height=2, bd=0, cursor="hand2")

btn_register = create_btn("👤  Register New Student", run_register, "#3498db") # Blue
btn_register.pack(pady=10)

btn_train = create_btn("🧠  Train AI Model", run_train, "#9b59b6") # Purple
btn_train.pack(pady=10)

btn_start = create_btn("📷  Start Attendance", run_attendance, "#2ecc71") # Green
btn_start.pack(pady=10)

btn_export = create_btn("📊  Export Report", run_export, "#e67e22") # Orange
btn_export.pack(pady=10)

# Footer
footer = tk.Label(root, text="System Ready", font=("Arial", 10), bg="#f0f0f0", fg="#777")
footer.pack(side="bottom", pady=20)

# Start the App
root.mainloop()
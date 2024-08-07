import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser
import os

# Replace with the path to your batch file
disable_path = r'disable_cam.bat'
enable_path = r'enable_cam.bat'

# Replace with the correct password
password = "nothing"

# Create the main window and buttons
root = tk.Tk()
root.title("Cam Security For Systems")
root.geometry("600x500")
root.configure(bg='black')
button_frame = tk.Frame(root, bg="grey")
success_label = tk.Label(button_frame, text="", font=("Arial", 12, "bold"), bg="grey", fg="#ff0000")
success_label.pack(pady=10)
def project_info():
    filename = "Project Information.html"
    path = os.path.abspath(filename)
    url = "file://" + path
    webbrowser.open(url)

# Define the function to be executed when the first button is clicked
def button1_clicked():
    # Create a password prompt dialog box
    password_window = tk.Toplevel(root)
    password_window.title("Enter Password")
    password_window.geometry("300x200")
    password_label = tk.Label(password_window, text="Enter Password:")
    password_label.pack()
    password_entry = tk.Entry(password_window, show="*")
    password_entry.pack()
    def ok_button():
        if password_entry.get()==password:
            subprocess.run([disable_path], text=True)
            password_window.destroy()
            success_label.config(text="Camera Disabled Successfully")
        else:
            error_label.config(text="Incorrect password. Please try again.")
            password_entry.delete(0, tk.END)
    ok_button = tk.Button(password_window, text="OK", command=ok_button)
    ok_button.pack()
    error_label = tk.Label(password_window, text="", font=("Arial", 12), bg="#f2f2f2", fg="#ff0000")
    error_label.pack()
    
# Define the function to be executed when the second button is clicked
def button2_clicked():
    # Create a password prompt dialog box
    password_window = tk.Toplevel(root)
    password_window.title("Enter Password")
    password_window.geometry("300x200")
    password_label = tk.Label(password_window, text="Enter Password:")
    password_label.pack()
    password_entry = tk.Entry(password_window, show="*")
    password_entry.pack()
    def ok_button():
        if password_entry.get()==password:
            subprocess.run([enable_path], text=True)
            password_window.destroy()
            success_label.config(text="Camera Enabled Successfully")
        else:
            error_label.config(text="Incorrect password. Please try again.")
            password_entry.delete(0, tk.END)
    ok_button = tk.Button(password_window, text="OK", command=ok_button)
    ok_button.pack()
    error_label = tk.Label(password_window, text="", font=("Arial", 12), bg="#f2f2f2", fg="#ff0000")


info_button = tk.Button(root, text="Project Info",font=("Arial", 14, "bold"),bg="red",fg="white",command=project_info)
info_button.pack(pady=20)
project_label = tk.Label(root,text="Preventing Spyware!!!",font=("Arial", 18,"bold"),bg="black",fg="white")
project_label.pack(pady=25)
# Create a PhotoImage object with the image file
image = tk.PhotoImage(file="image_cam.png")
# Decrease the width and height by a factor of 2
new_width = image.width() // 2
new_height = image.height() // 2


# Scale down the image using subsample()
image = image.subsample(2)
# Create a label and set the image
label = tk.Label(root, image=image)
label.pack()


button1 = tk.Button(button_frame, text="Disable Camera",font=("Arial", 14, "bold"),padx=10, pady=5,command=button1_clicked,bg="red",fg="white")
button2 = tk.Button(button_frame, text="Enable Camera",font=("Arial", 14, "bold"),padx=10, pady=5,command=button2_clicked,bg="red",fg="white")
# Pack the buttons in the frame

button1.pack(side="top", fill="x", padx=50, pady=10)
button2.pack(side="bottom", fill="x", padx=50, pady=10)

# Pack the frame in the root window
button_frame.pack(expand=True)


# Start the main event loop
root.mainloop()

import tkinter as tk
from tkinter import messagebox

# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()
    # Here you can add your logic to check the username and password 
    if username == "avni05_code" and password == "1062":
        messagebox.showinfo("login successful", "welcome to the coder's environment!")
    else:
        messagebox.showerror("login failed", "Invalid username or password.")
        
 # Create the main window 
root = tk.Tk()
root.title("Login page")    
root.geometry("300*200")
root.configure(bg="#2e2e2e") 
 
# create and place the username label and entry 
label_username = tk.Label(root, text="username:", bg="#2e2e2e", fg="#ffffff") 
label_username.pack(padx=10)
entry_username = tk.Entry(root, bg="#3e3e3e", fg="#ffffff", insertbackground='black')     
entry_username.pack(pady=5)   

# create and place the password label and entry
label_password = tk.Label(root, text="Password", bg="#2e2e2e", fg="#ffffff")
label_password.pack(pady=10)
entry_password = tk.Entry(root, show="*", bg="#3e3e3e", fg="#ffffff", insertbackground='black')
entry_password.pack(pady=5)

# create and place the login button 
button_login = tk.Button(root, text="login", command=login, bg="#4CAF50", fg="#ffffff")
button_login.pack(pady=20)

# run the applicarion
root.mainloop()
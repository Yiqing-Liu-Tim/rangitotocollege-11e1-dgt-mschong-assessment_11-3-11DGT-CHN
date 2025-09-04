import tkinter as tk
from tkinter import messagebox
# Create the main window
root = tk.Tk()
root.withdraw()  # Hide the main window
l, m = root.maxsize()
root.geometry(f"{l}x{m}+0+0")
root.title("RETRO GAME")
root.resizeble = False
root.configure(bg="black")
root.attributes("-fullscreen", True)# Enable fullscreen mode
root.iconbitmap('Python\icon.ico')# Set the window icon
welcome_label = tk.Label(root, text="WELCOME TO RETRO GAME", font=("Arial", 40), bg="black", fg="white")
welcome_label.pack(pady=50)
esc = tk.Button(root, text="PRESS ESC TO EXIT", font=("Arial", 20), bg="black", fg="white", command=root.quit)
esc.pack(pady=20)
# Create a new window for sign-in
def save_user_name():
    name = user_name.get()
    if name != "":
        sign_in.destroy()
        messagebox.showinfo("Success", "User name saved successfully!")
        root.deiconify()  # Show the main window
    else:
        messagebox.showwarning("Input Error", "Please enter a user name.")
        user_name.focus_set()
sign_in = tk.Toplevel(root)
sign_in.title("SIGN IN")
sign_in.geometry("400x400+500+100")
sign_in.iconbitmap('Python\icon.ico')
sign_in.configure(bg="black")
sign_in.resizable(False, False)
sign_in.attributes("-topmost", True)  # Keep the sign-in window on top
user_name_label = tk.Label(sign_in, text="ENTER USER NAME", font=("Arial", 20), bg="black", fg="white")
user_name_label.pack(pady=20)
user_name = tk.Entry(sign_in, font=("Arial", 20), bg="black", fg="white", insertbackground="white")
user_name.focus_set()# Set focus to the entry widget
sign_in.protocol("WM_DELETE_WINDOW", save_user_name)  # Close the main window if sign-in is closed

save_user_name_btn = tk.Button(sign_in, text="SAVE", font=("Arial", 20), bg="black", fg="white", command=save_user_name)
save_user_name_btn.pack(pady=20)
user_name.pack(pady=20)
root.mainloop()
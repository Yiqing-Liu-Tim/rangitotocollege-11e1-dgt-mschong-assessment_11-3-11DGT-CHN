import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
#root.withdraw()  # Hide the main window
l, m = root.maxsize()
root.geometry(f"{l}x{m}+0+0")
root.title("RETRO GAME")
root.resizeble = False
root.configure(bg="black")
root.attributes("-fullscreen", True)
root.iconbitmap('Python\icon.ico')
sign_in = tk.Toplevel(root)
sign_in.title("SIGN IN")
sign_in.geometry("400x400+500+200")
sign_in.iconbitmap('Python\icon.ico')
sign_in.configure(bg="black")
sign_in.resizable(False, False)
user_name_label = tk.Label(sign_in, text="ENTER USER NAME", font=("Arial", 20), bg="black", fg="white")
user_name_label.pack(pady=20)
user_name = ""
user_name = tk.Entry(sign_in, font=("Arial", 20), bg="black", fg="white", insertbackground="white")
def save_user_name():
    name = user_name.get()
    if name != "":
        messagebox.showinfo("Success", "User name saved successfully!")
        sign_in.destroy()
    else:
        messagebox.showwarning("Input Error", "Please enter a user name.")
        user_name.focus_set()
save_user_name_btn = tk.Button(sign_in, text="SAVE", font=("Arial", 20), bg="black", fg="white", command=save_user_name)
save_user_name_btn.pack(pady=20)
user_name.pack(pady=20)
root.mainloop()
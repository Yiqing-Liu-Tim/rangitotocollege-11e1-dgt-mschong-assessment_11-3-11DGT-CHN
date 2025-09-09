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
esc = tk.Button(root, text="EXIT", font=("Arial", 20), bg="black", fg="white", command=root.quit)
esc.place(x=0, y=0)

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
stop_sign_in = Button = tk.Button(sign_in, text="CLOSE", font=("Arial", 20), bg="black", fg="white", command=root.quit)
stop_sign_in.pack(pady=20)
#sign_in.attributes("-topmost", True)  # Keep the sign-in window on top
user_name_label = tk.Label(sign_in, text="ENTER USER NAME", font=("Arial", 20), bg="black", fg="white")
user_name_label.pack(pady=20)
user_name = tk.Entry(sign_in, font=("Arial", 20), bg="black", fg="white", insertbackground="white")
user_name.focus_set()# Set focus to the entry widget
sign_in.protocol("WM_DELETE_WINDOW", save_user_name)  # Close the main window if sign-in is closed

save_user_name_btn = tk.Button(sign_in, text="SAVE", font=("Arial", 20), bg="black", fg="white", command=save_user_name)
save_user_name_btn.pack(pady=20)
user_name.pack(pady=20)

def open_tic_tac_toe():
    root.withdraw()  # Hide the main window
    choose_mode()

def choose_mode():
    tic_tac_toe = tk.Tk()
    tic_tac_toe.withdraw()  # Hide the main window
    tic = tk.Toplevel(tic_tac_toe)
    tic.title("TIC-TAC-TOE")
    tic.geometry("400x400+500+100")
    tic.iconbitmap('Python\icon.ico')
    tic.configure(bg="black")
    tic.resizable(False, False)
    tic_label = tk.Label(tic, text="choose your mode", font=("Arial", 20), bg="black", fg="white")
    tic_label.pack(pady=20)
    single_player_btn = tk.Button(tic, text="SINGLE PLAYER", font=("Arial", 20), bg="black", fg="white")
    single_player_btn.pack(pady=20)
    play_with_friend_btn = tk.Button(tic, text="PLAY WITH FRIEND", font=("Arial", 20), bg="black", fg="white", command=play_with_friend)
    play_with_friend_btn.pack(pady=20)

def play_with_friend():
    tic_tac_toe = tk.Tk()
    tic_tac_toe.title("TIC-TAC-TOE")
    tic_tac_toe.geometry("400x400+500+100")
    tic_tac_toe.iconbitmap('Python\icon.ico')
    tic_tac_toe.configure(bg="black")
    tic_tac_toe.resizable(False, False)
    tic_label = tk.Label(tic_tac_toe, text="Play with friend", font=("Arial", 20), bg="black", fg="white")
    tic_label.pack(pady=20)

e_tic = tk.Button(root, text="Tic-tac-toe", font=("Arial", 25), bg="black", fg="white",height=3,width=30, command=open_tic_tac_toe)
e_star = tk.Button(root, text="Star Game", font=("Arial", 25), bg="black", fg="white", height=3,width=30)
e_balloon = tk.Button(root, text="Balloon Game", font=("Arial", 25), bg="black", fg="white", height=3,width=30)
e_tic.place(x=l//2 - 275, y=m//2 - 300)
e_star.place(x=l//2 - 275, y=m//2)
e_balloon.place(x=l//2 - 275, y=m//2 + 300)
root.mainloop()
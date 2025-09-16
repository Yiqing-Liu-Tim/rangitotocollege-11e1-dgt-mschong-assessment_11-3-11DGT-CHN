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
stop_sign_in = tk.Button(sign_in, text="CLOSE", font=("Arial", 20), bg="black", fg="white", command=root.quit)
stop_sign_in.pack(pady=20)
sign_in.attributes("-topmost", True)  # Keep the sign-in window on top
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

def play_with_friend():
    tic_tac_toe = tk.Tk()
    tic_tac_toe.title("TIC-TAC-TOE")
    tic_tac_toe.geometry("315x360+500+100")
    tic_tac_toe.iconbitmap('Python\icon.ico')
    tic_tac_toe.resizable(False, False)
    tic_tac_toe.attributes("-topmost", True)  # Keep the game window on top
    clicked = True
    count = 0
    winner = False

    #check if game is won or not
    def checkifwon():
        nonlocal winner
        #check for X
        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
            b1.configure(bg="lightgreen")
            b2.configure(bg="lightgreen")
            b3.configure(bg="lightgreen")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins!")
            tic_tac_toe.destroy()
        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
            b4.configure(bg="lightgreen")
            b5.configure(bg="lightgreen")
            b6.configure(bg="lightgreen")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins!")
            tic_tac_toe.destroy()
        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
            b7.configure(bg="lightgreen")
            b8.configure(bg="lightgreen")
            b9.configure(bg="lightgreen")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins!")
            tic_tac_toe.destroy()
        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
            b1.configure(bg="lightgreen")
            b4.configure(bg="lightgreen")
            b7.configure(bg="lightgreen")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins!")
            tic_tac_toe.destroy()
        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
            b2.configure(bg="lightgreen")
            b5.configure(bg="lightgreen")
            b8.configure(bg="lightgreen")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins!")
            tic_tac_toe.destroy()
        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            b3.configure(bg="lightgreen")
            b6.configure(bg="lightgreen")
            b9.configure(bg="lightgreen")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins!")
            tic_tac_toe.destroy()
        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            b1.configure(bg="lightgreen")
            b5.configure(bg="lightgreen")
            b9.configure(bg="lightgreen")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins!")
            tic_tac_toe.destroy()
        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
            b3.configure(bg="lightgreen")
            b5.configure(bg="lightgreen")
            b7.configure(bg="lightgreen")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congratulations! X wins!")
            tic_tac_toe.destroy()
        #check for O
        elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
            b1.configure(bg="lightgreen")
            b2.configure(bg="lightgreen")
            b3.configure(bg="lightgreen")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins!")
            tic_tac_toe.destroy()
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            b4.configure(bg="lightgreen")
            b5.configure(bg="lightgreen")
            b6.configure(bg="lightgreen")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins!")
            tic_tac_toe.destroy()
        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            b7.configure(bg="lightgreen")
            b8.configure(bg="lightgreen")
            b9.configure(bg="lightgreen")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins!")
            tic_tac_toe.destroy()
        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            b1.configure(bg="lightgreen")
            b4.configure(bg="lightgreen")
            b7.configure(bg="lightgreen")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins!")
            tic_tac_toe.destroy()
        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            b2.configure(bg="lightgreen")
            b5.configure(bg="lightgreen")
            b8.configure(bg="lightgreen")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins!")
            tic_tac_toe.destroy()
        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            b3.configure(bg="lightgreen")
            b6.configure(bg="lightgreen")
            b9.configure(bg="lightgreen")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins!")
            tic_tac_toe.destroy()
        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            b1.configure(bg="lightgreen")
            b5.configure(bg="lightgreen")
            b9.configure(bg="lightgreen")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins!")
            tic_tac_toe.destroy()
        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            b3.configure(bg="lightgreen")
            b5.configure(bg="lightgreen")
            b7.configure(bg="lightgreen")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Congratulations! O wins!")
            tic_tac_toe.destroy()
        elif count == 9 and winner == False:
            messagebox.showinfo("Tic Tac Toe", "It's a tie!\nNo one wins!")
            tic_tac_toe.destroy()                                      

    #X starting with true
        
    #click function 
    def b_click(b):
        nonlocal clicked, count
        if b["text"] == " " and clicked == True:
            b["text"] = "X"
            clicked = False
            count += 1
            checkifwon()
        elif b["text"] == " " and clicked == False:
            b["text"] = "O"
            clicked = True
            count += 1
            checkifwon()
        else:
            messagebox.showerror("Tic Tac Toe", "That box has already been selected\nPick another box")



    b1 = tk.Button(tic_tac_toe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b1))
    b2 = tk.Button(tic_tac_toe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b2))
    b3 = tk.Button(tic_tac_toe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b3))

    b4 = tk.Button(tic_tac_toe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b4))
    b5 = tk.Button(tic_tac_toe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b5))
    b6 = tk.Button(tic_tac_toe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b6))

    b7 = tk.Button(tic_tac_toe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b7))
    b8 = tk.Button(tic_tac_toe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b8))
    b9 = tk.Button(tic_tac_toe, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    tic_tac_toe.mainloop()

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
    play_with_friend_btn = tk.Button(tic, text="PLAY WITH FRIEND", font=("Arial", 20), bg="black", fg="white", command = play_with_friend)
    play_with_friend_btn.pack(pady=20)



e_tic = tk.Button(root, text="Tic-tac-toe", font=("Arial", 25), bg="black", fg="white",height=3,width=30, command=open_tic_tac_toe)
e_star = tk.Button(root, text="Star Game", font=("Arial", 25), bg="black", fg="white", height=3,width=30)
e_balloon = tk.Button(root, text="Balloon Game", font=("Arial", 25), bg="black", fg="white", height=3,width=30)
e_tic.place(x=l//2 - 275, y=m//2 - 300)
e_star.place(x=l//2 - 275, y=m//2)
e_balloon.place(x=l//2 - 275, y=m//2 + 300)
root.mainloop()
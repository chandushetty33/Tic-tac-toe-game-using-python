import tkinter as tk
from tkinter import messagebox

def check_winner():
    for pattern in win_patterns:
        a, b, c = pattern
        if board[a]["text"] == board[b]["text"] == board[c]["text"] != "":
            show_winner(board[a]["text"])
            return
    if all(button["text"] != "" for button in board):
        show_winner("Draw")

def show_winner(winner):
    win_window = tk.Toplevel(root)
    win_window.title("Game Over")
    win_window.geometry("300x150")
    win_window.configure(bg="lightyellow")
    
    msg = f"Congratulations! Winner is {winner}" if winner != "Draw" else "It's a Draw!"
    label = tk.Label(win_window, text=msg, font=("Arial", 14, "bold"), bg="lightyellow", fg="black")
    label.pack(pady=20)
    
    btn = tk.Button(win_window, text="OK", font=("Arial", 12, "bold"), bg="#191913", fg="white", command=lambda: [win_window.destroy(), reset_game()])
    btn.pack()

def on_click(index):
    global turnO
    if board[index]["text"] == "":
        board[index]["text"] = "O" if turnO else "X"
        board[index]["fg"] = "green" if turnO else "black"
        board[index]["bg"] = "lightgray"
        turnO = not turnO
        check_winner()

def reset_game():
    global turnO
    turnO = True
    for button in board:
        button["text"] = ""
        button["bg"] = "white"

def new_game():
    reset_game()

root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(bg="lightcyan")

turnO = True
win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

board = []
frame = tk.Frame(root, bg="lightcyan")
frame.pack()

for i in range(9):
    button = tk.Button(frame, text="", font=("Arial", 24, "bold"), height=2, width=5,
                       bg="white", fg="black", relief="raised", bd=5,
                       command=lambda i=i: on_click(i))
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    board.append(button)

reset_button = tk.Button(root, text="Reset Game", font=("Arial", 16, "bold"), bg="#191913", fg="white", 
                         relief="raised", bd=5, command=reset_game)
reset_button.pack(pady=10)

new_game_button = tk.Button(root, text="New Game", font=("Arial", 16, "bold"), bg="#004d99", fg="white", 
                            relief="raised", bd=5, command=new_game)
new_game_button.pack(pady=10)

root.mainloop()

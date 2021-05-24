from tkinter import *
from tkinter import messagebox
from random import choice

root = Tk()
root.title("Rock- Paper- Scissors")
root.geometry("260x300")
root.iconbitmap("image/rps.ico")
root.configure(bg="#1f211f")

your_choice = ""
computer_choice = ""
result = ""
win = ""
overall_win = ""

# Stats
no_of_games = 0
your_win = 0
your_win_ratio = 0
comp_win = 0
comp_win_ratio = 0
draw_no = 0

# define rock button function
def rock():
    global your_choice, computer_choice
    # Your choice
    your_choice = "Rock"
    player_choice_label = Label(root, text="Your's Choice: {}".format(your_choice), bg="#202421", fg="#ffffff")
    player_choice_label.place(x=38, y=170)

    # Computer Choice
    choices = ["Rock", "Paper", "Scissor"]
    computer_choice = choice(choices)
    comp_choice_label = Label(root, text="Computer's Choice: {}".format(computer_choice), bg="#202421", fg="#ffffff")
    comp_choice_label.place(x=10, y=195)

    # Decide winner by calling winner function
    winner()

    # deletes the lines
    player_choice_label.place_forget()
    comp_choice_label.place_forget()

# define paper button function
def paper():
    global your_choice, computer_choice
    # Your choice
    your_choice = "Paper"
    player_choice_label = Label(root, text="Your's Choice: {}".format(your_choice), bg="#202421", fg="#ffffff")
    player_choice_label.place(x=38, y=170)

    # Computer Choice
    choices = ["Rock", "Paper", "Scissor"]
    computer_choice = choice(choices)
    comp_choice_label = Label(root, text="Computer's Choice: {}".format(computer_choice), bg="#202421", fg="#ffffff")
    comp_choice_label.place(x=10, y=195)

    # Decide winner by calling winner function
    winner()

    # delete the lines
    player_choice_label.place_forget()
    comp_choice_label.place_forget()

#define scissor button function
def scissor():
    global your_choice, computer_choice, choices_g
    # Your choice
    your_choice = "Scissor"
    player_choice_label = Label(root, text="Your's Choice: {}".format(your_choice), bg="#202421", fg="#ffffff")
    player_choice_label.place(x=38, y=170)

    # Computer Choice
    choices_g = ["Rock", "Paper", "Scissor"]
    computer_choice = choice(choices_g)
    comp_choice_label = Label(root, text="Computer's Choice: {}".format(computer_choice), bg="#202421", fg="#ffffff")
    comp_choice_label.place(x=10, y=195)

    # Decide winner by calling winner function
    winner()

    # delete the lines
    player_choice_label.place_forget()
    comp_choice_label.place_forget()

# reveal winner
def winner():
    global result
    global win
    global no_of_games
    # defining possibilities of winning and loosing
    if your_choice == "Rock" and computer_choice == "Paper":
        win = "Computer Won!"
    elif your_choice == "Paper" and computer_choice == "Rock":
        win = "You Won!"
    elif your_choice == "Rock" and computer_choice == "Scissor":
        win = "You Won!"
    elif your_choice == "Scissor" and computer_choice == "Rock":
        win = "Computer Won!"
    elif your_choice == "Paper" and computer_choice == "Scissor":
        win = "Computer Won!"
    elif your_choice == "Scissor" and computer_choice == "Paper":
        win = "You Won!"
    else:
        win = "Draw!"

    # put the result in a message box as it popups
    result = messagebox.showinfo("Result", win)

    # increment every time when popup appear
    no_of_games += 1

    # calls stats function
    stats()

# Statistics of players
def stats():
    global your_win, comp_win, draw_no, your_win_ratio, comp_win_ratio, overall_win
    # Number of player wins
    if win == "You Won!":
        your_win += 1

    # Number of computer wins
    elif win == "Computer Won!":
        comp_win += 1

    # Number of draws
    elif win == "Draw!":
        draw_no += 1

    # gives the winning ratio of player and computer
    your_win_ratio = your_win / no_of_games
    comp_win_ratio = comp_win / no_of_games

    # compares winning ratio do decide overall winner
    if your_win_ratio > comp_win_ratio:
        overall_win = "You are the Winner!"
    elif comp_win_ratio > your_win_ratio:
        overall_win = "Computer is the Winner!"
    else:
        overall_win = "It's a Draw!"

# function which opens second window for stats
def score():
    score_window = Toplevel()
    score_window.title("Results")
    score_window.geometry("350x300")
    score_window.configure(bg="#1f211f")

    # defining stats
    total_game_label = Label(score_window, text="Games played:{0}{1}".format("\t\t", no_of_games), bg="#202421", fg="#ffffff")
    total_game_label.grid(row=0, column=0, padx=10, pady=1)

    your_win_label = Label(score_window, text="Your winnings:{0}{1}".format("\t\t", your_win), bg="#202421", fg="#ffffff")
    your_win_label.grid(row=1, column=0, padx=10, pady=1)

    comp_game_label = Label(score_window, text="Computer winnings:{0}{1}".format("\t", comp_win), bg="#202421", fg="#ffffff")
    comp_game_label.grid(row=2, column=0, padx=10, pady=1)

    draw_game_label = Label(score_window, text="Draws:{0}{1}".format("\t\t\t", draw_no), bg="#202421", fg="#ffffff")
    draw_game_label.grid(row=3, column=0, padx=10, pady=1)

    ratio_label = Label(score_window, text="Your winning ratio:{0}{1}\n\nComputer winning ratio:{2}{3}".format("\t", your_win_ratio, "\t", comp_win_ratio), bg="#202421", fg="#ffffff", relief=SUNKEN, border=5, padx=30, pady=5)
    ratio_label.grid(row=4, column=0, padx=10, pady=(1, 10))

    overall_win_label = Label(score_window, text="Overall winner:{0}{1}".format("\t\t", overall_win), bg="#202421", fg="#ffffff")
    overall_win_label.grid(row=5, column=0, padx=10, pady=1)

    close_button = Button(score_window, text="Close", bg="#202421", fg="#ffffff", border=5, padx=20, command=score_window.destroy)
    close_button.place(x=150, y=250)

# this function reset the stats value when reset button is clicked
def reset():
    global your_win, comp_win, draw_no, your_win_ratio, comp_win_ratio, overall_win, no_of_games
    no_of_games = 0
    your_win = 0
    your_win_ratio = 0
    comp_win = 0
    comp_win_ratio = 0
    draw_no = 0
    overall_win = ""

# Defining buttons
rock_button = Button(root, text="Rock", padx=30, pady=10, bg="#202421", fg="#ffffff", border=5, command=rock)
rock_button.place(x=80, y=10)

paper_button = Button(root, text="Paper", padx=28, pady=10, bg="#202421", fg="#ffffff", border=5, command=paper)
paper_button.place(x=80, y=62)

scissor_button = Button(root, text="Scissor", padx=25, pady=10, bg="#202421", fg="#ffffff", border=5, command=scissor)
scissor_button.place(x=80, y=113)

score_button = Button(root, text="Check Score", padx=10, bg="#202421", fg="#ffffff", border=5, command=score)
score_button.place(x=150, y=260)

reset_score_button = Button(root, text="Reset Score", padx=10, bg="#202421", fg="#ffffff", border=5, command=reset)
reset_score_button.place(x=10, y=260)


root.mainloop()
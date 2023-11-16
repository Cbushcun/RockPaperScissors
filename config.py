#-------
#Imports
#-------
import sys
import tkinter as tk
from tkinter import ttk
import random as rand

#---------
#Variables
#---------
background_color = '#d9cfe8'

#----------------------------
#Tkinter window configuration
#----------------------------
root = tk.Tk()
style = ttk.Style()

root.title("Rock Paper Scissors")
root.geometry("450x150")
root.minsize(width=450, height=150)

style.configure('.', background=background_color)

container = ttk.Frame(root)
container.pack(expand=True, fill='both')

container_button = ttk.Frame(container)
container_button.pack(side='bottom', pady=10)

#---------
#Functions
#---------

def get_bot_result():
    bot_result = rand.randint(1,3)
    bot_choice = ''
    if bot_result == 1:
        bot_choice = 'Rock'
    elif bot_result == 2:
        bot_choice = 'Paper'
    else:
        bot_choice = 'Scissors'
    return bot_choice


def get_winner(button_input):
    bot = get_bot_result()
    player = button_input
    label_bot.config(text='Bot Selection: ' + bot)
    label_player.config(text='Player Selection: ' + player)
    duel = (player, bot)
    player_win = [('Rock', 'Scissors'), ('Scissors', 'Paper'), ('Paper', 'Rock')]
    bot_win = [('Rock', 'Paper'), ('Paper', 'Scissors'), ('Scissors','Rock')]

    if duel in player_win or duel in bot_win:
        if duel in player_win:
            label_result.config(text='Player wins!')
        else:
            label_result.config(text='Bot wins!')
    else:
        label_result.config(text='Its a tie!')
        
#---------------
#Tkinter widgets
#---------------


label_bot = ttk.Label(container, text="Bot Selection: ")
label_bot.pack(side='top', pady=10)

label_player = ttk.Label(container, text="Your Selection: ")
label_player.pack(side='top', pady=10)

label_result = ttk.Label(container, text='')
label_result.pack()

button_rock = ttk.Button(container_button, text='Rock', command=lambda: get_winner('Rock'))
button_rock.pack(side='left', padx=5)

button_paper = ttk.Button(container_button, text='Paper', command=lambda: get_winner('Paper'))
button_paper.pack(side='left', padx=5)

button_scissors = ttk.Button(container_button, text='Scissors', command=lambda: get_winner('Scissors'))
button_scissors.pack(side='left', padx=5)

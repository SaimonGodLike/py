import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    choices = ["Камень", "Ножницы", "Бумага"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Ничья"
    elif (
        (player_choice == "Камень" and computer_choice == "Ножницы") or
        (player_choice == "Ножницы" and computer_choice == "Бумага") or
        (player_choice == "Бумага" and computer_choice == "Камень")
    ):
        return "Вы победили!"
    else:
        return "Вы проиграли."

def play_game(player_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    message = f"Вы выбрали: {player_choice}\nКомпьютер выбрал: {computer_choice}\n{result}"
    messagebox.showinfo("Результат", message)

def create_gui():
    window = tk.Tk()
    window.title("Камень, ножницы, бумага")

    label = tk.Label(window, text="Выберите ваш вариант:")
    label.pack(pady=10)

    choices = ["Камень", "Ножницы", "Бумага"]
    for choice in choices:
        button = tk.Button(window, text=choice, command=lambda c=choice: play_game(c))
        button.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
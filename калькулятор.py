import tkinter as tk
import re
from sympy import symbols, simplify

def calculate():
    expression = entry.get()
    try:
        expression = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expression)

        x = symbols('x')
        result = simplify(expression)
        result_label.config(text=f"Результат: {result}", fg="white")  
    except Exception as e:
        result_label.config(text=f"Ошибка: {str(e)}", fg="red") 

root = tk.Tk()
root.title("Командный калькулятор")

root.configure(bg="#202020") 

entry = tk.Entry(root, width=20, bg="#303030", fg="white") 
calculate_button = tk.Button(root, text="Вычислить", command=calculate, bg="#404040", fg="white")  
result_label = tk.Label(root, text="Результат: ", bg="#202020", fg="white") 

entry.grid(row=0, column=0, padx=10, pady=10)
calculate_button.grid(row=0, column=1, padx=10, pady=10)
result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

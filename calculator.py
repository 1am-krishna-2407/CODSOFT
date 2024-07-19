import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculate():
    num1 = entry_num1.get()
    num2 = entry_num2.get()
    operation = operation_var.get()

    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == 'Add':
            result = add(num1, num2)
        elif operation == 'Subtract':
            result = subtract(num1, num2)
        elif operation == 'Multiply':
            result = multiply(num1, num2)
        elif operation == 'Divide':
            result = divide(num1, num2)
        
        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")


root = tk.Tk()
root.title("Simple Calculator")


entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)

operation_var = tk.StringVar(root)
operation_var.set("Operation")  
operation_menu = tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide")

calculate_button = tk.Button(root, text="Calculate", command=calculate)
result_label = tk.Label(root, text="Result: ")

entry_num1.grid(row=0, column=0, padx=20, pady=20)
operation_menu.grid(row=0, column=1, padx=20, pady=20)
entry_num2.grid(row=0, column=2, padx=20, pady=20)
calculate_button.grid(row=1, column=0, columnspan=3, padx=20, pady=20)
result_label.grid(row=2, column=0, columnspan=3, padx=20, pady=20)

root.mainloop()
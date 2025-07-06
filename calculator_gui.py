import tkinter as tk

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = num1 / num2
        result_label.config(text=str(result))
    except ValueError:
        result_label.config(text="Error: Invalid input")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create and place widgets
label1 = tk.Label(root, text="Number 1:")
label1.grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(root, text="Number 2:")
label2.grid(row=0, column=2, padx=5, pady=5)
entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=3, padx=5, pady=5)

add_button = tk.Button(root, text="+", command=lambda: calculate('+'))
add_button.grid(row=1, column=0, padx=5, pady=5)

sub_button = tk.Button(root, text="-", command=lambda: calculate('-'))
sub_button.grid(row=1, column=1, padx=5, pady=5)

mul_button = tk.Button(root, text="*", command=lambda: calculate('*'))
mul_button.grid(row=1, column=2, padx=5, pady=5)

div_button = tk.Button(root, text="/", command=lambda: calculate('/'))
div_button.grid(row=1, column=3, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=1, column=4, padx=5, pady=5)

result_label = tk.Label(root, text="Result")
result_label.grid(row=2, column=0, columnspan=5, padx=5, pady=5)

# Start the application
root.mainloop()
import tkinter as tk
import math

# Button layout
button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="],
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0])

# Colors
color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

# Calculator state
expression = ""

def update_label(text):
    label.config(text=text)

def button_clicked(value):
    global expression

    if value == "AC":
        expression = ""
        update_label("0")

    elif value == "=":
        try:
            temp = expression.replace("×", "*").replace("÷", "/")
            result = eval(temp)
            expression = str(result)
            update_label(expression)
        except:
            expression = ""
            update_label("Error")

    elif value == "+/-":
        if expression:
            if expression.startswith("-"):
                expression = expression[1:]
            else:
                expression = "-" + expression
            update_label(expression)

    elif value == "%":
        try:
            expression = str(eval(expression) / 100)
            update_label(expression)
        except:
            update_label("Error")
            expression = ""

    elif value == "√":
        try:
            expression = str(math.sqrt(eval(expression)))
            update_label(expression)
        except:
            update_label("Error")
            expression = ""

    else:
        expression += value
        update_label(expression)

# Window setup
window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)
window.configure(bg=color_black)

frame = tk.Frame(window, bg=color_black)
frame.pack(padx=10, pady=10)

# Display label
label = tk.Label(
    frame,
    text="0",
    font=("Arial", 45),
    bg=color_black,
    fg=color_white,
    anchor="e",
    width=14,
    padx=10
)
label.grid(row=0, column=0, columnspan=column_count, pady=(0, 10))

# Buttons
for row in range(row_count):
    for col in range(column_count):
        value = button_values[row][col]

        bg_color = color_dark_gray
        fg_color = color_white

        if value in top_symbols:
            bg_color = color_light_gray
            fg_color = color_black
        elif value in right_symbols:
            bg_color = color_orange

        button = tk.Button(
            frame,
            text=value,
            font=("Arial", 20),
            width=5,
            height=2,
            bg=bg_color,
            fg=fg_color,
            command=lambda v=value: button_clicked(v)
        )

        button.grid(row=row + 1, column=col, padx=5, pady=5)

window.mainloop()

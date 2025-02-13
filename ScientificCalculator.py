import re
import tkinter as tk
import math
import traceback

def evaluate_expression():
    try:
        expression = entry.get()
        expression = expression.replace("X˟", "**")  # Replace pow with Python exponentiation
        expression = re.sub(r"(\d+)\s*root\s*(\d+)", r"\2 ** (1/\1)", expression)
        result = str(eval(expression))  
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(e))

# def check_expression(expression):
#     try:
#         if 'pow' in expression:
#             match = re.match(r"(\d+)\s*pow\s*(\d+)", expression)
#             if match:
#                 base = int(match.group(1))
#                 expo = int(match.group(2))
#                 handle_multi_input_operations('pow', base, expo)
#             else:
#                 print("The expression is not in the expected format.")
#         else:
#             evaluate_expression()
#     except Exception as e:
#         print(f"Exception: {str(e)}")
#         traceback.print_exc()
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, str(e))

def button_click(value):
    entry.insert(tk.END, value)

def clear_display():
    entry.delete(0, tk.END)

def handle_operation(operation):
    try:
        expression = entry.get()
        if operation == "sin":
            result = math.sin(math.radians(float(expression)))
        elif operation == "cos":
            result = math.cos(math.radians(float(expression)))
        elif operation == "tan":
            result = math.tan(math.radians(float(expression)))
        elif operation == "sqrt":
            result = math.sqrt(float(expression))
        elif operation == "log10[x]":
            result = math.log10(float(expression))
        elif operation == "loge[x]":
            result = math.log1p(float(expression))
        elif operation == "exp":
            result = math.exp(float(expression))
        elif operation == "[x]!":
            result = math.factorial(int(expression))
        elif operation == "2π[x]":
            result = 2*math.pi*float(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        traceback.print_exc()
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# def handle_multi_input_operations(operation, base, expo):
#     try:
#         if operation == "pow":
#             result = math.pow(float(base), expo)  
#             entry.delete(0, tk.END)
#             entry.insert(tk.END, str(result))
#     except Exception as e:
#         print(f"Exception: {str(e)}")
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, str(e))

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, width=40, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("sqrt", 5, 3),
    ("log10[x]", 6, 0), ("exp", 6, 1), ("X˟", 6, 2), ("root", 6, 3),
    ("log[x]", 7, 0), ("[x]!", 7, 1), ("2π[x]", 7, 2), ("C", 7, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 14), command=evaluate_expression)
    elif text == "C":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 14), command=clear_display)
    elif text in ["sin", "cos", "tan", "sqrt", "log10[x]", "exp", "loge[x]","[x]!","2π[x]"]:
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 14), command=lambda op=text: handle_operation(op))
    else:
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 14), command=lambda value=text: button_click(value))
    
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()

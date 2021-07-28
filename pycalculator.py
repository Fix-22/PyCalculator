import tkinter as tk

root = tk.Tk()

root.title("PyCalculator")
root.resizable(False, False)

expression = ""


#functions

def add(value, *args):
    global expression
    expression += value
    print(expression)
    result_label.config(text=expression)

def clear():
    global expression
    expression = ""
    result_label.config(text=expression)

def calculate():
    global expression
    if expression != "":
        try:
            result = eval(expression)
            expression = str(result)
        except:
            result = "Error"
            expression = ""
    
        result_label.config(text=result)

    else:
        result = "Error"
        result_label.config(text=result)
    #expression = str(result)

#result

result_label = tk.Label(root, text="", height=4, font=16)

result_label.grid(row=0, column=0, columnspan=4)

#buttons

button_1 = tk.Button(root, text="1", width= 8, height=4, command=lambda: add("1"))
button_1.grid(row=1, column=0)

button_2 = tk.Button(root, text="2", width= 8, height=4, command=lambda: add("2"))
button_2.grid(row=1, column=1)

button_3 = tk.Button(root, text="3", width= 8, height=4, command=lambda: add("3"))
button_3.grid(row=1, column=2)

button_divide = tk.Button(root, text="/", width= 8, height=4, command=lambda: add("/"))
button_divide.grid(row=1, column=3)

button_4 = tk.Button(root, text="4", width= 8, height=4, command=lambda: add("4"))
button_4.grid(row=2, column=0)

button_5 = tk.Button(root, text="5", width= 8, height=4, command=lambda: add("5"))
button_5.grid(row=2, column=1)

button_6 = tk.Button(root, text="6", width= 8, height=4, command=lambda: add("6"))
button_6.grid(row=2, column=2)

button_multiply = tk.Button(root, text="*", width= 8, height=4, command=lambda: add("*"))
button_multiply.grid(row=2, column=3)

button_7 = tk.Button(root, text="7", width= 8, height=4, command=lambda: add("7"))
button_7.grid(row=3, column=0)

button_8 = tk.Button(root, text="8", width= 8, height=4, command=lambda: add("8"))
button_8.grid(row=3, column=1)

button_9 = tk.Button(root, text="9", width= 8, height=4, command=lambda: add("9"))
button_9.grid(row=3, column=2)

button_subtract = tk.Button(root, text="-", width= 8, height=4, command=lambda: add("-"))
button_subtract.grid(row=3, column=3)

button_clear = tk.Button(root, text="C", width= 8, height=4, command=lambda: clear())
button_clear.grid(row=4, column=0)

button_0 = tk.Button(root, text="0", width= 8, height=4, command=lambda: add("0"))
button_0.grid(row=4, column=1)

button_dot = tk.Button(root, text=".", width= 8, height=4, command=lambda: add("."))
button_dot.grid(row=4, column=2)

button_add = tk.Button(root, text="+", width= 8, height=4, command=lambda: add("+"))
button_add.grid(row=4, column=3)

button_equals = tk.Button(root, text="=", width=36, height=4, command=lambda: calculate())
button_equals.grid(row=5, column=0, columnspan=4)

#keys

root.bind("1", lambda number: add("1"))
root.bind("2", lambda number: add("2"))
root.bind("3", lambda number: add("3"))
root.bind("/", lambda number: add("/"))

root.bind("4", lambda number: add("4"))
root.bind("5", lambda number: add("5"))
root.bind("6", lambda number: add("6"))
root.bind("*", lambda number: add("*"))

root.bind("7", lambda number: add("7"))
root.bind("8", lambda number: add("8"))
root.bind("9", lambda number: add("9"))
root.bind("-", lambda number: add("-"))

root.bind("<BackSpace>", lambda number: clear())
root.bind("0", lambda number: add("0"))
root.bind(".", lambda number: add("."))
root.bind("+", lambda number: add("+"))

root.bind("<Return>", lambda number: calculate())


root.iconbitmap("calculator.ico")


root.mainloop()

import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x500")
        
        self.dark_mode = False
        self.root.configure(bg="grey")
        
        self.equation = ""
        self.display = tk.Entry(root, font=("Arial", 18), bd=10, relief=tk.RIDGE, justify='right', bg="white", fg="black")
        self.display.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=8)
        
        self.create_buttons()
        
    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('^', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('log', 3, 4),





            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('sin', 4, 4),
            ('C', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('(', 5, 3), (')', 5, 4),
            ('Dark Mode', 6, 0, 5)
        ]
        
        for button in buttons:
            text, row, col = button[:3]
            colspan = button[3] if len(button) == 4 else 1
            btn = tk.Button(self.root, text=text, font=("Arial", 14), bd=5, relief=tk.RAISED,
                            command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, columnspan=colspan, ipadx=10, ipady=10, sticky="nsew")
        
    def on_button_click(self, char):
        if char == "C":
            self.equation = ""
        elif char == "=":
            try:
                result = str(eval(self.equation.replace('^', '**')))
                self.save_to_file(self.equation + " = " + result)
                self.equation = result
            except:
                messagebox.showerror("Error", "Invalid Expression")
                self.equation = ""
        elif char == "sqrt":
            try:
                self.equation = str(math.sqrt(float(self.equation)))
            except:
                messagebox.showerror("Error", "Invalid Expression")
        elif char == "log":
            try:
                self.equation = str(math.log10(float(self.equation)))
            except:
                messagebox.showerror("Error", "Invalid Expression")
        elif char == "sin":
            try:
                self.equation = str(math.sin(math.radians(float(self.equation))))
            except:
                messagebox.showerror("Error", "Invalid Expression")
        elif char == "cos":
            try:
                self.equation = str(math.cos(math.radians(float(self.equation))))
            except:
                messagebox.showerror("Error", "Invalid Expression")
        elif char == "tan":
            try:
                self.equation = str(math.tan(math.radians(float(self.equation))))
            except:
                messagebox.showerror("Error", "Invalid Expression")
        elif char == "Dark Mode":
            self.toggle_dark_mode()
        else:
            self.equation += char
        
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.equation)
    
    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        bg_color = "black" if self.dark_mode else "white"
        fg_color = "white" if self.dark_mode else "black"
        self.root.configure(bg=bg_color)
        self.display.configure(bg=bg_color, fg=fg_color)
    
    def save_to_file(self, expression):
        with open("calculations.txt", "a") as file:
            file.write(expression + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        # Create and pack widgets
        self.create_widgets()
    
    def create_widgets(self):
        # Number 1 entry
        self.num1_label = tk.Label(self.root, text="Number 1:")
        self.num1_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Number 2 entry
        self.num2_label = tk.Label(self.root, text="Number 2:")
        self.num2_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Operation choice
        self.operation_label = tk.Label(self.root, text="Operation:")
        self.operation_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.operation_var = tk.StringVar(value="add")
        self.operation_menu = tk.OptionMenu(self.root, self.operation_var, "add", "subtract", "multiply", "divide")
        self.operation_menu.grid(row=2, column=1, padx=10, pady=10)
        
        # Calculate button
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Result label
        self.result_label = tk.Label(self.root, text="Result:")
        self.result_label.grid(row=4, column=0, padx=10, pady=10)
        
        self.result_value = tk.Label(self.root, text="")
        self.result_value.grid(row=4, column=1, padx=10, pady=10)
    
    def calculate(self):
        try:
            # Get numbers and operation
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()
            
            # Perform calculation
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2
            else:
                raise ValueError("Invalid operation")
            
            # Display result
            self.result_value.config(text=str(result))
        
        except ValueError:
            messagebox.showerror("Input Error", "Invalid input. Please enter valid numbers.")
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Cannot divide by zero.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

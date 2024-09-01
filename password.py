import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        
        # Create and pack widgets
        self.create_widgets()
    
    def create_widgets(self):
        # Length label and entry
        self.length_label = tk.Label(self.root, text="Password Length:")
        self.length_label.pack(pady=5)
        
        self.length_entry = tk.Entry(self.root, width=10)
        self.length_entry.pack(pady=5)
        
        # Generate button
        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)
        
        # Password label
        self.password_label = tk.Label(self.root, text="Generated Password:")
        self.password_label.pack(pady=5)
        
        self.password_value = tk.Label(self.root, text="", font=('Arial', 14))
        self.password_value.pack(pady=5)
    
    def generate_password(self):
        try:
            # Get password length
            length = int(self.length_entry.get())
            
            if length <= 0:
                raise ValueError("Length must be a positive integer")
            
            # Define character sets
            characters = string.ascii_letters + string.digits + string.punctuation
            
            # Generate password
            password = ''.join(random.choice(characters) for _ in range(length))
            
            # Display password
            self.password_value.config(text=password)
        
        except ValueError as e:
            tk.messagebox.showerror("Input Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

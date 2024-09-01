import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        # Create the main frame
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)
        
        # Create and pack the widgets
        self.create_widgets()
    
    def create_widgets(self):
        # Label
        self.label = tk.Label(self.frame, text="To-Do List")
        self.label.pack(pady=5)
        
        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(pady=5)
        
        # Entry box to add tasks
        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.pack(pady=5)
        
        # Buttons
        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)
        
        self.delete_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)
        
        self.update_button = tk.Button(self.frame, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=5)
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task")
    
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete")
    
    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            updated_task = self.task_entry.get()
            if updated_task:
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, updated_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

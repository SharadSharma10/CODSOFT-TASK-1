import tkinter as tk
from tkinter import messagebox

# Taking empty tasks list 
tasks = []

# Updating the task  
def update_task_list():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, start=1):
        display_text = f"{i}. {task['title']} - {'Completed' if task['status'] == 'Complete' else 'Pending'}"
        task_listbox.insert(tk.END, display_text)

# Adding the new task
def add_task():
    task_list = task_entry.get() 
    if not task_list.strip():
        messagebox.showinfo("Input error","Task title cannot be empty.")
        return
    else:
        tasks.append({"title": task_list, "status": "pending"})
        update_task_list()
        task_entry.delete(0,tk.END) 

# Deleting the selected task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if not selected_task_index:
        messagebox.showwarning("Selection Error", "No task selected!")
        return
    del tasks[selected_task_index[0]]
    update_task_list()

# Completing the task
def complete_task():
    selected_task_index = task_listbox.curselection()
    if not selected_task_index:
        messagebox.showwarning("lection Error", "No task selected!")
        return
    tasks[selected_task_index[0]]["status"] = "Complete"
    update_task_list()
    
root = tk.Tk()
root.title("To-Do List Application")
root.iconbitmap("to-do-list.ico")
root.geometry("400x400")
root.config(bg="deep sky blue")

# Input frame for task entry
input_frame = tk.Frame(root, bg="deep sky blue")
input_frame.pack(pady=10)

task_entry = tk.Entry(input_frame, font=("Arial", 8), width=40)
task_entry.pack(side=tk.LEFT, padx=5)
    
add_task_button = tk.Button(input_frame,text="Add task",command=add_task, fg="white", bg="dark blue")
add_task_button.pack(side=tk.LEFT)
   
# Task list box
task_listbox_frame = tk.Frame(root, bg="deep sky blue")
task_listbox_frame.pack(pady=10)

task_listbox = tk.Listbox(task_listbox_frame,width=50, height=16)
task_listbox.pack(side=tk.BOTTOM)
    
# Action frame
action_frame = tk.Frame(root, bg="deep sky blue")
action_frame.pack(pady=10)

delete_task_button = tk.Button(action_frame, text="Delete task", command=delete_task, fg="white", bg="red")
delete_task_button.pack(side=tk.LEFT, padx=10)

complete_task_button = tk.Button(action_frame, text="Complete task",command=complete_task, fg="white", bg="green")
complete_task_button.pack(side=tk.LEFT, padx=10)

root.mainloop()

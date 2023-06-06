import tkinter as tk
from tkinter import font
from database_functions import get_tasks, add_task, delete_task, mark_complete

local_tasks = []


def get_object_id(task, tasks):
    # Retrieve the ObjectId of a task from the list
    for i in range(len(tasks)):
        if tasks[i]["task"] == task:
            return tasks[i]["_id"]
    else:
        return None


def check_mark_complete(id, tasks):
    # Check the status of a task based on its ObjectId
    for i in range(len(tasks)):
        if tasks[i]["_id"] == id:
            return tasks[i]["status"]
    else:
        return None


def update_listbox():
    # Update the Listbox with tasks from the database
    tasks = get_tasks()
    listbox.delete(0, tk.END)
    for task in tasks:
        if task["status"] == "complete":
            listbox.insert(tk.END, task["task"])
            listbox.itemconfig(tk.END, fg="green", selectforeground="#4DED30")
        else:
            listbox.insert(tk.END, task["task"])
    global local_tasks
    local_tasks = tasks


def add_item():
    # Add a new task to the database and update the Listbox
    text = entry.get()
    if text:
        if text not in listbox.get(0, tk.END):
            add_task(text, "incomplete")
            update_listbox()
            entry.delete(0, tk.END)


def delete_item():
    # Delete a selected task from the database and Listbox
    selected_index = listbox.curselection()
    if selected_index:
        id = get_object_id(listbox.get(selected_index[0]), local_tasks)
        delete_task(id)
        listbox.delete(selected_index)
        update_listbox()


def mark_item_complete():
    # Mark a selected task as complete or incomplete in the database and update the Listbox
    selected_index = listbox.curselection()
    if selected_index:
        id = get_object_id(listbox.get(selected_index[0]), local_tasks)
        status = check_mark_complete(id, local_tasks)
        if status == "incomplete":
            mark_complete(id, "complete")
        else:
            mark_complete(id, "incomplete")
        update_listbox()


# Create a window
window = tk.Tk()

# Set the window title
window.title("To Do List")

# Create a Tk window with the size of a mobile phone screen
window.geometry("360x640")
window.resizable(0, 0)

# The main frame that includes all the widgets
main_frame = tk.Frame(window, height=640, width=360, bg="#CED3D8")
main_frame.pack(fill=tk.BOTH, expand=True)

# Add a header bar
header = tk.Frame(main_frame, height=50, width=360, bg="#CED3D8")
header.pack(side=tk.TOP)

header_label = tk.Label(header, text="Chamika's List",
                        font=("Times New Roman", 16, "bold italic"), bg="#CED3D8")
header_label.pack(side=tk.TOP, pady=5)

# Main section to display the tasks
main_section = tk.Frame(main_frame, height=580, width=360,
                        bg="#CED3D8", padx=10, pady=10)
main_section.pack(side=tk.TOP)

entry_frame = tk.Frame(main_section, height=50, width=360, bg="#CED3D8")
entry_frame.pack(side=tk.TOP)

entry = tk.Entry(entry_frame, width=20, font=("Helvetica 14 bold"))
entry.pack(side=tk.LEFT, padx=5, pady=5)

add_button = tk.Button(entry_frame, text="Add",
                       command=add_item, width=40, font=("Times New Roman", 10))
add_button.pack(side=tk.LEFT, padx=5, pady=5)

button_frame = tk.Frame(main_section, height=50, width=360, bg="#CED3D8")
button_frame.pack(side=tk.TOP)

delete_button = tk.Button(button_frame, text="Delete",
                          command=delete_item, width=22, font=("Times New Roman", 10))
delete_button.pack(side=tk.LEFT, padx=5, pady=5)

mark_read_button = tk.Button(button_frame, text="Mark Complete",
                             command=mark_item_complete, width=22, font=("Times New Roman", 10))
mark_read_button.pack(side=tk.LEFT, padx=5, pady=5)

listbox_frame = tk.Frame(main_section, height=430,
                         width=360, bg="#CED3D8", padx=5, pady=5)
listbox_frame.pack(side=tk.TOP)

listbox = tk.Listbox(listbox_frame, width=360, height=21, selectbackground="blue", font=(
    "Helvetica 14 bold"), bd=0, highlightthickness=0, bg="#CED3D8")
listbox.pack()

# Add a footer bar
footer = tk.Frame(main_frame, height=50, width=360, bg="#CED3D8")
footer.pack(side=tk.BOTTOM)

footer_label = tk.Label(footer, text="A Simple To Do List App by Chamika", font=(
    "Helvetica 7 italic"), fg="#646D74", bg="#CED3D8")
footer_label.pack(side=tk.BOTTOM, pady=5)

# Update Listbox with tasks
update_listbox()

window.mainloop()

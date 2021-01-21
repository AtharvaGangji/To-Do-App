# ----------------------------------------------------------------------  Imports
import tkinter as tk
from tkinter import *
import pickle

xpo = tk.Tk()

# ---------------------------------------------------------------------- Frame for list box

# We don't need frame for now

"""
my_frame = tk.Frame(xpo)
my_frame.pack()

"""
# ----------------------------------------------------------------------  our list box
my_list = tk.Listbox(
    xpo,
    font = ("Agency FB", 19),
    width = 25,
    height = 5,

    bd = 0,
    fg = "#464646",

    selectbackground = "#a6a6a6",
    activestyle = "none",
)
my_list.pack(anchor = CENTER, pady = 20, padx = 10, fill = BOTH)
my_list.config(justify=CENTER)

# ---------------------------------------------------------------------- Our Entry Box
entry_box = tk.Entry(
    bd = 0,
    width = 30,
)

entry_box.pack(pady = (0, 10))

# ---------------------------------------------------------------------- Our Scroll Bar


# We don't need scroll bar for now


""" my_scroll_bar = tk.Scrollbar(
    my_frame,
)
my_scroll_bar.pack(side = RIGHT, fill = BOTH)


my_list.config(yscrollcommand=my_scroll_bar.set)
my_scroll_bar.config(command = my_list.yview)

"""

# ---------------------------------------------------------------------- Function for Inserting item


def insert_item():
    got_input = entry_box.get()
    my_list.insert(END, got_input)
    entry_box.delete(0, END)

# ---------------------------------------------------------------------- Function for deleting list


def delete_item():
    my_list.delete(0, END)

# ---------------------------------------------------------------------- Function for saving item


def save_item():
    pass #starting

# ---------------------------------------------------------------------- Function for removing item


def remove_item():
    my_list.delete(ANCHOR)

# ---------------------------------------------------------------------- List of Items


list = ["mad", "mad2"]

# ---------------------------------------------------------------------- Lets insert items in the list box
for item in list:
    my_list.insert(END, item)

# ---------------------------------------------------------------------- Our Button Label

button_label = tk.Label(
    xpo,

)
button_label.pack()

# ---------------------------------------------------------------------- Our Button2 Label

button_label2 = tk.Label(
    xpo,

)
button_label2.pack(pady = (0,20))

# ----------------------------------------------------------------------  Remove Item Button


def remove_enter(x):
    remove.config(bg = "#a6a6a6")


def remove_leave(x):
    remove.config(bg="SystemButtonFace")


remove = tk.Button(
    button_label,
    text = "Remove Item",
    command = remove_item,
    border = 0,
    width = 13,
)

remove.bind("<Enter>", remove_enter)
remove.bind("<Leave>", remove_leave)

# ---------------------------------------------------------------------- Insert Item Button


def insert_enter(x):
    insert.config(bg="#a6a6a6")


def insert_leave(x):
    insert.config(bg="SystemButtonFace")


insert = tk.Button(
    button_label,
    text = "Insert Item",
    command = insert_item,
    border = 0,
    width = 13,
)

insert.bind("<Enter>", insert_enter)
insert.bind("<Leave>", insert_leave)

# ---------------------------------------------------------------------- Save Item Button

save = tk.Button(
    button_label2,
    text = "Save",
    command = save_item,
    border = 0,
    width = 20,
    bg = "lime"
)

remove.grid(row = 0, column = 0, padx = 20)
# save.grid(row = 0, column = )
insert.grid(row = 0, column = 1)


def save_enter(x):
    save.config(bg="Green")


def save_leave(x):
    save.config(bg="Lime")


save.pack()

save.bind("<Enter>", save_enter)
save.bind("<Leave>", save_leave)

# ---------------------------------------------------------------------- Delete List Button


def delete_enter(x):
    delete.config(bg="red")


def delete_leave(x):
    delete.config(bg="#E74C3C")


delete = tk.Button(
    button_label2,
    text = "Delete",
    bg = "#E74C3C",
    command = delete_item,
    border = 0,
    width = 20,
)
delete.pack(pady = (7, 20))

delete.bind("<Enter>", delete_enter)
delete.bind("<Leave>", delete_leave)

# ---------------------------------------------------------------------- loop of tkinter
xpo.mainloop()


"""
bg = "SystemButtonFace",
hilightthickness = 0,

# label for our list
list_label = tk.Label(xpo,)


"""
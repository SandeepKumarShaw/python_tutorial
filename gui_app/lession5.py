#Menu Bar creation
import tkinter as tk 
from tkinter import ttk 
window = tk.Tk()
window.title("Menu Bar Tutorial")
# def hello():
#     print("Hello Sandeep")
# menubar = tk.Menu(window)
# menubar.add_command(label = "file", command = hello)
# menubar.add_command(label = "edit", command = hello)
# menubar.add_command(label = "selection", command = hello)
# window.config(menu=menubar)

original_menu_space = tk.Menu(window)
file_menu = tk.Menu(original_menu_space, tearoff = 0)
file_menu.add_command(label = "new file")
file_menu.add_command(label = "open file")
file_menu.add_command(label = "save file")

edit_menu = tk.Menu(original_menu_space, tearoff = 0)
edit_menu.add_command(label = "undo")
edit_menu.add_command(label = "redo")
edit_menu.add_command(label = "cut")

original_menu_space.add_cascade(label = "file",menu = file_menu)
original_menu_space.add_cascade(label = "edit",menu = edit_menu)

window.config(menu=original_menu_space)


window.mainloop()
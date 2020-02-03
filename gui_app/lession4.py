#How to Create Tabs in window
import tkinter as tk 
from tkinter import ttk
window = tk.Tk()
window.title("by using notebook")
note_book = ttk.Notebook(window)
one = ttk.Frame(note_book)
two = ttk.Frame(note_book)
note_book.add(one,text = "tab1")
note_book.add(two,text = "tab2")
note_book.grid(row = 0,column = 0)
note_book.pack(expand = True,fill = "both")

#labels
enter_name_lable = ttk.Label(one,text = "Enter Your Name :-")
enter_name_lable.grid(row = 0,column = 0,sticky = tk.W)

name = tk.StringVar()
name_entry_box = ttk.Entry(one,width = 18,textvariable = name)
name_entry_box.grid(row = 0,column = 1)

surname = tk.StringVar()
surname_entry_box = ttk.Entry(two,width = 18,textvariable = surname)
surname_entry_box.grid(row = 0,column = 1)

window.mainloop()
#Notepad
import tkinter as tk 
from tkinter import ttk 
from tkinter import font,colorchooser,filedialog,messagebox
import os 

main_application = tk.Tk()
main_application.geometry("800x600")
main_application.title("Ms Notepad")

#menu creation
main_menu = tk.Menu()
#file menu and it's submenu
new_icon = tk.PhotoImage(file = "icon2/new.png")
open_icon = tk.PhotoImage(file = "icon2/open.png")
save_icon = tk.PhotoImage(file = "icon2/save.png")
save_as_icon = tk.PhotoImage(file = "icon2/save_as_icon.png")
exit_icon = tk.PhotoImage(file = "icon2/exit.png")

file = tk.Menu(main_menu,tearoff = False)
main_menu.add_cascade(label = "File",menu = file)
file.add_command(label = "New",image = new_icon,compound = tk.LEFT,accelerator = "ctrl+N")
file.add_command(label = "Open",image = open_icon,compound = tk.LEFT,accelerator = "ctrl+O")
file.add_command(label = "Save",image = save_icon,compound = tk.LEFT,accelerator = "ctrl+S")
file.add_command(label = "Save as",image = save_as_icon,compound = tk.LEFT,accelerator = "ctrl+Alt+S")
file.add_command(label = "Exit",image = exit_icon,compound = tk.LEFT,accelerator = "ctrl+")

#Edit menu and it's submenu

copy_icon = tk.PhotoImage(file = "icon2/copy.png")
paste_icon = tk.PhotoImage(file = "icon2/paste.png")
cut_item_icon = tk.PhotoImage(file = "icon2/cut.png")
clear_icon = tk.PhotoImage(file = "icon2/clear_all.png")
find_icon = tk.PhotoImage(file = "icon2/find.png")

edit = tk.Menu(main_menu,tearoff = False)
main_menu.add_cascade(label = "Edit",menu = edit)
edit.add_command(label = "Copy",image = copy_icon,compound = tk.LEFT,accelerator = "ctrl+C")
edit.add_command(label = "Paste",image = paste_icon,compound = tk.LEFT,accelerator = "ctrl+V")
edit.add_command(label = "Cut",image = cut_item_icon,compound = tk.LEFT,accelerator = "ctrl+X")
edit.add_command(label = "Clear all",image = clear_icon,compound = tk.LEFT,accelerator = "ctrl+Alt+S")
edit.add_command(label = "Find",image = find_icon,compound = tk.LEFT,accelerator = "ctrl+F")



# View menu and it's submenu
tool_bar = tk.PhotoImage(file = "icon2/tool_bar.png")
status_bar = tk.PhotoImage(file = "icon2/cstatus_bar.png")

view = tk.Menu(main_menu,tearoff = False)
main_menu.add_cascade(label = "View",menu = view)
view.add_command(label = "Copy",image = tool_bar,compound = tk.LEFT,accelerator = "ctrl+C")
view.add_command(label = "Paste",image = status_bar,compound = tk.LEFT,accelerator = "ctrl+V")





main_application.config(menu = main_menu)



main_application.mainloop()
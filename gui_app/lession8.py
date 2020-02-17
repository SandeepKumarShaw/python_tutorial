#Notepad
import tkinter as tk 
from tkinter import ttk 
from tkinter import font,colorchooser,filedialog,messagebox
import os 
from PIL import ImageTk


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

# new_icon = ""
# open_icon = "" 
# save_icon = ""
# save_as_icon = ""
# exit_icon = ""

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

# copy_icon = "" 
# paste_icon = "" 
# cut_item_icon = ""
# clear_icon = ""
# find_icon = ""

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

# tool_bar = "" 
# status_bar = "" 
view = tk.Menu(main_menu,tearoff = False)
main_menu.add_cascade(label = "View",menu = view)
view.add_checkbutton(label = "Tool Bar",onvalue = True,image = tool_bar,compound = tk.LEFT,accelerator = "ctrl+C")
view.add_checkbutton(label = "Status Bar",onvalue = True,image = status_bar,compound = tk.LEFT,accelerator = "ctrl+V")


#Color menu and it's submenu

light_theme = tk.PhotoImage(file = "icon2/light_default.png")
light_plus_icon = tk.PhotoImage(file = "icon2/light_plus.png")
dark_theme = tk.PhotoImage(file = "icon2/dark.png")
red_theme = tk.PhotoImage(file = "icon2/red.png")
monokia_theme = tk.PhotoImage(file = "icon2/monokia.png")
night_theme = tk.PhotoImage(file = "icon2/night_blue.png")

# light_theme = "" 
# light_plus_icon = "" 
# dark_theme = ""
# red_theme = ""
# monokia_theme = ""
# night_theme =""

color_theme = tk.Menu(main_menu,tearoff = False)
main_menu.add_cascade(label = "Color Theme",menu = color_theme)

color_icons = (light_theme,light_plus_icon,dark_theme,red_theme,monokia_theme,night_theme)
color_dict = {
    'Light Default ' : ('#000000',"#ffffff"),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' :  ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}
count = 0
for i in color_dict:
    color_theme.add_radiobutton(label = i,image = color_icons[count],compound = tk.LEFT)
    count +=1

# ToolBars Label
tool_bar_label = ttk.Label(main_application)
tool_bar_label.pack(side = tk.TOP,fill = tk.x)
font_tuple = tk.font.families()
font_family = tk.StringVar
font_box = ttk.Combobox(tool_bar_label,width= 30,textvariable=font_family,state="readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0,column=0,padx=5,pady=5)

#size box
size_variable = tk.IntVar()
font_size = ttk.Combobox(tool_bar_label,width= 20,textvariable=size_variable,state="readonly")
font_size["values"] = tuple(range(8,100,2))
font_box.current(4)
font_size.grid(row=0,column=1,padx=5,pady=5)

## bold button 

bold_icon = tk.PhotoImage(file = "icons2/bold.png")
bold_btn = ttk.Button(tool_bar_label,image = bold_icon)
bold_btn.grid(row = 0,column = 2 ,padx = 5)

## italic button 
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(tool_bar_label, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

## underline button 
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(tool_bar_label, image = underline_icon)
underline_btn.grid(row = 0, column=4, padx=5)

## font color button 
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar_label, image=font_color_icon)
font_color_btn.grid(row=0, column=5,padx=5)

## align left 
align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar_label, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

## align center 
align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
align_center_btn = ttk.Button(tool_bar_label, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

## align right 
align_right_icon = tk.PhotoImage(file='icons2/align_right.png')
align_right_btn = ttk.Button(tool_bar_label, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)

# text editor 

text_editor = tk.Text(main_application)
text_editor.config(wrap = "word",relief = tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT,fill = tk.Y)
text_editor.pack(fill = tk.BOTH,expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)

# status bar  word and character count 

status_bars = ttk.Label(main_application,text = "Status bar")
status_bars.pack(side = tk.BOTTOM)

text_change = False
def change_word(event = None):
    global text_change
    if text_editor.edit_modified():
        text_change = True
        word = len(text_editor.get(1.0,"end-1c").split())
        chararcter = len(text_editor.get(1.0,"end-1c").replace(" ",""))
        status_bars.config(text = f"character :{chararcter} word :{word}")
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>",change_word)    


main_application.config(menu = main_menu)



main_application.mainloop()
#Message box and Exception handling

import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox as m_box

window = tk.Tk() # window create
window.title("Message box") #window title
#lable Frame

lable_frame = ttk.LabelFrame(window,text = "User Information")
lable_frame.grid(row = 0,column = 0,padx = 40, pady = 10)

#lable
name_label = ttk.Label(lable_frame,text = "Enter Your Name :-",font = ('Helvetica',14))
age_label = ttk.Label(lable_frame,text = "Enter Your Age :-",font = ('Helvetica',14))
#lable grid
name_label.grid(row = 0,column = 0,padx = 5,pady = 5,sticky = tk.W)
age_label.grid(row = 1,column = 0,padx = 5,pady = 5,sticky = tk.W)
#Entry variable
name_var = tk.StringVar()
age_var = tk.StringVar()
#Entrybox
name_entry_box = ttk.Entry(lable_frame,width = 36,textvariable = name_var)
age_entry_box = ttk.Entry(lable_frame,width = 36,textvariable = age_var)
#Entrybox grid(position)
name_entry_box.grid(row = 0,column = 1,padx = 5,pady = 5,sticky = tk.W)
age_entry_box.grid(row = 1,column = 1,padx = 5,pady = 5,sticky = tk.W)
def submit():
    name = name_var.get()
    age = age_var.get()
    if name != "":
        if age != "":
            try:
                age = int(age)
            except ValueError:
                m_box.showerror("title","Only digits are allowed in age field")
            else:
                if age < 18:
                    m_box.showerror("warning","you are not 18, visit this content on your risk")  
                    print(f"Your name is {name} \n your age is {age}")         
        else:
            m_box.showerror("Error","Please fill the age")        

    else:    
        m_box.showerror("Error","Please fill the name")        
#Button submit
submit_btn = ttk.Button(window,text="Submit",command = submit)
submit_btn.grid(row = 1,columnspan = 2,padx = 40)

window.mainloop() # hold the window
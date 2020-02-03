import tkinter as tk 
from tkinter import ttk 
window = tk.Tk()
window.title("Label Frame")
lable_fram = ttk.LabelFrame(window,text = "User Details")
lable_fram.grid(row = 0,column = 0)
#label
label = ["name","surname","Email","Phone number"]
for i in range(len(label)):
    main_label = "label" + str(i)
    main_label = ttk.Label(lable_fram,text = label[i])
    main_label.grid(row = i,column = 0, sticky = tk.W,padx = 5,pady = 2)
#Entry box
user_data = {
    "name":tk.StringVar(),
    "surname":tk.StringVar(),
    "email":tk.StringVar(),
    "phone number":tk.StringVar()
}    
number = 0
for i in user_data:
    main_entrybox = "entry" + i 
    main_entrybox = ttk.Entry(lable_fram,width = 18,textvariable = user_data[i])
    main_entrybox.grid(row = number,column = 1,padx = 5,pady = 2)
    number += 1
def submit():
    print(user_data["name"].get())
    print(user_data["surname"].get())
    print(user_data["email"].get())
    print(user_data["phone number"].get())

submit_btn = ttk.Button(lable_fram, text = "submit", command=submit)
submit_btn.grid(row=5,column=2,padx = 5,pady = 2)

for i in lable_fram.winfo_children():
    i.grid_configure(padx = 4,pady = 4)

#window will not close
window.mainloop()
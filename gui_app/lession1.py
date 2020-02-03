# Introduction to GUI Software Development using Tinker module

#Metho1
# import tkinter
# window = tkinter.Tk()

#Method2
# from tkinter import*
# window = Th()

#method3
import os
from csv import DictWriter
from tkinter import ttk
import tkinter as tk
window = tk.Tk()
window.title("Firt Gui Software")
#labels
enter_name_lable = ttk.Label(window,text = "Enter Your Name :-")
enter_name_lable.grid(row = 0,column = 0,sticky = tk.W)

enter_surname_lable = ttk.Label(window,text = "Enter Your SurName :-")
enter_surname_lable.grid(row = 1,column = 0,sticky = tk.W)

enter_email_lable = ttk.Label(window,text = "Enter Your Email :-")
enter_email_lable.grid(row = 2,column = 0,sticky = tk.W)

enter_gender_lable = ttk.Label(window,text = "Select gender :-")
enter_gender_lable.grid(row = 3,column = 0,sticky = tk.W)

#entry box
name = tk.StringVar()
name_entry_box = ttk.Entry(window,width = 18,textvariable = name)
name_entry_box.grid(row = 0,column = 1)

surname = tk.StringVar()
surname_entry_box = ttk.Entry(window,width = 18,textvariable = surname)
surname_entry_box.grid(row = 1,column = 1)

email = tk.StringVar()
email_entry_box = ttk.Entry(window,width = 18,textvariable = email)
email_entry_box.grid(row = 2,column = 1)

#combox
male_female = tk.StringVar()
new_combo_box = ttk.Combobox(window,width = 18,state="readonly",textvariable = male_female)
new_combo_box["values"] = ("Male","Femal")
new_combo_box.current(0)
new_combo_box.grid(row = 3,column = 1)

#Radio button
user_type = tk.StringVar()
new_radio_btn1 = ttk.Radiobutton(window,text = "Student",value = "student",variable = user_type)
new_radio_btn1.grid(row = 4,column = 0)

new_radio_btn2 = ttk.Radiobutton(window,text = "Teacher",value = "teacher",variable = user_type)
new_radio_btn2.grid(row = 4,column = 1)

#checkbox
condition_var = tk.IntVar()
new_check_box = ttk.Checkbutton(window,text = "check for latest update",variable = condition_var)
new_check_box.grid(row = 5,column = 0)

#button submit
def button_click_function():
    names = name.get()
    surnames = surname.get()
    emails = email.get()
    genders = male_female.get()
    user_teacher_student = user_type.get()
    if condition_var.get() == 0:
        checked = "Please check the checkbox"
    else:
        checked = "you have succesfully checked the check box button"

    #print(f"your name is {names} \n your surname is {surnames} \n your email is {emails}")        
    #print(f"your gender is {genders} \n your usertype is {user_teacher_student}")        

    all_details = (f"your name is {names} \n your surname is {surnames} \n your email is {emails} \n your gender is {genders} \n your usertype is {user_teacher_student}")
    new_label_of_all_detail = ttk.Label(window,text = all_details)
    new_label_of_all_detail.grid(row = 7,column = 0)
    
    with open("zzzz.txt" , "a") as file:
        file.write(f"{names},{surnames},{emails},{genders},{user_teacher_student},{checked}")
    
    with open("vvvzz.csv","a",newlines="") as file:
        new_data = DictWriter(file,fieldnames = ["useranme","surname","email","Gender","type","checkbox"])
        if os.start("vvvzz.csv").st_size == 0:
            new_data.writeheader()
        new_data.writerow({
            "useranme":names,
            "surname":surnames,
            "email":emails,
            "Gender":genders,
            "type":user_teacher_student,
            "checkbox":checked,
        })
    name_entry_box.delete(0,tk.END)
    surname_entry_box.delete(0,tk.END)
    email_entry_box.delete(0,tk.END)
    

new_submit_button = ttk.Button(window,text = "Submit",command = button_click_function)
new_submit_button.grid(row = 6,column = 1)
window.mainloop()
#Login System
from tkinter import*
from tkinter import messagebox 
from PIL import ImageTk


class login_system:
    def __init__(self,window):
        self.window = window
        self.window.title("Login SYstem")
        self.window.geometry("900x600+0+0")

        # All Image
        self.bg_icon = ImageTk.PhotoImage(file = "images/bg.png")
        self.user_icon = PhotoImage(file = "images/man.png")
        self.password_icons = PhotoImage(file = "images/password.png")
        self.logo_icons = PhotoImage(file = "images/logo.png")

        # self.bg_icon = ""
        # self.user_icon = ""
        # self.password_icons =""
        # self.logo_icons = ""

        bg_label = Label(self.window,image = self.bg_icon).pack()
        title = Label(self.window,text = "Login System",font = ("times new roman",40,"bold"),bg = "yellow",fg = "red",bd = 10)
        title.place(x=0,y=0,relwidth=1)

        #frame
        login_frame = Frame(self.window,bg = "white")
        login_frame.place(x=200,y=150)

        logo_label = Label(login_frame,image=self.logo_icons,bd=0).grid(row=0,columnspan=2,pady=20)
        
        #username and password label

        label_user = Label(login_frame,text = "UserName",bg="white",image=self.user_icon,compound = LEFT,font = ("times new roman",20,"bold"))
        label_user.grid(row=1,column=0,padx=20,pady=5) 

        label_password = Label(login_frame,text = "pPassword",bg="white",image=self.password_icons,compound = LEFT,font = ("times new roman",20,"bold"))
        label_password.grid(row=2,column=0,padx=20,pady=5) 

        #username and password Entry Box
        self.user_name = StringVar()
        user_entry_box = Entry(login_frame,bd = 5,textvariable = self.user_name,relief = GROOVE,font = ("",15))
        user_entry_box.grid(row=1,column=0,padx=20)

        self.pass_name = StringVar()
        pass_entry_box = Entry(login_frame,bd = 5,textvariable = self.pass_name,relief = GROOVE,font = ("",15))
        pass_entry_box.grid(row=2,column=0,padx=20)

        #Submit Button
        login_button = Button(login_frame,text="Login",width=15,font=("times new roman",15,"bold"),bg="yellow",fg="red",command=self.login).grid(row=3,column=1,pady=10)
    def login(self):
        if self.user_name.get() == "" or self.pass_name.get() == "":
            messagebox.showerror("Error","Please do not leave blank")
        elif self.user_name.get() == "sandeep" and self.pass_name.get() == "12345":
            messagebox.showinfo("successfully",f"Welcome {self.user_name.get()}")
        else:
            messagebox.showerror("login fail","username and password is incorrect!")        
window = Tk()
obj = login_system(window)
window.mainloop()
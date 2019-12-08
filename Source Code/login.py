from tkinter import *
import tkinter.messagebox
import sqlite3



class login:
    def __init__(self, master, *args, **kwargs):
        self.master = master


        self.heading_0 = Label(master, text="TECHNOZILLA STORE", width=20, font=("bold", 20), bg='skyblue')
        self.heading_0.place(x=90, y=53)

        self.name_1 = Label(master, text="Full Name", width=20, font=("bold", 10), bg='skyblue')
        self.name_1.place(x=80, y=130)

        self.name_e = Entry(master, bg='white', fg='black')
        self.name_e.place(x=240, y=130)

        self.pass_1 = Label(master, text="Password", width=20, font=("bold", 10), bg='skyblue')
        self.pass_1.place(x=80, y=180)

        self.pass_e = Entry(master, bg='white', fg='black', show='*')
        self.pass_e.place(x=240, y=180)

        self.name_e.focus()
        self.l = Button(master, text='LOGIN', width=20, bg='brown', fg='white', command =self.logdata).place(x=180, y=380)


    def logdata(self, *args, **kwargs):

        self.name = self.name_e.get()
        self.password = self.pass_e.get()
        conn = sqlite3.connect("D:\database\store.db")
        with conn:
            c = conn.cursor()


        c.execute('SELECT * FROM logindata WHERE name = ? AND password = ?', (self.name, self.password))
        result = c.fetchone()
        if result:
            tkinter.messagebox.showinfo("Success", "Login is successful")
            self.p1()

        else:
            tkinter.messagebox.showinfo("Error", "Name and Password doesn't match.")



    def p1(self, *args, **kwargs):
        from mainpage import root3



root8 = Tk()
d=login(root8)
root8.geometry("500x500")
root8.title("Login Page")
root8.config(bg="skyblue")
root8.mainloop()


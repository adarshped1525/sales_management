from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
import sqlite3


class Registration:
    def __init__(self, master, *args, **kwargs):
        self.master = master

        self.heading_1 = Label(master, text="Registration Form", width=20, font=("bold", 20), bg='lightslategray')
        self.heading_1.place(x=90, y=53)

        self.name1_1 = Label(master, text="Full Name", width=20, font=("bold", 10), bg='lightslategray')
        self.name1_1.place(x=80, y=130)

        self.name1_e = Entry(master, bg='lightslategray', fg='white')
        self.name1_e.place(x=240, y=130)

        self.email_1 = Label(master, text="Email", width=20, font=("bold", 10), bg='lightslategray')
        self.email_1.place(x=68, y=180)

        self.email_e = Entry(master, bg='lightslategray', fg='white')
        self.email_e.place(x=240, y=180)

        self.pass_2 = Label(master, text="Password", width=20, font=("bold", 10), bg='lightslategray')
        self.pass_2.place(x=68, y=230)

        self.pass2_e = Entry(master, bg='lightslategray', fg='white', show='*')
        self.pass2_e.place(x=240, y=230)

        self.addr_1 = Label(master, text="Address", width=20, font=("bold", 10), bg='lightslategray')
        self.addr_1.place(x=70, y=280)
        self.addr_e = Entry(master, bg='lightslategray', fg='white')
        self.addr_e.place(x=240, y=280)



        self.city_1 = Label(master, text="City", width=20, font=("bold", 10), bg='lightslategray')
        self.city_1.place(x=70, y=330)

        self.city_choose = Combobox(master, values=['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam',
                                         'Bihar', 'Chhattisgarh', 'Chandigarh', 'Dadra and Nagar Haveli',
                                         'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
                                         'jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep',
                                         'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',
                                         'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
                                         'Telagana', 'Tripura', 'Uttarakhand', 'Utter Pradesh', 'West Bengal'])
        self.city_choose.place(x=240, y=330)
        self.city_choose.config(width=20)
        print(dict(self.city_choose))
        self.city_choose.current(1)
        print(self.city_choose.current(), self.city_choose.get())
        """list1 = ['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Chandigarh','Dadra and Nagar Haveli','Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','jammu and Kashmir','Jharkhand','Karnataka','Kerala','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telagana','Tripura','Uttarakhand','Utter Pradesh','West Bengal']
        c = StringVar()
        droplist = OptionMenu(root, c, *list1)
        droplist.config(width=15, bg='lightslategray', fg='white')
        c.set('Select Your City')
        droplist.place(x=240, y=280)"""

        self.name1_e.focus()

        self.btn_data = Button(master, text='REGISTER', width=20, bg='brown', fg='white', command=self.regdata).place(x=180, y=380)

        self.btn_log = Button(master, text='Already have an account?', width=30, bg='brown', fg='white', command = self.p2).place(x=180, y=425)


    def p2(self, *args, **kwargs):
        from login import root8





    def regdata(self, *args, **kwargs):
        self.name = self.name1_e.get()
        self.email = self.email_e.get()
        self.password = self.pass2_e.get()
        self.address = self.addr_e.get()
        self.city = self.city_choose.get()

        conn = sqlite3.connect("D:\database\store.db")
        with conn:
             c = conn.cursor()

        if '@' in self.email:


            c.execute('INSERT INTO logindata ( name, email, password , address , city ) VALUES(?,?,?,?,?)',(self.name, self.email, self.password, self.address, self.city))

            conn.commit()

            tkinter.messagebox.showinfo("Success", "Registration is successful.")

            self.p2()

        else:
            tkinter.messagebox.showinfo("ERROR", "Please enter valid entries.")




root = Tk()
c=Registration(root)
root.geometry('500x500')
root.title("Registration Form")
root.config(bg="lightslategray")
root.mainloop()

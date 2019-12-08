from tkinter import *

import sqlite3
import tkinter.messagebox

conn = sqlite3.connect("D:\database\store.db")
c = conn.cursor()

result = c.execute("SELECT MAX (id) from inventory")
for r in result:
    id = r[0]

class Database:
    def __init__(self, master ,*args, **kwargs):

        self.master= master
        self.heading =  Label(master , text="Add to database", font= ('arial 40 bold '), fg='steelblue')
        self.heading.place(x=400,y=0)

        #LAbels

        self.name_1 = Label(master, text="Enter Product Name", font=('arial 18 bold '))
        self.name_1.place(x=0, y=70)

        self.stock_1 = Label(master, text="Enter Stocks", font=('arial 18 bold '))
        self.stock_1.place(x=0, y=120)

        self.cp_1= Label(master, text="Enter Cost Price", font=('arial 18 bold '))
        self.cp_1.place(x=0, y=170)

        self.sp_1 = Label(master, text="Enter Selling Price", font=('arial 18 bold '))
        self.sp_1.place(x=0, y=220)

        self.vendor_1 = Label(master, text="Enter Vendor Name", font=('arial 18 bold '))
        self.vendor_1.place(x=0, y=270)

        self.vendor_phone_1 = Label(master, text="Enter Vendor Phone Number", font=('arial 18 bold '))
        self.vendor_phone_1.place(x=0, y=320)

        self.id_1 = Label(master, text="Enter ID", font=('arial 18 bold '))
        self.id_1.place(x=0, y=370)

        #Entry

        self.name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.name_e.place(x=380, y=70)

        self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
        self.stock_e.place(x=380, y=120)

        self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.cp_e.place(x=380, y=170)

        self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.sp_e.place(x=380, y=220)

        self.vendor_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_e.place(x=380, y=270)

        self.vendor_phone_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vendor_phone_e.place(x=380, y=320)

        self.id_e = Entry(master, width=25, font=('arial 18 bold'))
        self.id_e.place(x=380, y=370)

        #button

        self.btn_add = Button(master, text="Add to database", width=25, height=2, bg='steelblue', fg='white', command=self.get_items)
        self.btn_add.place(x=520, y=420)

        self.btn_clear = Button(master, text="Clear All Fields", width=18, height=2, bg='lightgreen', fg='white',
                                command=self.clear_all)
        self.btn_clear.place(x=350, y=420)

        """self.btn_to_update = Button(master, text="Update database" , width=18, height = 2, bg='steelblue', fg='white', command = self.path2)
        self.btn_to_update.place(x=420,y=480)

        self.btn_to_mainpage = Button(master, text="mainpage", width=18, height=2, bg='steelblue', fg='white',
                                    command=self.path3)
        self.btn_to_mainpage.place(x=420, y=480)"""
        #text box for logs

        self.tBox = Text(master, width=50, height=18)
        self.tBox.place(x=750, y=70)
        self.tBox.insert(END, "ID has reached upto: " + str(id))

    """def path2(self):
        from Update import root2

    def path3(self):
        from mainpage import root3"""

    def clear_all(self, *args, **kwargs):
        #num = id+1
        self.name_e.delete(0,END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vendor_e.delete(0, END)
        self.vendor_phone_e.delete(0, END)
        self.id_e.delete(0, END)






    def get_items(self,*args,**kwargs):

        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor = self.vendor_e.get()
        self.vendor_phone = self.vendor_phone_e.get()

        self.totalcp = float(self.cp) * float(self.stock)
        self.totalsp = float(self.sp) * float(self.stock)
        self.assumed_profit = float(self.totalsp - self.totalcp)

        if len(self.vendor_phone) !=10:
            tkinter.messagebox.showinfo("Error", "Please Enter Valid Number.")


        else:
            sql = "INSERT INTO inventory ( name, stock, cp , sp , totalcp , totalsp , assumed_profit , vendor , vendor_phone ) VALUES(?,?,?,?,?,?,?,?,?)"
            r = c.execute(sql, (self.name, self.stock, self.cp, self.sp , self.totalcp , self.totalsp , self.assumed_profit , self.vendor , self.vendor_phone))
            conn.commit()

            tkinter.messagebox.showinfo("Success","Successfully added to the database")

            self.tBox.insert(END, "\n\nInserted " + str(self.name) + " into the database with code " + str(self.id_e.get()))




root1 = Tk()
b=Database(root1)
root1.geometry("1366x768+0+0")
root1.title("Add to Database")
root1.mainloop()










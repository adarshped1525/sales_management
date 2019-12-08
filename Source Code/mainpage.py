from tkinter import *
import tkinter.messagebox
import datetime
import sqlite3
import os
import random

conn = sqlite3.connect("D:\database\store.db")
c = conn.cursor()

#For date purpose
date = datetime.datetime.now().date()

#for tracking record
product_list = []
product_price = []
product_quantity = []
product_id = []
labels_list = []


class Application:
    def __init__(self,master,*args,**kwargs):

        self.master=master
        #Frame
        self.left = Frame(master , width=700,height=768, bg='white')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=666, height=768, bg='lightblue')
        self.right.pack(side=RIGHT)

        #component
        self.heading = Label(self.left, text="TECHNOZILLA  Store", font=('arial 40 bold'), bg='white')
        self.heading.place(x=0, y=0)

        #date

        self.date_1= Label(self.right, text="Today's Date: "+str(date), font=('arial 16 bold'), bg='lightblue', fg='white')
        self.date_1.place(x=0, y=0)

        #table invoice================

        self.tproduct = Label(self.right, text="Products", font=('arial 18 bold') ,bg='lightblue', fg='white')
        self.tproduct.place(x=0, y=60)

        self.tquantity = Label(self.right, text="Quantity", font=('arial 18 bold'), bg='lightblue', fg='white')
        self.tquantity.place(x=300, y=60)

        self.tamount = Label(self.right, text="Amount", font=('arial 18 bold'), bg='lightblue', fg='white')
        self.tamount.place(x=500, y=60)


        #enter stuff

        self.enterid = Label(self.left, text="Enter Product's ID", font=('arial 18 bold'), bg='white')
        self.enterid.place(x=0, y=80)

        self.enteride= Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.enteride.place(x=220, y=80)

        self.enteride.focus()

        #button
        self.search_btn= Button(self.left, text="Search", width=22, height=2, bg='orange', command=self.ajax)
        self.search_btn.place(x=350, y=120)

        #fill it by the function ajax
        self.productname= Label(self.left, text="", font=('arial 27 bold'), bg='white', fg='Steelblue')
        self.productname.place(x=0, y=250)

        self.pprice = Label(self.left, text="", font=('arial 27 bold'), bg='white', fg='Steelblue')
        self.pprice.place(x=0, y=290)

        self.total_1= Label(self.right, text="", font=('arial 40 bold'), bg='lightblue', fg='white')
        self.total_1.place(x=0, y=640)

        self.master.bind("<Return>",self.ajax)
        self.master.bind("<Up>", self.add_to_cart)
        self.master.bind("<space>", self.generate_bill)


    def ajax(self, *args, **kwargs):

        self.get_id = self.enteride.get()
        #get the products info with that id and fill it in the labels above
        query = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(query, (self.get_id, ))
        for self.r in result:
            self.get_id = self.r[0]
            self.get_name = self.r[1]
            self.get_stock = self.r[2]
            self.get_price = self.r[4]

        self.productname.configure(text="Product's Name: " +str(self.get_name))
        self.pprice.configure(text="Price: RS. " + str(self.get_price))

        #for Qauntity
        self.quantity_1 = Label(self.left, text="Enter Quantity", font=('arial 18 bold'), bg='white')
        self.quantity_1.place(x=0, y=370)

        self.quantity_e= Entry(self.left, width = 25 , font=('arial 18 bold'), bg='lightblue')
        self.quantity_e.place(x=190, y=370)
        self.quantity_e.focus()

        #Discount
        self.discount_1 = Label(self.left, text="Enter Discount", font=('arial 18 bold'), bg='white')
        self.discount_1.place(x=0, y=410)

        self.discount_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.discount_e.place(x=190, y=410)
        self.discount_e.insert(END, 0)


        #Add to cart
        self.add_to_cart_btn = Button(self.left, text="Add To Cart", width=22, height=2, bg='orange', command=self.add_to_cart)
        self.add_to_cart_btn.place(x=350, y=450)

        #change
        self.change_1 = Label(self.left, text="Given Amount", font=('arial 18 bold'), bg='white')
        self.change_1.place(x=0, y=550)

        self.change_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.change_e.place(x=190, y=550)

        self.change_btn = Button(self.left, text="Calculate Change", width=22, height=2, bg='orange', command=self.change_func)
        self.change_btn.place(x=350, y=590)

        #Bill
        self.bill_btn = Button(self.left, text="Generate Bill", width=100, height=2, bg='Red' , fg='white', command=self.generate_bill)
        self.bill_btn.place(x=0, y=720)

    def add_to_cart(self, *args, **kwargs):

        self.quantity_value = int(self.quantity_e.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo("Error", "Not that many products in our inventory.")

        else:
            self.final_price = (float(self.quantity_value) * float(self.get_price)) - (float(self.discount_e.get()))
            product_list.append(self.get_name)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value)
            product_id.append(self.get_id)

            self.x_index = 0
            self.y_index = 100
            self.counter = 0
            for self.p in product_list:
                self.tempname = Label(self.right, text=str(product_list[self.counter]), font=('arial 18 bold'), bg='lightblue' , fg='white')
                self.tempname.place(x=0, y=self.y_index)
                labels_list.append(self.tempname)

                self.tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=('arial 18 bold'), bg='lightblue', fg='white')
                self.tempqt.place(x=300, y=self.y_index)
                labels_list.append(self.tempqt)

                self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=('arial 18 bold'), bg='lightblue', fg='white')
                self.tempprice.place(x=500, y=self.y_index)
                labels_list.append(self.tempprice)

                self.y_index += 40
                self.counter += 1

                #totalkeliye
                self.total_1.configure(text="Total: RS." + str(sum(product_price)))

                #delete entry after clicking add to cart

                self.quantity_1.place_forget()
                self.quantity_e.place_forget()
                self.discount_1.place_forget()
                self.discount_e.place_forget()
                self.productname.configure(text="")
                self.pprice.configure(text="")
                self.add_to_cart_btn.destroy()


                self.enteride.focus()
                self.enteride.delete(0, END)
    def change_func(self, *args, **kwargs):

        self.amount_given = float(self.change_e.get())
        self.our_total = float(sum(product_price))

        self.to_give = self.amount_given - self.our_total

        if self.to_give > 0:

            self.c_amount = Label(self.left, text="Change: RS. " + str(self.to_give), font=('arial 18 bold'), fg='red', bg='white')
            self.c_amount.place(x=0, y=600)

        else:
            tkinter.messagebox.showinfo("ERROR", "Given amount is less than total bill amount.")


    def generate_bill(self, *args, **kwargs):


        #original bill
        directory = "D:/invoice/" + str(date) + "/"
        if not os.path.exists(directory):
            os.makedirs(directory)

        company = "\t\t\t\tTechnozilla Pvt. Ltd.\n"
        address = "\t\t\t\t\tKharghar, Navi Mumbai\n"
        phone = "\t\t\t\t\t9999999999\n"
        sample = "\t\t\t\t\tInvoice\n"
        dt = "\t\t\t\t\t" + str(date)

        table_header = "\n\n\t\t\t-----------------------------------------------------\n\t\t\tSN.\tProducts\t\tQty\t\tAmount\n\t\t\t-----------------------------------------------------\n"
        final = company + address + phone + sample + dt + "\n" + table_header

        file_name = str(directory) + str(random.randrange(0, 5000)) + ".rtf"
        f = open(file_name, 'w')
        f.write(final)

        r = 1
        i = 0
        for t in product_list:
            f.write("\n\t\t\t" + str(r) + "\t" + str(product_list[i] + ".......")[:7] + "\t\t" + str(product_quantity[i]) + "\t\t" + str(product_price[i]))
            i += 1
            r += 1
        f.write("\n\n\t\t\tTotal: RS. " + str(sum(product_price)))
        f.write("\n\t\t\tThanks for Visiting.")
        os.startfile(file_name, "print")
        f.close()



        self.x = 0

        initial = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(initial, (product_id[self.x], ))

        for i in product_list:
            for r in result:
                self.old_stock = r[2]
            self.new_stock = int(self.old_stock) - int(product_quantity[self.x])

            sql = "UPDATE inventory SET stock=? WHERE id=?"
            c.execute(sql, (self.new_stock, product_id[self.x]))
            conn.commit()

            #transactions

            sql2 = "INSERT INTO transactions (product_name , quantity, amount, date) VALUES (?, ?, ?, ?)"
            c.execute(sql2, (product_list[self.x], product_quantity[self.x], product_price[self.x], date))
            conn.commit()

            self.x +=1

        for a in labels_list:
            a.destroy()

        del(product_list[:])
        del(product_id[:])
        del(product_quantity[:])
        del(product_price[:])

        self.total_1.configure(text="")
        self.c_amount.configure(text="")
        self.change_e.delete(0, END)
        self.enteride.focus()


        tkinter.messagebox.showinfo("Success","Done everything smoothly")


root3=Tk()
b=Application(root3)
root3.geometry("1366x768+0+0")
root3.mainloop()


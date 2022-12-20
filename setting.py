from cgi import test
from email import message
from email.mime import image
from select import select
from tkinter import *
from tkinter import ttk, messagebox, colorchooser
import sqlite3
from tkinter import filedialog
import os
import time
from PIL import Image, ImageTk
import create_db 

from numpy import insert



class settingClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry('550x500+255+140')
        self.root.config(bg="white")
        self.root.iconbitmap('images/icon.ico')
        # self.root.iconbitmap('images/icon.ico')
        self.root.focus_force()
        self.root.title("Inventory Management System | Developed By Shaheer")


        # =======  Variable

        self.var_address = StringVar()
        self.var_shop_name = StringVar()
        self.var_phone_number = StringVar()
        self.var_discount = StringVar()
        self.var_email = StringVar()
        self.var_website = StringVar()

    # ==============  Clock Label  ==============
        self.clock_label=Label(self.root, text="Welcome to SMART SHOP \t\t DD:MM:YY", font=("Montserrat", 13), bg="#245e5b", fg="white")
        self.clock_label.place(x=0, y=0, relwidth=1)

        # def update_date_time(self):
        time_ = time.strftime("%I:%M:%S")
        date_ = time.strftime("%d-%m-%Y")

        self.clock_label.config(text=f"Welcome to Smart Shop \t\t {time_}")
        self.clock_label.after(200, self.clock_label)

    # =================================     Settings Label Start    ==============================


    # Label
        shop_name = Label(self.root, text= "Your Shop Name",font=("Montserrat",12, "bold"), bg="white", fg="black")
        shop_name.place(x=20, y=50)

        shop_name_entry = Entry(self.root, bg="#ADDFFF", fg="black", textvariable=self.var_shop_name, relief=FLAT, font=("Montserrat",12, "bold"))
        shop_name_entry.place(x=175, y=50, width=250, height=28)

        phone_on_lbl = Label(self.root, text= "Phone Number",font=("Montserrat",12, "bold"), bg="white", fg="black")
        phone_on_lbl.place(x=20, y=115)

        phone_on_entry = Entry(self.root, bg="#ADDFFF", fg="black", textvariable = self.var_phone_number, relief=FLAT, font=("Montserrat",12, "bold"))
        phone_on_entry.place(x=175, y=115, width=250, height=28)

        address_lbl = Label(self.root, text="Your Address", font=("Montserrat", 12, "bold"), bg="white", fg="black")
        address_lbl.place(x=20, y=180)

        address_entry = Entry(self.root, bg="#ADDFFF", fg="black",textvariable = self.var_address , relief=FLAT, font=("Montserrat", 12, "bold"))
        address_entry.place(x=175, y=180, width=250, height=28)

        product_discount_lbl = Label(self.root, text="Discount", font=("Montserrat", 12, "bold"), bg="white", fg="black")
        product_discount_lbl.place(x=20, y=240)

        product_discount_entry = Entry(self.root, bg="#ADDFFF", textvariable = self.var_discount, fg="black", relief=FLAT, font=("Montserrat", 12, "bold"))
        product_discount_entry.place(x=175, y=240, width=250, height=28)

        email_lbl = Label(self.root, text="Email", font=("Montserrat", 12, "bold"), bg="white", fg="black")
        email_lbl.place(x=20, y=300)

        email_entry = Entry(self.root, bg="#ADDFFF", textvariable = self.var_email, fg="black", relief=FLAT, font=("Montserrat", 12, "bold"))
        email_entry.place(x=175, y=300, width=250, height=28)

        website_lbl = Label(self.root, text="Website", font=("Montserrat", 12, "bold"),  bg="white", fg="black")
        website_lbl.place(x=20, y=360)

        website_entry = Entry(self.root, bg="#ADDFFF", fg="black", textvariable = self.var_website, relief=FLAT, font=("Montserrat", 12, "bold"))
        website_entry.place(x=175, y=360, width=250, height=28)


        '''logo_lbl = Label(self.root, text= "Your Logo",font=("Montserrat",12, "bold"), bg="#212121", fg="black")
        logo_lbl.place(x=20, y=420)

        self.select_btn = PhotoImage(file="images/browse_btn.png")
        select_btn = Button(self.root, image=self.select_btn,bd=0, command=self.filedialogs, relief= FLAT, bg="#212121",activebackground="#212121")
        select_btn.place(x=175, y=420)'''






        self.save_btn = PhotoImage(file="images/save_btn.png")
        save_btn = Button(self.root, image=self.save_btn,bd=0, command=self.insert_data, relief= FLAT, bg="white",activebackground="white")
        save_btn.place(x=180, y=430)
# =======================================    Function are here    ==============================

    '''def filedialogs(self):
        # global self.get_image
        self.get_iamge = filedialog.askopenfile(title="Selece Logo", filetypes=(("png", "*.png"), ("jpg", "*.jpg")))


    def convert_image_into_bianiary(self, filename):
        with open (filename, 'rb') as file:
            photo_image = file.read()
        return photo_image

    def insert_images(self):
        con = sqlite3.connect(r"yms.db")
        cur = con.cursor()

        for image in self.get_iamge:
            insert_photo = self.convert_image_into_bianiary(image)
            cur.execute('INSERT INTO setting VALUE(:image)', 
                        {'image':insert_photo})

            con.commit()
            con.close()'''


    def insert_data(self):

        if self.var_shop_name.get() == "":
            messagebox.showerror("Error", "Shop name should be required!")

        else:

            '''con = sqlite3.connect(r"yms.db")
            cur = con.cursor()
            cur.execute("INSERT INTO setting (name, phone_no, address, discount, email, website ) VALUES (?,?,?,?,?,?)", (
                self.var_shop_name.get(),
                self.var_phone_number.get(),
                self.var_address.get(),
                self.var_discount.get(),
                self.var_email.get(),
                self.var_website.get(),
                
            ))
            con.commit()
            messagebox.showinfo("Success", "Your settings information saved successfully!")
            con.close()'''


            con = sqlite3.connect(r"ims.db")
            cur = con.cursor()
            cur.execute("Update setting set name=?, phone_no=?, address=?, discount=?, email=?, website=?",  (

                        self.var_shop_name.get(),
                        self.var_phone_number.get(),
                        self.var_address.get(),
                        self.var_discount.get(),
                        self.var_email.get(),
                        self.var_website.get(),
                    ))
            con.commit()
            messagebox.showinfo("Success", "Settings Updated Successfully", parent=self.root)




if __name__ == "__main__":
    root= Tk()
    obj = settingClass(root)
    root.mainloop()
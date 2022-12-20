from tkinter import *
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from setting import settingClass
import sqlite3
from tkinter import messagebox
import os
import time
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x720+0+0")
        self.root.iconbitmap('images/icon.ico')
        self.root.title("Inventory Management System | Developed By Shaheer")
        self.root.config(bg="white")
        #===title=====
        con = sqlite3.connect(database =r"ims.db")
        cur = con.cursor()
        try:

            cur.execute("SELECT name FROM setting ")
            rows = cur.fetchall()
            for row in rows:
                name = row[0]

            self.icon_title=PhotoImage(file="images/logo1.png")
            title=Label(self.root,text=f"{name}",image=self.icon_title,compound=LEFT,font=("times new roman",30,"bold"),bg="#010c48",fg="white",anchor="w",padx=20)
            title.place(x=0,y=0,relwidth=1,height=70)

            con.commit()
            cur.close()

        except Exception as es:
            messagebox.showerror("Error", f"Your error due to {es}")

        #===btn_logout===
        btn_logout=Button(self.root,text="logout",command=self.logout,font=("times new roman",15,"bold"),bg="#00BFFF",cursor="hand2", activebackground="yellow", activeforeground="darkblue")
        btn_logout.place(x=1050,y=12,height=40,width=150)
        
        #======= settings =======
        self.setting_btn = PhotoImage(file="images/setting_icon.png")
        setting_btn=Button(self.root, image=self.setting_btn,command=self.settings, bg="#010c48", bd=0, cursor="hand2", activebackground="#1D2142")
        setting_btn.place(x=1250, y=15)
        
        
        #===clock====
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15,),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #====left Menu==
        self.Menulogo=Image.open("images/menu_im.png")
        self.Menulogo=self.Menulogo.resize((200,200),Image.ANTIALIAS)
        self.Menulogo=ImageTk.PhotoImage(self.Menulogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
        
        lbl_menulogo=Label(LeftMenu,image=self.Menulogo)
        lbl_menulogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/side.png")
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)

        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",command=self.logout,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        #====content==========

        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)
     
        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)
        
        self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)


        #===footer====
        con = sqlite3.connect(database =r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name, phone_no, address, email, website FROM setting ")
            rows = cur.fetchall()
            for row in rows:
                name = row[0]
                '''phone_no = row[1]
                address = row[2]
                email = row[3]
                website = row[4]'''

            footer = Label(self.root, text=f"{name}  |  Developed by Shaheer \n website: www.shahreer.com      |     email: shahreer@gmail.com      |      Contact: 0172****15 / 0199*****9", font=("Montserrat", 9), bg="#245e5b", fg="white")
            footer.pack(side=BOTTOM, fill=X)
            con.commit()

        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to:  {str(ex)}", parent=self.root)

        self.update_content()

        # lbl_clock=Label(self.root,text="IMS-Inventory Management System | Developed by Shaheer\nfor any Technical Issue Contact:0340xxxx58",font=("times new roman",12,),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        # self.update_content()
#==========================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
    
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)      
    
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)      
    
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)  
    
    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total products\n[ {str(len(product))} ]')
            
            cur.execute("Select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Supplier\n[ {str(len(supplier))} ]')
            
            cur.execute("Select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total category\n[ {str(len(category))} ]')
            
            cur.execute("Select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employee\n[ {str(len(employee))}]')
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n[{str(bill)}]')


     # Update date and time visualization with database
            
            cur.execute("SELECT name FROM setting ")
            rows = cur.fetchall()
            for row in rows:
                name = row[0]

            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")

            self.lbl_clock.config(text=f"Welcome to {name} \t\t\t\t {str(time_)} \t\t\t\t {str(date_)}")
            self.lbl_clock.after(200, self.update_content)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 
    
    def logout(self):
        self.root.destroy()
        os.system("python login.py")

    def settings(self):
        self.new_win= Toplevel(self.root)
        self.new_obj = settingClass(self.new_win)


if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()
    
from cgitb import text
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import time
import os
import tempfile

class billClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x800+0+0")
        self.root.title("Inventory Management System | Developed By Shaheer")
        self.root.config(bg="white")
        self.root.iconbitmap('images/icon.ico')
        self.cart_list=[]
        self.chk_print=0
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
        btn_logout.place(x=1200,y=12,height=40,width=150)
        #===clock====
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15,),bg="#245e5b", fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #==============product frame==========================
        self.var_search=StringVar()

    
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=635)
 
     

        pTitle=Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        
        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(ProductFrame2,text="Search Product | By Product ID ",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)

        lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=128,y=47,width=150,height=22)
        self.btn_search=Button(ProductFrame2,text="Search", command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2")
        self.btn_search.place(x=285,y=45,width=100,height=25)
        btn_show_all=Button(ProductFrame2,text="Show All",command=self.show,font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)
       

        cart_Frame=Frame(ProductFrame1,bd=3,relief=RIDGE)
        cart_Frame.place(x=2,y=140,width=398,height=450)
        
        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)

#=================frame================================================================

        self.product_Table=ttk.Treeview(cart_Frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)


        self.product_Table.heading("pid",text="PID")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="QTY")
        self.product_Table.heading("status",text="Status")
        self.product_Table["show"]="headings"
        self.product_Table.column("pid",width=40)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=40)
        self.product_Table.column("status",width=90)
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(ProductFrame1,text="Note:'Enter 0 Quantity to remove from the Cart'",font=("goudy old style",14),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)

        #===============Customer frame=======================
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=100)

        cTitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgrey").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_search=Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=180)
        
        lbl_contact=Label(CustomerFrame,text="Contact No.",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=380,y=35,width=140)
        
        #============CAL CART FRAME================
        Cal_Cart_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=554)
        
        #============CALCULATOR FRAME===========================
        self.var_cal_input=StringVar()

        Cal_Frame=Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)
        

        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)
        
        btn_7=Button(Cal_Frame,text='7',font=('arial',15,'bold'),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text='8',font=('arial',15,'bold'),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text='9',font=('arial',15,'bold'),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text='+',font=('arial',15,'bold'),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)
        
         
        btn_4=Button(Cal_Frame,text='4',font=('arial',15,'bold'),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text='5',font=('arial',15,'bold'),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text='6',font=('arial',15,'bold'),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text='-',font=('arial',15,'bold'),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)
        
         
        btn_1=Button(Cal_Frame,text='1',font=('arial',15,'bold'),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text='2',font=('arial',15,'bold'),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text='3',font=('arial',15,'bold'),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text='*',font=('arial',15,'bold'),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)
        
         
        btn_0=Button(Cal_Frame,text='0',font=('arial',15,'bold'),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text='c',font=('arial',15,'bold'),command=self.clear_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text='=',font=('arial',15,'bold'),command=self.perform_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text='/',font=('arial',15,'bold'),command=lambda:self.get_input('/'),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=3)
#=================Cart frame================================================================
        
        cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        cart_Frame.place(x=280,y=8,width=245,height=342)        
        self.cartTitle=Label(cart_Frame,text="Cart \t Total Product: [0]",font=("goudy old style",15),bg="lightgrey")
        self.cartTitle.pack(side=TOP,fill=X)

        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)


        self.CartTable=ttk.Treeview(cart_Frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)


        self.CartTable.heading("pid",text="PID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="QTY")
        
        self.CartTable["show"]="headings"
        self.CartTable.column("pid",width=40)
        self.CartTable.column("name",width=90)
        self.CartTable.column("price",width=90)
        self.CartTable.column("qty",width=40)
        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)    
        
        #===================ADD CART WIDGET FRAME====================== 
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()

        Add_Cart_Widget_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_Cart_Widget_Frame.place(x=420,y=550,width=530,height=190)
        
        lbl_p_name=Label(Add_Cart_Widget_Frame,text="Product Name",font=("times new roman",17),bg="white").place(x=20,y=5)
        txt_p_name=Entry(Add_Cart_Widget_Frame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=45,width=190,height=25)
        
        lbl_p_price=Label(Add_Cart_Widget_Frame,text="Price Per Qty",font=("times new roman",17),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_Cart_Widget_Frame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=45,width=150,height=25)
        
        lbl_p_qty=Label(Add_Cart_Widget_Frame,text="Quantity",font=("times new roman",17),bg="white").place(x=400,y=5)
        txt_p_qty=Entry(Add_Cart_Widget_Frame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=395,y=45,width=120,height=25)
         
        self.lbl_inStock=Label(Add_Cart_Widget_Frame,text="In Stock",font=("times new roman",18),bg="white")
        self.lbl_inStock.place(x=8,y=105) 

        btn_clear_cart=Button(Add_Cart_Widget_Frame,text="Clear",command=self.clear_cart,font=("times new roman",15,"bold"),bg="lightgrey",cursor="hand2").place(x=180,y=100,width=150,height=45)
        btn_add_cart=Button(Add_Cart_Widget_Frame,text="Add | Update Cart",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=100,width=180,height=45)
        
        #========================BILLING AREA ===================================
        billFrame=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        billFrame.place(x=980,y=110,width=390,height=635)
        
        BTitle=Label(billFrame,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="#f44336",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        #===================BILLING BUTTONS====================
        billMenuFrame=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        billMenuFrame.place(x=953,y=520,width=570,height=225)

        self.lbl_amnt=Label(billMenuFrame,text='Bill Amount\n[0]',font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=5,y=5,width=150,height=120)
        
    #   ================  Discount % fetch from database  ===================
        con = sqlite3.connect(database =r"ims.db")
        cur = con.cursor()
        try:

            cur.execute("SELECT discount FROM setting ")
            rows = cur.fetchall()
            for row in rows:
                discount = row[0]
            self.lbl_discount=Label(billMenuFrame,text=f'Discount \n[{discount}]',font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white")
            self.lbl_discount.place(x=155,y=5,width=150,height=120)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 

        
        self.lbl_net_pay=Label(billMenuFrame,text='Net pay\n[0]',font=("goudy old style",15,"bold"),bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=305,y=5,width=150,height=120)

        btn_print=Button(billMenuFrame,text='Print',command=self.print_bill,cursor="hand2",font=("goudy old style",15,"bold"),bg="red",fg="white", relief=FLAT)
        btn_print.place(x=5,y=135,width=110,height=50)
        
        btn_clear_all=Button(billMenuFrame,text='Clear All',command=self.clear_all,cursor="hand2",font=("goudy old style",15,"bold"),bg="purple",fg="white", relief=FLAT)
        btn_clear_all.place(x=122,y=135,width=110,height=50)
        
        btn_generate=Button(billMenuFrame,text='Generate Bill/Save Bill',command=self.generate_bill,cursor="hand2",font=("goudy old style",15,"bold"),bg="#009688",fg="white", relief=FLAT)
        btn_generate.place(x=240,y=135,width=200,height=50)

        logo_btn = Button(billMenuFrame, text="Logo Place", command=self.logo_import)
        logo_btn.place(x=15,y=190,width=400,height=20)




#=========================  footer  ===================================

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

            footer = Label(self.root, text=f"{name}  |  Developed by Shaheer \n website : www.shahreer.com     |     email : shahreer@gmail.com      |     Contact : 0172****15 / 0199*****9", font=("Montserrat", 9), bg="#245e5b", fg="white")
            footer.pack(side=BOTTOM, fill=X)

            con.commit()

        except Exception as ex:
            messagebox.showerror("Error", f"Your error due to:  {str(ex)}", parent=self.root)


        
        self.show()
        #self.bill_top()
        self.update_date_time()
# ================================ALL FUNCTION====================================

    def logo_import(self):
        # Add image in text box
        global my_logo

        logo_image = Image.open(f"images/logo.png", 'r')
        resize_image = logo_image.resize((40, 40))
        self.logo = ImageTk.PhotoImage(resize_image)
        position = self.txt_bill_area.index(INSERT)
        self.txt_bill_area.image_create(position, image=self.logo)
        logo_label.config(image=self.logo, text=position)


        # label for logo position
        logo_label = Label(self.root, text="")
        logo_label.pack()
            
    def get_input(self,num):
            xnum=self.var_cal_input.get()+str(num)
            self.var_cal_input.set(xnum)
    def clear_cal(self):
            self.var_cal_input.set('')
   
    def perform_cal(self):
            result=self.var_cal_input.get()
            self.var_cal_input.set(eval(result))            


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:    
            cur.execute("select pid,name,price,qty,status from product where status='Active'")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search Input is required",parent=self.root) 
            else:
                cur.execute("select pid,name,price,qty,status from product where pid LIKE '%"+self.var_search.get()+"%' and status='Active'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)
                    # self.add_update_cart()
                    

                    self.var_pid.set(row[0])
                    self.var_qty.set('1')
                    self.var_pname.set(row[1])            
                    self.var_price.set(row[2])
                    self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
                    self.var_stock.set(row[3])

                    f=self.product_Table.focus()
                    content=(self.product_Table.item(f))
                    row=content['values']

                    f=self.CartTable.focus()
                    content=(self.CartTable.item(f))
                    row=content['values']

                    self.add_update_cart()

                    
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
                
                

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 
    
    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])            
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')
    
    def get_data_cart(self,ev):
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])            
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_inStock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
        
        
    def add_update_cart(self):
        
        if self.var_qty.get()=='':
            messagebox.showerror('Error',"Quantity is Required",parent=self.root)
        
        if int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror('Error',"Invalid Quantity",parent=self.root)    
        else:            
            #price_cal=(int(self.var_qty.get())*float(self.var_price.get()))   
            #price_cal=float(price_cal)
            price_cal = self.var_price.get()
           
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]        
            
            #=====UPDATE CART===============================================================
            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            if present=='yes':
                op=messagebox.askyesno('Confirm',"Product already present \nDo you want to update| Remove from the Cart list",parent=self.root) 
                if op ==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        #self.cart_list[index_][2]=price_cal #price
                        self.cart_list[index_][3]=self.var_qty.get()
            else:                
                self.cart_list.append(cart_data) 
            self.show_cart()
            self.bill_updates()

    def bill_updates(self):
        con = sqlite3.connect(database =r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT discount FROM setting ")
            rows = cur.fetchall()
            for row in rows:
                discount = row[0]
    
            self.bill_amnt=0
            self.net_pay=0
            self.discount=0

            for row in self.cart_list:
                self.bill_amnt=self.bill_amnt + (float(row[2])*int(row[3]))

            self.discount=(self.bill_amnt*int(discount))/100
            self.net_pay=self.bill_amnt-self.discount

            self.lbl_amnt.config(text=f'Bill Amount\n{str(self.bill_amnt)}')
            self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
            self.lbl_discount.config(text=f"Discount\n{str(self.discount)}")
            self.cartTitle.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")

        except Exception as es:
            messagebox.showerror("Error", f"Your error due to {es}")



    def show_cart(self):
        try:    
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error",f"Customer Details are required",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error",f"Please Add product to cart!!!",parent=self.root)
        else:
            #===Bill Top===
            self.bill_top()
            #===Bill Middle===
            self.bill_middle()
            #===Bill Bottom===
            self.bill_bottom()

            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo('Saved',"Bill has been generated/Save in Backend",parent=self.root)            
            self.chk_print=1

        


    def bill_top(self):

        con = sqlite3.connect(database =r"ims.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name, phone_no, address, email, website FROM setting ")
            rows = cur.fetchall()
            for row in rows:
                name = row[0]
                phone_no = row[1]
                address = row[2]
                email = row[3]
                website = row[4]


            self.invoice = int(time.strftime('%H%M%S'))+int(time.strftime("%d%m%y"))
            bill_top_temp=f'''
\t\t{name}
    Phone No. {phone_no} , {address}
        email: {email} 
        website: {website}\n
{str("="*45)}
 Customer Name: {self.var_cname.get()}
 Ph no. :{self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*45)}
 Product Name\t\t\tQTY\tmrp
{str("="*45)}
        '''
            self.txt_bill_area.delete('1.0',END)
            self.txt_bill_area.insert('1.0',bill_top_temp)

        except Exception as es:
            messagebox.showerror("Error", f"Your error due to {str(es)}")
        


    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*45)}
 Bill Amount\t\t\t\tRs.{self.bill_amnt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*45)}\n
\t\t\tTHANKS FOR COMING         
{str("="*45)}\n
\t\tSoftware Developed By Shaheer
{str("="*45)}\n

        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)


    def bill_middle(self):
     con=sqlite3.connect(database=r'ims.db')
     cur=con.cursor()

     try:  
        for row in self.cart_list:
            
        
            pid=row[0]
            name=row[1]
            qty=int(row[4])-int(row[3])
            if int(row[3])==int(row[4]):
                status='Inactive'
            if int(row[3])!=int(row[4]):
                status='Active'    

            price=float(row[2])*int(row[3])
            price=str(price)
            self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tRs."+price)
            #======update qty in the product table================
            cur.execute('update product set qty=?,status=? where pid=?',(
                qty,
                status,
                pid
            ))
            con.commit()
        con.close()
        self.show()
     except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    
    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')            
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_inStock.config(text=f"In Stock")
        self.var_stock.set('')
        
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.chk_print=0
        self.txt_bill_area.delete('1.0',END)
        self.cartTitle.config(text=f"Cart \t Total Product: [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
    def update_date_time(self):
        # Update date and time visualization with database
        con = sqlite3.connect(database =r"ims.db")
        cur = con.cursor()
        try:
                
            cur.execute("SELECT name FROM setting ")
            rows = cur.fetchall()
            for row in rows:
                name = row[0]

            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")

            self.lbl_clock.config(text=f"Welcome to {name} \t\t\t\t {str(time_)} \t\t\t\t {str(date_)}")
            self.lbl_clock.after(200, self.update_date_time)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 
    
    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('Print',"Please wait while printing",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')

        else:
            messagebox.showerror('Print',"Please generate bill, to print the receipt",parent=self.root)
    
    def logout(self):
        self.root.destroy()
        os.system("python login.py")        

if __name__=="__main__":
    root=Tk()
    obj=billClass(root)
    root.mainloop()
    
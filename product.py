from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import qrcode
from barcode import EAN13
# import barcode
class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed By Shaheer")
        self.root.config(bg="white")
        self.root.iconbitmap('images/icon.ico')
        self.root.focus_force()
        #====Variables====
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()

        
        #==================================================================

        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)

        #=============title====================

        title=Label(product_Frame,text="Manage Products Details",font=("goudy old style",18),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
   
        #======column1============
        lbl_pid = Label(product_Frame,text="Product ID",font=("goudy old style",18),bg="white").place(x=30,y=60)
        lbl_category=Label(product_Frame,text="Category",font=("goudy old style",18),bg="white").place(x=30,y=110)
        lbl_supplier=Label(product_Frame,text="Supplier",font=("goudy old style",18),bg="white").place(x=30,y=160)
        lbl_name=Label(product_Frame,text="Name",font=("goudy old style",18),bg="white").place(x=30,y=210)
        lbl_price=Label(product_Frame,text="Price",font=("goudy old style",18),bg="white").place(x=30,y=260)
        lbl_qty=Label(product_Frame,text="Quantity",font=("goudy old style",18),bg="white").place(x=30,y=310)
        lbl_status=Label(product_Frame,text="Status",font=("goudy old style",18),bg="white").place(x=30,y=360)
        
       
                   
        #======column2============
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=150,y=110,width=200)
        cmb_cat.current(0)
        

        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_sup.place(x=150,y=160,width=200)
        cmb_sup.current(0)


        txt_pid=Entry(product_Frame,textvariable=self.var_pid,font=("goudy old style",15),bg="lightyellow").place(x=150,y=60,width=200)        
        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=210,width=200)
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow").place(x=150,y=260,width=200)
        txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=("goudy old style",15),bg="lightyellow").place(x=150,y=310,width=200)
        
        
        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=150,y=360,width=200)
        cmb_status.current(0)

        #==========button============
        btn_add=Button(product_Frame,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)           
        btn_update=Button(product_Frame,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)           
        btn_delete=Button(product_Frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)           
        btn_clear=Button(product_Frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)           

        #=====searchframe========
        searchframe=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        searchframe.place(x=480,y=10,width=600,height=80)
                   
        #======option============
        cmb_search=ttk.Combobox(searchframe,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("goudy old style",14))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(searchframe,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)           
        btn_search=Button(searchframe,text="search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=8,width=150,height=30)           

                   
        
       
       
        #====Product Details====
        pro_frame=Frame(self.root,bd=3,relief=RIDGE)
        pro_frame.place(x=480,y=100,width=600,height=200)

        scrolly=Scrollbar(pro_frame,orient=VERTICAL)
        scrollx=Scrollbar(pro_frame,orient=HORIZONTAL)
        
        
        self.productTable=ttk.Treeview(pro_frame,columns=("pid","Supplier","Category","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)



        self.productTable.heading("pid",text="P ID")
        self.productTable.heading("Category",text="Category")
        self.productTable.heading("Supplier",text="Supplier")
        self.productTable.heading("name",text="Name") 
        self.productTable.heading("price",text="Price")
        self.productTable.heading("qty",text="Qty")
        self.productTable.heading("status",text="Status")

        self.productTable["show"]="headings"
        
        self.productTable.column("pid",width=40)
        self.productTable.column("Category",width=75)
        self.productTable.column("Supplier",width=80)
        self.productTable.column("name",width=100)
        self.productTable.column("price",width=60)
        self.productTable.column("qty",width=50)
        self.productTable.column("status",width=50)
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()


#====================    QR CODE AND BAR CODE GENERATOR   ============================

    
        # Qr code and Barcode Frame
        self.qr_bar_frame=Frame(self.root, bg="white",relief=RIDGE ,bd=3)
        self.qr_bar_frame.place(x=480, y=310, width=600, height=175)
        
        # Qr code Label
        self.qr_code_lbl = Label(self.qr_bar_frame,text="No QR\nAvailable",  font=("Montserrat", 12), bg="#CFECEC", fg="#123456",)
        self.qr_code_lbl.place(x=20, y=10, width=150, height=150)

        # Barcode
        self.bar_code_lbl = Label(self.qr_bar_frame,text="No Barcode\nAvailable",  font=("Montserrat", 12), bg="#CFECEC", fg="#123456",)
        self.bar_code_lbl.place(x=220, y=65, width=163, height=90)

    #======= Buttton here=======
        self.qr_generate = Button(self.qr_bar_frame, text="QR BAR Code Generate",command=self.generate, font=("Montserrat", 10), bg="#550A35", fg="white")
        self.qr_generate.place(x=220, y=10, width=300, height=50)






        
#================================================================================================
#=====================================           Function           =============================
    # ================================      BAR CODE GENERATOR      =============================

    def generate(self):
        
        if self.var_cat.get()=='' or self.var_cat.get()=='' or self.var_sup.get()=='' or self.var_name.get()=='' or self.var_price.get()=='' or self.var_qty.get()=='' or self.var_status.get()=='':
            messagebox.showerror("Error", "All fields should be required")

        else:
            
        # create qr code
            qr_data = (f"Catagory : {self.var_cat.get()}\nSupplier : {self.var_sup.get()}\nName : {self.var_name.get()}\nPrice : {self.var_price.get()}\nQTY : {self.var_qty.get()}\nStatus : {self.var_status.get()}")
            qr_code = qrcode.make(qr_data)
            print(qr_code)
            qr_code.save(f"bar_qr/qr_code/qr_"+str(self.var_pid.get())+'.png')

        # QR code image config
            image = Image.open(f"bar_qr/qr_code/qr_"+str(self.var_pid.get())+'.png', 'r')
            resize_image = image.resize((180, 180))
            self.im = ImageTk.PhotoImage(resize_image)
            self.qr_code_lbl.config(image=self.im)

            # =================== Barcode  =================

            #setup self.bar_code_lbl
            number = self.var_pid.get()
            my_barcode = EAN13(number)

            #save
            my_barcode.save(f"bar_qr/bar_code/bar_"+str(self.var_pid.get()))

            # config Barcode Label
            self.bar_code_lbl.config(text=f"Saved!")

            messagebox.showinfo("Success", "Your Product details QR Code and Barcode generated successful!")




    
    
    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:     
            cur.execute("Select name from category")
            cat=cur.fetchall()   
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")                
                for i in cat:
                    self.cat_list.append(i[0])
                            
            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
               del self.sup_list[:]
               self.sup_list.append("Select")                
               for i in sup:
                  self.sup_list.append(i[0])       
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_sup.get()=="Empty" or self.var_name.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product already present, try different",parent=self.root)
                else:
                    if int(self.var_qty.get())<=0:
                        self.var_status.set("Inactive")
                    cur.execute("Insert into product (pid,Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?,?)",(
                            self.var_pid.get(),
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                        ))

                    con.commit()
                    messagebox.showinfo("Sucess","Product Added Sucessfully")
                   
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_cat.set(row[2])
        self.var_sup.set(row[1])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])   
        
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Select Product form list",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    cur.execute("Update product set Category=?, Supplier=?, name=?, price=?, qty=?, status=? where pid=?",(
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                            self.var_pid.get(),
                            
                        ))

                    con.commit()
                    messagebox.showinfo("Success","Product Updated Sucessfully")
                    self.root.focus_force()
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Select Product from the list",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Sucess","Product Deleted Sucessfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_name.set("")
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_pid.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search by Option",parent=self.root) 
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Select Input is required",parent=self.root) 

            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root) 

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 


if __name__=="__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop()
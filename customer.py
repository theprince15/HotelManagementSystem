from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Customer_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+50+90")


    #=====================================variables=====================================================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


        self.var_cust_name=StringVar()
        self.var_mother = StringVar()
        self.var_father = StringVar()
        self.var_gender = StringVar()
        self.var_pin = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_idproof = StringVar()
        self.var_idnumber = StringVar()

   #========================================title======================================================
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

   #     ============================logo====================================
        img2 = Image.open("images\logo.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)


        label=Label(self.root,image=self.photoimage2,bd=0,relief=RIDGE)
        label.place(x=5,y=2,width=100,height=40)

    #===================================Label Frame=======================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman", 12, "bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

    #===================================labels and enteries====================================
        #custRef
        lbl_cust_ref= Label(labelframeleft,text="Customer Ref",font=("arial", 12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial", 13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        # cust name
        cname = Label(labelframeleft, text="Customer Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)

        textcname = ttk.Entry(labelframeleft,textvariable=self.var_cust_name, width=29, font=("arial", 13, "bold"))
        textcname.grid(row=1, column=1)

        #mother name
        lblmname = Label(labelframeleft, text="Mother Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)

        textmname = ttk.Entry(labelframeleft,textvariable=self.var_mother, width=29, font=("arial", 13, "bold"))
        textmname.grid(row=2, column=1)

        #father name
        lblfname = Label(labelframeleft, text="Father Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblfname.grid(row=3, column=0, sticky=W)

        textfname = ttk.Entry(labelframeleft,textvariable=self.var_father, width=29, font=("arial", 13, "bold"))
        textfname.grid(row=3, column=1)

        #gender combobox
        lbl_gender = Label(labelframeleft, text="Gender:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=4, column=0, sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,width=27, font=("arial", 12, "bold"),state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=4,column=1)

        #pincode
        lblPinCode = Label(labelframeleft, text="PinCode:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPinCode.grid(row=5, column=0, sticky=W)

        textPinCode = ttk.Entry(labelframeleft,textvariable=self.var_pin,width=29, font=("arial", 13, "bold"))
        textPinCode.grid(row=5, column=1)

        #mobilenumber
        lblMobile = Label(labelframeleft, text="Mobile:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=6, column=0, sticky=W)

        textMobile = ttk.Entry(labelframeleft,textvariable=self.var_mobile, width=29, font=("arial", 13, "bold"))
        textMobile.grid(row=6, column=1)

        #email
        lblEmail = Label(labelframeleft, text="Email:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblEmail.grid(row=7, column=0, sticky=W)

        textEmail = ttk.Entry(labelframeleft,textvariable=self.var_email, width=29, font=("arial", 13, "bold"))
        textEmail.grid(row=7, column=1)

        #nationality
        lblNationality = Label(labelframeleft, text="Nationality:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNationality.grid(row=8, column=0, sticky=W)

        combo_Natioanality= ttk.Combobox(labelframeleft,textvariable=self.var_nationality, width=27, font=("arial", 12, "bold"), state="readonly")
        combo_Natioanality["value"] = ("Indian", "American", "British","Other")
        combo_Natioanality.current(0)
        combo_Natioanality.grid(row=8, column=1)

        #id prooftype combobox

        lblIdProof = Label(labelframeleft, text="Id Proof Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdProof.grid(row=9, column=0, sticky=W)

        combo_id = ttk.Combobox(labelframeleft,textvariable=self.var_idproof, width=27, font=("arial", 12, "bold"), state="readonly")
        combo_id["value"] = ("Aadhar Card", "Driving License", "Passport")
        combo_id.current(0)
        combo_id.grid(row=9, column=1)


        #id number
        lblIdNumber = Label(labelframeleft, text="Id Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=10, column=0, sticky=W)

        textIdNumber = ttk.Entry(labelframeleft,textvariable=self.var_idnumber, width=29, font=("arial", 13, "bold"))
        textIdNumber.grid(row=10, column=1)

        # address
        lblAddress = Label(labelframeleft, text="Address:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAddress.grid(row=11, column=0, sticky=W)

        textAddress = ttk.Entry(labelframeleft,textvariable=self.var_address, width=29, font=("arial", 13, "bold"))
        textAddress.grid(row=11, column=1)

    #=====================================buttons======================================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=420,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

    #====================================Table Frame Search System===============================================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",font=("arai", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(Table_Frame, text="Search By:", font=("arial", 12, "bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W)

        self.search_var=StringVar()
        combo_Search = ttk.Combobox(Table_Frame,textvariable=self.search_var, width=24, font=("arial", 12, "bold"), state="readonly")
        combo_Search["value"] = ("Mobile", "Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1,padx=2)

        self.txt_search=StringVar()
        textSearch = ttk.Entry(Table_Frame,textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
        textSearch.grid(row=0, column=2,padx=2)

        btnSearch = Button(Table_Frame, text="Search",command=self.search, width=10,font=("arial", 11, "bold"), bg="black",fg="gold")
        btnSearch.grid(row=0, column=3 , padx=2)

        btnShowAll = Button(Table_Frame , text="Show All",command=self.fetch_data, width=10,font=("arial", 11, "bold"), bg="black",fg="gold")
        btnShowAll.grid(row=0, column=4, padx=2)

        #=============================================Show DataTable=====================================================
        Details_Table = Frame(Table_Frame, bd=2, relief=RIDGE)
        Details_Table.place(x=0, y=50, width=860, height=350)

        scroll_x=ttk.Scrollbar(Details_Table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Details_Table, orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(Details_Table,column=("ref","name","father","mother","gender","pin","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("mother", text="Mother Name")
        self.Cust_Details_Table.heading("father", text="Father Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("pin", text="PINCode")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idproof", text="Id Proof")
        self.Cust_Details_Table.heading("idnumber", text="Id Number")
        self.Cust_Details_Table.heading("address", text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("mother", width=100)
        self.Cust_Details_Table.column("father", width=100)
        self.Cust_Details_Table.column("mother", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("pin", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idproof", width=100)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("address", width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
            messagebox.showerror("Error", "All fields are mandatory", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.var_ref.get(),
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_father.get(),
                self.var_gender.get(),
                self.var_pin.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_idproof.get(),
                self.var_idnumber.get(),
                self.var_address.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_father.set(row[3])
        self.var_gender.set(row[4])
        self.var_pin.set(row[5])
        self.var_mobile.set(row[6])
        self.var_email.set(row[7]),
        self.var_nationality.set(row[8]),
        self.var_idproof.set(row[9]),
        self.var_idnumber.set(row[10]),
        self.var_address.set(row[11])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("update customer set Name=%s,Mother=%s,Father=%s,Gender=%s,PinCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                                                                                                                                                                   self.var_cust_name.get(),
                                                                                                                                                                                   self.var_mother.get(),
                                                                                                                                                                                   self.var_father.get(),
                                                                                                                                                                                   self.var_gender.get(),
                                                                                                                                                                                   self.var_pin.get(),
                                                                                                                                                                                   self.var_mobile.get(),
                                                                                                                                                                                   self.var_email.get(),
                                                                                                                                                                                   self.var_nationality.get(),
                                                                                                                                                                                   self.var_idproof.get(),
                                                                                                                                                                                   self.var_idnumber.get(),
                                                                                                                                                                                   self.var_address.get(),
                                                                                                                                                                                   self.var_ref.get()
                                                                                                                                                                                                      ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Customer details have been updated sucessfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer?",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
            my_cursor = conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        self.var_father.set(""),
        #self.var_gender.set(""),
        self.var_pin.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_idproof.set(""),
        self.var_idnumber.set(""),
        self.var_address.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+ "%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()










if __name__=="__main__":
        root=Tk()
        obj=Customer_Window(root)
        root.mainloop()

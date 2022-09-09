from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from datetime import datetime
from time import strftime


class ReportDetails:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+50+90")

#============================================================variables=============================================================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_chekout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomsavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
#========================================title======================================================
        lbl_title = Label(self.root, text="REPORT OF BOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

   #     ============================logo====================================
        img2 = Image.open("images/logo.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)


        label=Label(self.root,image=self.photoimage2,bd=0,relief=RIDGE)
        label.place(x=5,y=2,width=100,height=40)

#===================================Label Frame=======================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("times new roman", 12, "bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

#===================================labels and enteries====================================
        #Customer Contact
        lbl_cust_contact= Label(labelframeleft,text="Customer Contact",font=("arial", 12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial", 13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        #fetchdatabutton
        btnFetchData = Button(labelframeleft,command=self.fetch_contact, text="Fetch Data", font=("arial", 8, "bold"), bg="black", fg="gold",width=8)
        btnFetchData.place(x=347, y=4)

        #CheckInDate
        check_in_date = Label(labelframeleft, text="Check In Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        textcheck_in_date = ttk.Entry(labelframeleft,textvariable=self.var_checkin, width=29, font=("arial", 13, "bold"))
        textcheck_in_date.grid(row=1, column=1)

        #CheckOutDate
        lbl_check_out_date = Label(labelframeleft, text="Check Out Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_check_out_date.grid(row=2, column=0, sticky=W)

        textcheck_out_date = ttk.Entry(labelframeleft,textvariable=self.var_chekout, width=29, font=("arial", 13, "bold"))
        textcheck_out_date.grid(row=2, column=1)

        #RoomType
        lblRoom_Type = Label(labelframeleft, text="Room Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblRoom_Type.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        id = my_cursor.fetchall()

        comboRoom_Type = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, width=27, font=("arial", 12, "bold"),state="readonly")
        comboRoom_Type["value"] = id
        comboRoom_Type.current(0)
        comboRoom_Type.grid(row=3, column=1)

        #AvailableRoom
        lblRoomAvailable = Label(labelframeleft, text="Available Room:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)

       # textRoomAvailable= ttk.Entry(labelframeleft,textvariable=self.var_roomsavailable, width=29, font=("arial", 13, "bold"))
        #textRoomAvailable.grid(row=4, column=1)

        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select Room_No from details")
        rows= my_cursor.fetchall()

        comboRoom_No = ttk.Combobox(labelframeleft, textvariable=self.var_roomsavailable, width=27,font=("arial", 12, "bold"), state="readonly")
        comboRoom_No["value"] = rows
        comboRoom_No.current(0)
        comboRoom_No.grid(row=4, column=1)

        #Meal
        lblMeal = Label(labelframeleft, text="Meal:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)

        textMeal = ttk.Entry(labelframeleft,textvariable=self.var_meal,width=29, font=("arial", 13, "bold"))
        textMeal.grid(row=5, column=1)

        #NoOfDays
        lblNoOfDays = Label(labelframeleft, text="No Of Days:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)

        textNoOfDays = ttk.Entry(labelframeleft,textvariable=self.var_noofdays, width=29, font=("arial", 13, "bold"))
        textNoOfDays.grid(row=6, column=1)

        #PaidTax
        lblPaidTax = Label(labelframeleft, text="Paid Tax:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPaidTax.grid(row=7, column=0, sticky=W)

        textPaidTax= ttk.Entry(labelframeleft,textvariable=self.var_paidtax, width=29, font=("arial", 13, "bold"))
        textPaidTax.grid(row=7, column=1)

        #SubTotal
        lblSubTotal = Label(labelframeleft, text="Sub Total:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)

        textSubTotal = ttk.Entry(labelframeleft,textvariable=self.var_actualtotal, width=29, font=("arial", 13, "bold"))
        textSubTotal.grid(row=8, column=1)

        #TotalCost
        lblTotalCost = Label(labelframeleft, text="Total Cost:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblTotalCost.grid(row=9, column=0, sticky=W)

        textTotalCost = ttk.Entry(labelframeleft,textvariable=self.var_total,width=29, font=("arial", 13, "bold"))
        textTotalCost.grid(row=9, column=1)

        #=========================================Bill Button==================================================================
        btnBill = Button( labelframeleft,text="Bill",command=self.total,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1,sticky=W)

        #============================================Buttons======================================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=420,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        #========================================Right Side Image==================================================
        img3 = Image.open("images/rooms.png")
        img3 = img3.resize((520, 300), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        label = Label(self.root,image=self.photoimage3,bd=0, relief=RIDGE)
        label.place(x=760, y=55, width=520, height=200)

        # ====================================Table Frame and Search System===============================================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",font=("arai", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(Table_Frame, text="Search By:", font=("arial", 12, "bold"), bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame,textvariable=self.search_var, width=24, font=("arial", 12, "bold"),state="readonly")
        combo_Search["value"] = ("Contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        textSearch = ttk.Entry(Table_Frame,textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
        textSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search",command=self.search, width=10, font=("arial", 11, "bold"),bg="black", fg="gold")
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(Table_Frame, text="Show All",command=self.fetch_data, width=10, font=("arial", 11, "bold"),bg="black", fg="gold")
        btnShowAll.grid(row=0, column=4, padx=2)

        # =============================================Show DataTable=====================================================
        Details_Table = Frame(Table_Frame, bd=2, relief=RIDGE)
        Details_Table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(Details_Table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Details_Table, orient=VERTICAL)

        self.Room_Table = ttk.Treeview(Details_Table, column=("contact", "checkin", "checkout", "roomtype", "roomsavailable", "meal", "noofdays",),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Room_Table.xview)
        scroll_y.config(command=self.Room_Table.yview)

        self.Room_Table.heading("contact", text="Contact")
        self.Room_Table.heading("checkin", text="Check-In")
        self.Room_Table.heading("checkout", text="Check-Out")
        self.Room_Table.heading("roomtype", text="Room Type")
        self.Room_Table.heading("roomsavailable", text="Room No")
        self.Room_Table.heading("meal", text="Meal")
        self.Room_Table.heading("noofdays", text="NoOfDays")

        self.Room_Table["show"] = "headings"

        self.Room_Table.column("contact", width=100)
        self.Room_Table.column("checkin", width=100)
        self.Room_Table.column("checkout", width=100)
        self.Room_Table.column("roomtype", width=100)
        self.Room_Table.column("roomsavailable", width=100)
        self.Room_Table.column("meal", width=100)
        self.Room_Table.column("noofdays", width=100)

        self.Room_Table.pack(fill=BOTH, expand=1)
        self.Room_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "All fields are mandatory", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root",database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)", (
                                                                                       self.var_contact.get(),
                                                                                       self.var_checkin.get(),
                                                                                       self.var_chekout.get(),
                                                                                       self.var_roomtype.get(),
                                                                                       self.var_roomsavailable.get(),
                                                                                       self.var_meal.get(),
                                                                                       self.var_noofdays.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room Booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)
#fetch_data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Room_Table.delete(*self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

#getcursor
    def get_cursor(self, event=""):
        cursor_row = self.Room_Table.focus()
        content = self.Room_Table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_chekout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomsavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

#Update
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("update room set Check_in=%s,Check_out=%s,Room_type=%s,Room=%s,Meal=%s,No_OF_Days=%s where Contact=%s",(
                                                                                                                                                                                   self.var_checkin.get(),
                                                                                                                                                                                   self.var_chekout.get(),
                                                                                                                                                                                   self.var_roomtype.get(),
                                                                                                                                                                                   self.var_roomsavailable.get(),
                                                                                                                                                                                   self.var_meal.get(),
                                                                                                                                                                                   self.var_noofdays.get(),
                                                                                                                                                                                   self.var_contact.get(),

                                                                                                                                                                                                      ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Room details has been updated sucessfully",parent=self.root)

#=======================================================Delete==================================================
    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?",parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
            my_cursor = conn.cursor()
            query = "delete from room where Contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
#=============================================Reset=========================================================
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_chekout.set(""),
        self.var_roomtype.set(""),
        self.var_roomsavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")


#======================================================All Data Fetching================================================
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
            my_cursor = conn.cursor()
            query=("select name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","This mobile no not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
#====================================================Gender============================================================
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
            my_cursor = conn.cursor()
            query=("select Gender from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblGender = Label(showDataframe, text="Gender:", font=("arial", 12, "bold"))
            lblGender.place(x=0, y=30)

            lbl2 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
            lbl2.place(x=90, y=30)
#==========================================================Email===============================================================
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
            my_cursor = conn.cursor()
            query=("select Email from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblGender = Label(showDataframe, text="Email:", font=("arial", 12, "bold"))
            lblGender.place(x=0, y=60)

            lbl2 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
            lbl2.place(x=90, y=60)

#====================================================Nationality===================================================
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
            my_cursor = conn.cursor()
            query=("select Nationality from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblGender = Label(showDataframe, text="Nationality:", font=("arial", 12, "bold"))
            lblGender.place(x=0, y=90)

            lbl2 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
            lbl2.place(x=90, y=90)

#================================================Address===================================================================
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
            my_cursor = conn.cursor()
            query=("select Address from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblGender = Label(showDataframe, text="Address:", font=("arial", 12, "bold"))
            lblGender.place(x=0, y=120)

            lbl2 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
            lbl2.place(x=90, y=120)
#=============================================Search System===================================================
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from room where "+ str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Room_Table.delete(*self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("", END, values=i)
            conn.commit()
        conn.close()


    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_chekout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="Breakfast"  and self.var_roomtype.get()=="Single"):
         q1=float(300)
         q2=float(700)
         q3=float(self.var_noofdays.get())
         q4=float(q1+q2)
         q5=float(q3+q4)
         Tax="Rs."+str("%.2f"%((q5)*0.09))
         ST="Rs."+str("%.2f"%((q5)))
         TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
         self.var_paidtax.set(Tax)
         self.var_actualtotal.set(ST)
         self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Luxury"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.09))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() =="Dinner" and self.var_roomtype.get() == "Double"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.09))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)






if __name__=="__main__":
        root=Tk()
        obj=ReportDetails(root)
        root.mainloop()
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from datetime import datetime
from time import strftime


class RoomDetails:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+50+90")

#========================================title======================================================
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

   #     ============================logo====================================
        img2 = Image.open("images/logo.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)


        label=Label(self.root,image=self.photoimage2,bd=0,relief=RIDGE)
        label.place(x=5,y=2,width=100,height=40)

#===================================Label Frame=======================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman", 12, "bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)


#===================================labels and enteries====================================
        #Floor
        lbl_floor= Label(labelframeleft,text="Floor",font=("arial", 12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W,padx=20)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("arial", 13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        #Room No
        lbl_RoomNo = Label(labelframeleft, text="Room No", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W)

        self.var_RoomNo=StringVar()
        entry_RoomNo = ttk.Entry(labelframeleft,textvariable=self.var_RoomNo, width=20, font=("arial", 13, "bold"))
        entry_RoomNo.grid(row=1, column=1, sticky=W)

        #Room Type
        lbl_RoomType = Label(labelframeleft, text="Room Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W)

        self.var_Room_type=StringVar()
        entry_RoomType = ttk.Entry(labelframeleft,textvariable=self.var_Room_type, width=20, font=("arial", 13, "bold"))
        entry_RoomType.grid(row=2, column=1, sticky=W)

        # ============================================Buttons======================================================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add",command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold",width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update, font=("arial", 11, "bold"), bg="black",fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete, font=("arial", 11, "bold"), bg="black",fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset_data,font=("arial", 11, "bold"), bg="black",fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

# ====================================Table Frame and Search System===============================================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details",font=("arai", 12, "bold"), padx=2)
        Table_Frame.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.Room_Table = ttk.Treeview(Table_Frame, column=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Room_Table.xview)
        scroll_y.config(command=self.Room_Table.yview)

        self.Room_Table.heading("floor", text="Floor")
        self.Room_Table.heading("roomno", text="Room No")
        self.Room_Table.heading("roomtype", text="Room Type")

        self.Room_Table["show"] = "headings"

        self.Room_Table.column("floor", width=100)
        self.Room_Table.column("roomno", width=100)
        self.Room_Table.column("roomtype", width=100)

        self.Room_Table.pack(fill=BOTH, expand=1)
        self.Room_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

#AddData
    def add_data(self):
            if self.var_floor.get() == "" or self.var_Room_type.get() == "":
                messagebox.showerror("Error", "All fields are mandatory", parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root",database="management")
                    my_cursor = conn.cursor()
                    my_cursor.execute("insert into details values(%s,%s,%s)", (
                        self.var_floor.get(),
                        self.var_RoomNo.get(),
                        self.var_Room_type.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "New Room Added Successfully", parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)

#Fetch_data

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Room_Table.delete(*self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

#cursor
    def get_cursor(self,event=""):
        cursor_row=self.Room_Table.focus()
        content=self.Room_Table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0]),
        self.var_RoomNo.set(row[1]),
        self.var_Room_type.set(row[2])

#Update
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter floor number",parent=self.root)
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("update details set Floor=%s,RoomType=%s where Room_No=%s",(
                                                                                      self.var_floor.get(),
                                                                                      self.var_Room_type.get(),
                                                                                      self.var_RoomNo.get(),
                                                                                    ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Room details has been updated sucessfully",parent=self.root)

#=======================================================Delete==================================================
    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this room details?",parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="management")
            my_cursor = conn.cursor()
            query = "delete from details where Room_No=%s"
            value = (self.var_RoomNo.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

#=================================================Reset===================================================
    def reset_data(self):
        self.var_floor.set(""),
        self.var_RoomNo.set(""),
        self.var_Room_type.set("")






if __name__=="__main__":
        root=Tk()
        obj=RoomDetails(root)
        root.mainloop()
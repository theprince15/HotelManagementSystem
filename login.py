from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import time
import datetime
import mysql.connector
from tkinter import messagebox
from datetime import datetime
from time import strftime
from hotel import HotelManagementSystem
from tkinter import *
from PIL import Image,ImageTk
from customer import Customer_Window
from room import RoomBooking
from details import RoomDetails
from report import ReportDetails
import calendar


def main():
          win=Tk()
          app=Login_Window(win)
          win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x900+0+0")

        self.bg=ImageTk.PhotoImage(file="images/login.png")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=510,y=170,width=340,height=450)

        img1=Image.open("images/login1.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=630,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label
        username=lbl=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"),show="*")
        self.txtpass.place(x=40, y=250, width=270)

#====================================================Icon Images==================================================
        img2 = Image.open("images/login1.png")
        img2 = img2.resize((25,25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=550, y=323 , width=25, height=25)

        img3 = Image.open("images/login2.png")
        img3 = img3.resize((45, 45), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=550, y=395, width=25, height=25)

#loginbutton
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman", 15, "bold"),bd=3,relief=RIDGE,fg="white",bg="cyan",activeforeground="white",activebackground="cyan")
        loginbtn.place(x=110,y=300,width=120,height=35)

#registerbutton
        registerbtn = Button(frame, text="New User Register",command=self.register_window, font=("times new roman", 10, "bold"), borderwidth=0, fg="white",bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

#forgotpasswordbutton
        loginbtn = Button(frame, text="Forgot Password", command=self.forgot_passwrd_window,font=("times new roman", 10, "bold"),borderwidth=0, fg="white",bg="black", activeforeground="white", activebackground="black")
        loginbtn.place(x=10, y=370, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are mandatory")
        elif self.txtuser.get()=="Prince" and self.txtpass.get()=="prince":
            messagebox.showinfo("Success","Welcome to Hotel Management System")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get(),
                                                                                       ))
            row=my_cursor.fetchone()

            #print(row)
            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:

                #open_main=messagebox.askyesno("YesNo","Successful")
                #if open_main>0:
                self.new_window=Toplevel(self.root)
                self.app=HotelManagementSystem(self.new_window)
                #else:
                    #if not open_main:
                        #return
            conn.commit()
            conn.close()

#=====================================================Reset Password==========================================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="management")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct security answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset successfully",parent=self.root2)
                self.root2.destroy()


#=====================================================Forgot Password========================================
    def forgot_passwrd_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Pleaser enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="management")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error","Please enter the valid email address")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l1=Label(self.root2,text="Forgot Password",font=("times new roman", 20, "bold"), fg="blue", bg="white")
                l1.place(x=0,y=10,relwidth=1)

                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"),bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth place", "Your favourite mentor", "Your Pet name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white",fg="black")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password= Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white",fg="black")
                new_password.place(x=50, y=220)

                self.txt_new_password = ttk.Entry(self.root2, font=("times new roman", 15,"bold"))
                self.txt_new_password.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman", 15,"bold"),fg="white",bg="green")
                btn.place(x=120,y=290,width=100)


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
#==========================================Variables================================================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_passwrd=StringVar()
        self.var_confpasswrd=StringVar()

#==================================BG IMAGE=========================================================
        self.bg=ImageTk.PhotoImage(file="images/Register.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

#==================================left image=========================================================
        self.bg1= ImageTk.PhotoImage(file="images/Register1.png")
        bg_lbl = Label(self.root, image=self.bg1)
        bg_lbl.place(x=50, y=100,width=470,height=550)

#====================================main frame=========================================================
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="deep sky blue",bg="white")
        register_lbl.place(x=20,y=20)

#===========================================Label and entry================================================
        #------------------row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #----------------------row2
        contact= Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white",fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200,width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)
        #------------------------row3
        security_Q = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ, font=("times new roman", 15, "bold"),state="readonly")
        self.combo_security_Q["values"] = ("Select","Your Birth place","Your favourite mentor", "Your Pet name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white",fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame,textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        #---------------------------------row4----------------------------------------
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_passwrd, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpasswrd,font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        #===================================Check Button===================================================
        self.var_Check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_Check,text="I Agree The Terms & conditons",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        #============================================Buttons==================================================
        img=Image.open("images/registernow.png")
        img=img.resize((200,55),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=70,y=420,width=200)

        img1 = Image.open("images/registernow1.png")
        img1 = img1.resize((200, 45), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1,command=self.return_login, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b1.place(x=400, y=420, width=200)

#============================================Function Declaration===========================================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ=="Select":
            messagebox.showerror("Error","All fields are mandatory",parent=self.root)
        elif self.var_passwrd.get()!=self.var_confpasswrd.get():
            messagebox.showerror("Error","Passoword and confirm password must be same",parent=self.root)
        elif self.var_Check.get()==0:
            messagebox.showerror("Error","Please agree out terms and conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_fname.get(),
                                                                                       self.var_lname.get(),
                                                                                       self.var_contact.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_securityQ.get(),
                                                                                       self.var_securityA.get(),
                                                                                       self.var_passwrd.get()
                                                                                        ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successful")
                self.root.destroy()

    def return_login(self):
        self.root.destroy()

#=============================Main Window==========================================================
class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        #==================================1st image====================================
        img1=Image.open("images\hotel.png")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        label = Label(self.root, image=self.photoimage1, bd=4, relief=RIDGE)
        label.place(x=0, y=0, width=1550, height=140)

        #============================logo====================================
        img2 = Image.open("images\logo.png")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)


        label=Label(self.root,image=self.photoimage2,bd=4,relief=RIDGE)
        label.place(x=0,y=0,width=230,height=140)

        #      ==========================Title======================================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)


        #      ================================main frame==================================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)


        #      =============================menu============================================
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #     ====================================button frame=====================================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="ROOM",command=self.room_booking, width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS",command=self.room_details, width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT",command=self.report_details, width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame,command=self.logoout, text="LOGOUT", width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)

        #===============================RIGHT SIDE IMAGE================================================
        img3 = Image.open("images\img3.png")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        label1 = Label(main_frame, image=self.photoimage3, bd=4, relief=RIDGE)
        label1.place(x=225, y=0, width=1310, height=590)

        #===========================down images=========================================================
        img4 = Image.open("images\img4.png")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimage4 = ImageTk.PhotoImage(img4)

        label1 = Label(main_frame, image=self.photoimage4, bd=4, relief=RIDGE)
        label1.place(x=0, y=225, width=230, height=210)

        img5 = Image.open("images\img5.png")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.photoimage5 = ImageTk.PhotoImage(img5)

        label1 = Label(main_frame, image=self.photoimage5, bd=4, relief=RIDGE)
        label1.place(x=0, y=420, width=230, height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Customer_Window(self.new_window)

    def room_booking(self):
        self.new_window=Toplevel(self.root)
        self.app=RoomBooking(self.new_window)

    def room_details(self):
        self.new_window=Toplevel(self.root)
        self.app=RoomDetails(self.new_window)

    def report_details(self):
        self.new_window = Toplevel(self.root)
        self.app = ReportDetails(self.new_window)

    def logoout(self):
        self.root.destroy()



if __name__=="__main__":
        main()

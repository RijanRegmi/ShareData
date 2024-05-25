from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import ctypes
import random,os
import mysql.connector 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sqlalchemy import create_engine
# import login as firtpage

myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)




class sharedata:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+280+95")
        self.root.title("Share Data")
        self.root.resizable(0, 0)
        img = PhotoImage(file='image/RJNnobg.png')
        root.iconphoto(False, img)
        self.products_added = []
        self.fp()
        self.info_table = None
        self.share_info_table = None


    def insert(self):
        Fname = self.txtfirstname.get()
        Lname = self.txtlastname.get()
        contact = self.txlcontact.get()
        email = self.txlemail.get()
        password = self.txtpassword.get()
        confrimpassword = self.txtconfrimpassword.get()

        if Fname == "" or Lname == "" or contact == "" or email == "" or password == "" or confrimpassword == "" :
            messagebox.showinfo("Insert Status", "All Fields are required")
        elif password != confrimpassword:
            messagebox.showinfo("Insert Status", "Confrim password dosenot match to Password")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="login")
            cursor = con.cursor()
            cursor.execute("insert into sid values('" + Fname + "','" + Lname + "','" + contact + "','" + email + "','" + password + "','" + confrimpassword + "')")
            cursor.execute("commit")

            messagebox.showinfo("Insert Status", "Account created")
            con.close()

    
    def check_login(self):
        contact = self.txtusername.get()
        password = self.txtpword.get()

        # Connect to MySQL database
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="login")
        cursor = conn.cursor()

        # Execute SQL query to check if username and password match
        query = "SELECT * FROM sid WHERE contact=%s AND password=%s"
        cursor.execute(query, (contact, password))
        account = cursor.fetchone()

        if account:
            self.window()
            
        else:
            messagebox.showinfo("Login","Login Failed")
            self.login()


    def data(self):
        date = self.txtdate.get()
        symbol = self.txtsymbol.get()
        name = self.txts_name.get()
        status = self.Combo_status.get()
        qty = self.txtqty.get()
        amount = self.txtamount.get()
        # self.chart()
        

        if date == "" or symbol == "" or name == "" or status == "" or qty == "" or amount == "" :
            messagebox.showinfo("Insert Status", "All Fields are required")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="share_data")
            cursor = con.cursor()
            cursor.execute("insert into s_data values('" + date + "','" + symbol + "','" + name + "','" + status + "','" + qty + "','" + amount + "')")
            cursor.execute("commit")

            messagebox.showinfo("Insert Status", "Date stored")
            con.close()
            self.fetch_data()


    def forshare(self):
        date = self.txtDate.get()
        hari = self.txtHari.get()
        rijan = self.txtRijan.get()
        anita = self.txtAnita.get()
        rishav = self.txtRishav.get()

        if date == "" or hari == "" or rijan == "" or anita == "" or rishav == "":
            messagebox.showinfo("Insert Status", "All Fields are required")
            return

        try:
            hari = float(hari)
            rijan = float(rijan)
            anita = float(anita)
            rishav = float(rishav)
            total_value = hari + rijan + anita + rishav
        except ValueError:
            messagebox.showinfo("Insert Status", "Please enter valid numbers for Hari, Rijan, Anita, and Rishav")
            return

        try:
            con = mysql.connector.connect(host="localhost", user="root", password="root", database="share_data")
            cursor = con.cursor()
            query = "INSERT INTO share (date, Hari, Rijan, Anita, Rishav, total_amount) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (date, hari, rijan, anita, rishav, total_value)
            cursor.execute(query, values)
            con.commit()

            messagebox.showinfo("Insert Status", "Data stored")
        except mysql.connector.Error as err:
            messagebox.showinfo("Insert Status", f"Error: {err}")
        finally:
            con.close()



    
        
#MMKJL
# =====
#MEHL
#MKSC

        
    def fp(self):
        #frame
        firstpage_Frame = Frame(self.root,  relief=GROOVE, bg="#9FA8B2")
        firstpage_Frame.place(x=0, y=0, width=1366, height=768)

        #image1
        fpimg1 = Image.open("image/stock.jpg")
        fpimg1 = fpimg1.resize((1366, 768))
        self.photofpimg1 = ImageTk.PhotoImage(fpimg1)

        lblfppimg1 = Label(firstpage_Frame, image=self.photofpimg1, bg="#9FA8B2")
        lblfppimg1.place(x=0, y=0, width=1366, height=768)


        #fp frame
        fp_Frame = Frame(firstpage_Frame,  relief=GROOVE, bg="#9FA8B2")
        fp_Frame.place(x=520, y=120, width=330, height=450)


        #image
        loginimg = Image.open("image/RJNnobg.png")
        loginimg = loginimg.resize((80, 80))
        self.photologinimg = ImageTk.PhotoImage(loginimg)

        lbl_loginimg = Label(fp_Frame, image=self.photologinimg, bg="#9FA8B2")
        lbl_loginimg.place(x=130, y=40, width=80, height=80)


        #button
        self.btnforlogin = Button(fp_Frame, text="login", height=50, command=self.login,  font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#FFFFFF", width=120, cursor="hand2")
        self.btnforlogin.place(x=100, y=160, width=130, height=44)

        #button2
        self.btnforsignup = Button(fp_Frame, text="signup", command=self.signup, height=50, font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#FFFFFF", width=120, cursor="hand2")
        self.btnforsignup.place(x=100, y=260, width=130, height=44)

        # ===========================================================login============================================================

    def login(self):

        self.username = StringVar()
        self.pword = StringVar()


        login_Frame = Frame(self.root,  relief=GROOVE, bg="#9FA8B2")
        login_Frame.place(x=0, y=0, width=1366, height=768)

        

        #image1
        loginimg1 = Image.open("image/stock.jpg")
        loginimg1 = loginimg1.resize((1366, 768))
        self.photologinimg1 = ImageTk.PhotoImage(loginimg1)

        lbl_loginimg1 = Label(login_Frame, image=self.photologinimg1, bg="#9FA8B2")
        lbl_loginimg1.place(x=0, y=0, width=1366, height=768)

        #image2
        loginimg2 = Image.open("image/login.png")
        loginimg2 = loginimg2.resize((600, 450))
        self.photologinimg2 = ImageTk.PhotoImage(loginimg2)

        lbl_loginimg2 = Label(login_Frame, image=self.photologinimg2, bg="#9FA8B2")
        lbl_loginimg2.place(x=120, y=120, width=600, height=450)

        
        #pageframe
        page_Frame = Frame(login_Frame,  relief=GROOVE, bg="#9FA8B2")
        page_Frame.place(x=950, y=120, width=330, height=450)

        #image
        signupimg = Image.open("image/RJNnobg.png")
        signupimg = signupimg.resize((80, 80))
        self.photosignupimg = ImageTk.PhotoImage(signupimg)

        lbl_signupimg = Label(page_Frame, image=self.photosignupimg, bg="#9FA8B2")
        lbl_signupimg.place(x=120, y=10, width=80, height=80)


        self.btnback = Button(login_Frame, text="⬅", command=self.fp, height=50, font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#FFFFFF", width=120, cursor="hand2")
        self.btnback.place(x=10, y=10, width=20, height=20)


        #username
        self.lblusername = Label(page_Frame, text="Contact",   font=("arial", 18, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lblusername.place(x=105, y=120)

        self.txtusername = ttk.Entry(page_Frame, font=("arial", 12, "bold"), width=24)
        self.txtusername.place(x=50, y=160)


        #password
        self.lblpword = Label(page_Frame, text="password", font=("arial", 18, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lblpword.place(x=105, y=220)

        self.txtpword = ttk.Entry(page_Frame, show="*",  font=("arial", 12, "bold"), width=24)
        self.txtpword.place(x=50, y=260)


        #button
        self.btnlogin = Button(page_Frame, text="login", command=self.check_login, height=50, font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#FFFFFF", width=120, cursor="hand2")
        self.btnlogin.place(x=100, y=350, width=130, height=44)



        # ===============================================================signup==============================================================

    def signup(self):
        
        
        
        signup_Frame = Frame(self.root, relief=GROOVE, bg="#9FA8B2")
        signup_Frame.place(x=0, y=0, width=1366, height=768)

       

        signupimg1 = Image.open("image/stock.jpg")
        signupimg1 = signupimg1.resize((1366, 768))
        self.photosignupimg1 = ImageTk.PhotoImage(signupimg1)

        lbl_signupimg1 = Label(signup_Frame, image=self.photosignupimg1, bg="#9FA8B2")
        lbl_signupimg1.place(x=0, y=0, width=1366, height=768)

        #frame
        user_Frame = Frame(signup_Frame,  relief=GROOVE, bg="#9FA8B2")
        user_Frame.place(x=200, y=90, width=966, height=568)

        #image
        img2 = Image.open("image/RJNnobg.png")
        img2 = img2.resize((80, 80))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_img2 = Label(user_Frame, image=self.photoimg2, bg="#9FA8B2")
        lbl_img2.place(x=450, y=10, width=80, height=80)

        self.btnback = Button(signup_Frame, text="⬅", command=self.fp, height=50, font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#FFFFFF", width=120, cursor="hand2")
        self.btnback.place(x=10, y=10, width=20, height=20)

        

        #firstname
        self.lbfirstlname = Label(user_Frame, text="First Name", font=("arial", 18, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lbfirstlname.place(x=170, y=120)

        self.txtfirstname = ttk.Entry(user_Frame, font=("arial", 16, "bold"), width=26)
        self.txtfirstname.place(x=95, y=160)



        #lastname
        self.lblastlname = Label(user_Frame, text="Last Name", font=("arial", 18, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lblastlname.place(x=680, y=120)

        self.txtlastname = ttk.Entry(user_Frame, font=("arial", 16, "bold"), width=26)
        self.txtlastname.place(x=595, y=160)


        # contact
        self.lblcontact = Label(user_Frame, text="Contact", font=("arial", 18, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lblcontact.place(x=190, y=220)

        self.txlcontact = ttk.Entry(user_Frame, font=("arial", 16, "bold"), width=26)
        self.txlcontact.place(x=95, y=260)

        # email
        self.lblemail = Label(user_Frame, text="email", font=("arial", 18, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lblemail.place(x=700, y=220)

        self.txlemail = ttk.Entry(user_Frame, font=("arial", 16, "bold"), width=26)
        self.txlemail.place(x=595, y=260)


        #password
        self.lblpassword = Label(user_Frame, text="password", font=("arial", 18, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lblpassword.place(x=180, y=320)

        self.txtpassword = ttk.Entry(user_Frame,show="*", font=("arial", 16, "bold"), width=26)
        self.txtpassword.place(x=95, y=360)

        # button_mode=True

        # def hide():
        #     global button_mode
        #     if button_mode:
        #         self.btnopen_eye.config(image=closeeye,activebackground="white") 
        #         self.txtpassword.config(show="*")
        #         button_mode=False
        #     else:
        #         self.btnopen_eye.config(image=openeye,activebackground="white") 
        #         self.txtpassword.config(show="*")
        #         button_mode=True


        
        # openeye = PhotoImage(file="image/eye.png")
        # closeeye = PhotoImage(file="image/hidden.png")
        # #open_button
        # self.btnopen_eye = Button(user_Frame, image=openeye, command=hide,  height=50,  width=120, cursor="hand2")
        # self.btnopen_eye.place(x=720, y=450, width=20, height=20)

        #confrimpassword
        self.lblconfrimpassword = Label(user_Frame, text="confrim password", font=("arial", 18, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lblconfrimpassword.place(x=630, y=320)

        self.txtconfrimpassword = ttk.Entry(user_Frame,show="*", font=("arial", 16, "bold"), width=26)
        self.txtconfrimpassword.place(x=595, y=360)


        #button
        self.btnsingup = Button(user_Frame, command=self.insert, text="Sign up", height=50, font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#FFFFFF", width=120, cursor="hand2")
        self.btnsingup.place(x=320, y=450, width=130, height=44)

        self.btnlogin = Button(user_Frame, command=self.login, text="Login", height=50, font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#FFFFFF", width=120, cursor="hand2")
        self.btnlogin.place(x=520, y=450, width=130, height=44)

        

        # ==========================================================================window===================================================================
    def window(self):
        left_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="#126CAA")
        left_Frame.place(x=0, y=0, width=180, height=768)

        #Image
        img = Image.open("image/RJNnobg.png")
        img = img.resize((60, 60))
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_img = Label(left_Frame, image=self.photoimg, bg="#126CAA")
        lbl_img.place(x=50, y=10, width=60, height=60)


        self.btnshare = Button(left_Frame, text="Share", command=self.share, height=50, font=('arial', 15, 'bold'), bg="#9FA8B2", fg="#FFFFFF", width=120, cursor="hand2")
        self.btnshare.place(x=20, y=80, width=130, height=44)


        self.btndata = Button(left_Frame, text="Data", command=self.sharedata, height=50, font=('arial', 15, 'bold'), bg="#9FA8B2", fg="#FFFFFF", width=120, cursor="hand2")
        self.btndata.place(x=20, y=150, width=130, height=44)
    
        self.btnlogout = Button(left_Frame, text="Logout", command=self.logout, height=50, font=('arial', 15, 'bold'), bg="#9FA8B2", fg="#FFFFFF", width=120, cursor="hand2")
        self.btnlogout.place(x=20, y=220, width=130, height=44)
        self.share()

    def logout(self):
        if self.btnlogout:
            result = messagebox.askokcancel("Logout", "Are you sure you want to logout?")
            if result:
                self.fp()
            else:
                messagebox.showinfo("Cancelled", "Logout was cancelled.")
                
            
            
        



# =========================================================================share_data=========================================================================

    def sharedata(self):

        

        
        # ====================Variable=====================
        self.date_data = StringVar()
        self.symbol = StringVar()
        self.name = StringVar()
        self.qty = IntVar()
        self.amount = IntVar()
        self.search_data = StringVar()
        self.status_data=StringVar()




        self.status=["Buy","Sell"]

        share_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="#9FA8B2")
        share_Frame.place(x=180, y=0, width=1186, height=768)

        #Image1
        img1 = Image.open("image/RJNnobg.png")
        img1 = img1.resize((80, 80))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl_img1 = Label(share_Frame, image=self.photoimg1, bg="#9FA8B2")
        lbl_img1.place(x=10, y=10, width=80, height=80)

        #date
        self.lbldate = Label(share_Frame, text="date", font=("arial", 12, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lbldate.place(x=55, y=100)

        self.txtdate = ttk.Entry(share_Frame, textvariable=self.date_data, font=("arial", 12, "bold"), width=10)
        self.txtdate.place(x=30, y=150)

        #symbol
        self.lblsymbol = Label(share_Frame, text="Symbol", font=("arial", 12, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lblsymbol.place(x=170, y=100)

        self.txtsymbol = ttk.Entry(share_Frame, textvariable=self.symbol, font=("arial", 12, "bold"), width=12)
        self.txtsymbol.place(x=150, y=150)

        #firstname
        self.lbls_name = Label(share_Frame, text="Name", font=("arial", 12, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lbls_name.place(x=320, y=100)

        self.txts_name = ttk.Entry(share_Frame, textvariable=self.name, font=("arial", 12, "bold"), width=18)
        self.txts_name.place(x=290, y=150)

        #status
        self.lblstatus = Label(share_Frame, text="Status", font=("arial", 12, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lblstatus.place(x=490, y=100)

        self.Combo_status=ttk.Combobox(share_Frame, textvariable=self.status_data, value=self.status, font = ("arial",12,"bold"),width=8,state="readonly")
        # self.Combo_status.current(0)
        self.Combo_status.place(x=480, y=150)

        #qty
        self.lblqty = Label(share_Frame, text="QTY", font=("arial", 12, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lblqty.place(x=625, y=100)

        self.txtqty = ttk.Entry(share_Frame, textvariable=self.qty, font=("arial", 12, "bold"), width=10)
        self.txtqty.place(x=600, y=150)


        #amount
        self.lblamount = Label(share_Frame, text="Amount", font=("arial", 12, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lblamount.place(x=740, y=100)

        self.txtamount = ttk.Entry(share_Frame, textvariable=self.amount, font=("arial", 12, "bold"), width=12)
        self.txtamount.place(x=725, y=150)


        #button
        self.btnadddata = Button(share_Frame, text="Add", height=1, font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#FFFFFF",
                             width=10, cursor="hand2", command=self.adddata)
        self.btnadddata.place(x=30, y=300)

        self.btnsavedata = Button(share_Frame, text="Save", height=1, font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#FFFFFF",
                              width=10, cursor="hand2", command=self.savedata)
        self.btnsavedata.place(x=30, y=350)

        self.btncleardata = Button(share_Frame, text="Clear", command=self.cleardata, height=1, font=('arial', 15, 'bold'),
                               bg="#4f5c8b", fg="#FFFFFF", width=10, cursor="hand2")
        self.btncleardata.place(x=30, y=400)

        self.btnupdate = Button(share_Frame, text="Update", command=self.update,  height=1, font=('arial', 15, 'bold'),
                               bg="#4f5c8b", fg="#FFFFFF", width=10, cursor="hand2")
        self.btnupdate.place(x=30, y=450)

        self.btndelete = Button(share_Frame, text="Delete", command=self.delete,  height=1, font=('arial', 15, 'bold'),
                               bg="#4f5c8b", fg="#FFFFFF", width=10, cursor="hand2")
        self.btndelete.place(x=30, y=500)



        # # search
        Search_Frame = Frame(share_Frame, bd=2, bg="#9FA8B2")
        Search_Frame.place(x=350, y=200, width=750, height=40)

        

        self.lbldata = Label(Search_Frame, text="Date", font=("arial", 13, "bold"), bg="#4f5c8b", fg="#FFFFFF")
        self.lbldata.grid(row=0, column=0, sticky=W, padx=1)

        self.txt_Search = ttk.Entry(Search_Frame, textvariable=self.search_data, font=('arial', 13, 'bold'), width=12)
        self.txt_Search.grid(row=0, column=1, sticky=W, padx=2)

        self.btnSearch = Button(Search_Frame, text="Search", font=('arial', 9, 'bold'), bg="#4f5c8b", fg="#FFFFFF",
                                width=10, cursor="hand2", command=self.data_search)
        self.btnSearch.grid(row=0, column=2)



        # dataframe info aria
        dataLabelFrame = LabelFrame(share_Frame, text="Info Aria", font=("times new romen", 12, "bold"), bg="white",fg="#b90508")
        dataLabelFrame.place(x=200, y=230, width=950, height=290)

        scroll_y = Scrollbar(dataLabelFrame, orient=VERTICAL)
        self.texta = Text(dataLabelFrame, yscrollcommand=scroll_y.set, font=("times new romen", 12, "bold"), bg="white", fg="#b90508")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.texta.yview)
        self.texta.pack(fill=BOTH, expand=1)
        self.shareData()

        self.fetch_data()



    # ===================================================info====================================================================


# date == "" or symbol == "" or name == "" or status == "" or qty == "" or amount == ""

        info_Frame = Frame(share_Frame, bd=5, relief=GROOVE, bg="#9FA8B2")
        info_Frame.place(x=200, y=550, width=950, height=200)

        scroll_x = ttk.Scrollbar(info_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(info_Frame, orient=VERTICAL)
        self.info_table = ttk.Treeview(info_Frame, columns=("date", "symbol", "name", "status", "qty", "amount"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.info_table.heading("date", text="Date")
        self.info_table.heading("symbol", text="Symbol")
        self.info_table.heading("name", text="Name")
        self.info_table.heading("status", text="Status")
        self.info_table.heading("qty", text="QTY")
        self.info_table.heading("amount", text="Amount")

        self.info_table["show"] = "headings"

        self.info_table.pack(fill=BOTH, expand=1)

        self.info_table.column("date", width=30)
        self.info_table.column("symbol", width=30)
        self.info_table.column("name", width=30)
        self.info_table.column("status", width=30)
        self.info_table.column("qty", width=30)
        self.info_table.column("amount", width=30)

        self.info_table.pack(fill=BOTH, expand=1)
        self.info_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
        
        


    def update(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="share_data")
        my_cursor = conn.cursor()
        my_cursor.execute(
                "UPDATE s_data SET date=%s, name=%s, status=%s, qty=%s, amount=%s WHERE symbol=%s",
                (self.date_data.get(), self.name.get(), self.status_data.get(), self.qty.get(), self.amount.get(), self.symbol.get())
            )
        conn.commit()
        messagebox.showinfo("Updated","Updated Succesfully!")
        my_cursor.close()
        conn.close()
        self.fetch_data()





    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="share_data")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM s_data")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            if self.info_table is not None:
                self.info_table.delete(*self.info_table.get_children())
                for i in rows:
                    self.info_table.insert("", END, value=i)
                conn.commit()
        conn.close()  


    def get_cursor(self,event=""):
        cursor_row=self.info_table.focus()
        content=self.info_table.item(cursor_row)
        row=content["values"]
        self.date_data.set(row[0])
        self.symbol.set(row[1])
        self.name.set(row[2])
        self.status_data.set(row[3])
        self.qty.set(row[4])
        self.amount.set(row[5])

    def delete(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="share_data")
        my_cursor = conn.cursor()
        query="delete from s_data where symbol=%s"
        value=(self.symbol.get(),)
        my_cursor.execute(query,value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Deleted successfully")
               



        

    def adddata(self):
        if self.symbol.get() == "" or self.name.get() == "" or self.qty.get() == "" or self.amount.get() == "":
            messagebox.showerror("Error", "Enter Share Value for all members")
        elif self.date_data.get() == "":
            messagebox.showerror("Error", "Enter Date")
        else:
            self.totalamount = float(self.qty.get()) * float(self.amount.get())
            self.texta.insert(END,f"\n{self.date_data.get()}\t\t{self.symbol.get()}\t\t{self.name.get()}\t\t{self.status_data.get()}\t\t{self.qty.get()}\t\t{self.amount.get()}\t\t{self.totalamount}")
            self.data()


            

    # def date(self):
    #     self.texta.insert(END,f"\n Date:{self.date_data.get()}")

    


    def savedata(self):
        op=messagebox.askyesno("Save Share","Do you want to save the Share?")
        if op>0:
            self.data_info=self.texta.get(1.0,END)
            f1=open('data/'+str(self.date_data.get())+".txt",'w')
            f1.write(self.data_info)
            op=messagebox.showinfo("Saved",f"Date:{self.date_data.get()} saved successfully")
            
            f1.close()


    def cleardata(self):
        op=messagebox.askyesno("Clear Share","Do you want to Clear all?")
        if op>0:
            self.texta.delete(1.0,END)
            self.date_data.set("")
            self.symbol.set("")
            self.qty.set(0)
            self.name.set("")
            self.amount.set(0)
            self.search_data.set("")
            self.status_data.set("")
            self.shareData()


    def shareData(self):
        self.texta.delete(1.0,END)
        self.texta.insert(END,"\n======================================================================================================")
        self.texta.insert(END,f"\n Date\t\tSymbol\t\tName\t\tStatus\t\tqty\t\tAmount\t\tTotal")
        self.texta.insert(END,"\n======================================================================================================\n")


    def data_search(self):
        found = "no"
        for filename in os.listdir("data"):
            if filename.split('.')[0]==(self.search_data.get()):
                with open(os.path.join("data", filename), 'r') as f1:
                    data_data = f1.read()
                    self.texta.delete(1.0, END)
                    self.texta.insert(END, data_data)
                found = "yes"
                break
        if found == 'no':
            messagebox.showerror("Error", "Invalid data No.")



    




        # ====================================================================================SHARE===========================================================================================

    def share(self):
        # self.chart()

        self.date = StringVar()
        self.hari = DoubleVar()
        self.rijan = DoubleVar()
        self.anita = DoubleVar()
        self.rishav = DoubleVar()
        self.total_value = DoubleVar()
        self.root = root
        

        Main_Frame = Frame(self.root, bd=5, bg="white")
        Main_Frame.place(x=180, y=0, width=1186, height=768)


        #Image1
        img2 = Image.open("image/RJNnobg.png")
        img2 = img2.resize((80, 80))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_img2 = Label(Main_Frame, image=self.photoimg2, bg="white")
        lbl_img2.place(x=10, y=10, width=80, height=80)

        # ======================Variables======================
        self.date = StringVar()
        self.hari = StringVar()
        self.rijan = StringVar()
        self.anita = StringVar()
        self.rishav = StringVar()
        self.date = StringVar()
        # self.bill_no.set(str(random.randint(1000, 9999)))
        self.search_bill = StringVar()
        self.total_value = StringVar()

        

        #date
        self.lblDate = Label(Main_Frame, text="Date", font=("arial", 18, "bold"), bg="white",fg="black", bd=4)
        self.lblDate.place(x=50, y=100)

        self.txtDate = ttk.Entry(Main_Frame, textvariable=self.date, font=("arial", 18, "bold"), width=24)
        self.txtDate.place(x=250, y=100)

        # Hari Regmi
        self.lblHari = Label(Main_Frame, text="Hari Regmi", font=("arial", 18, "bold"), bg="white",fg="black", bd=4)
        self.lblHari.place(x=50, y=180)

        self.txtHari = ttk.Entry(Main_Frame, textvariable=self.hari, font=("arial", 18, "bold"), width=24)
        self.txtHari.place(x=250, y=180)

        # Rijan Regmi
        self.lblRijan = Label(Main_Frame, text="Rijan Regmi", font=("arial", 18, "bold"), bg="white",fg="black", bd=4)
        self.lblRijan.place(x=50, y=260)

        self.txtRijan = ttk.Entry(Main_Frame, textvariable=self.rijan, font=("arial", 18, "bold"), width=24)
        self.txtRijan.place(x=250, y=260)

        # Anita Regmi
        self.lblAnita = Label(Main_Frame, text="Anita Regmi", font=("arial", 18, "bold"), bg="white",fg="black", bd=4)
        self.lblAnita.place(x=50, y=340)

        self.txtAnita = ttk.Entry(Main_Frame, textvariable=self.anita, font=("arial", 18, "bold"), width=24)
        self.txtAnita.place(x=250, y=340)

        # Rishav Regmi
        self.lblRishav = Label(Main_Frame, text="Rishav Regmi", font=("arial", 18, "bold"), bg="white",fg="black", bd=4)
        self.lblRishav.place(x=50, y=420)

        self.txtRishav = ttk.Entry(Main_Frame, textvariable=self.rishav, font=("arial", 18, "bold"), width=24)
        self.txtRishav.place(x=250, y=420)

        # button
        self.btnadd = Button(Main_Frame, text="Add", height=1, font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#FFFFFF",
                             width=10, cursor="hand2", command=self.add)
        self.btnadd.place(x=10, y=480)

        self.btnsave = Button(Main_Frame, text="Save", height=1, font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#FFFFFF",
                              width=10, cursor="hand2", command=self.save)
        self.btnsave.place(x=150, y=480)

        self.btnclear = Button(Main_Frame, text="Clear", command=self.clear, height=1, font=('arial', 15, 'bold'),
                               bg="#4f5c8b", fg="#FFFFFF", width=10, cursor="hand2")
        self.btnclear.place(x=290, y=480)

        self.btnclear = Button(Main_Frame, text="View Chart", command=self.LineGraph, height=1, font=('arial', 15, 'bold'),
                               bg="#4f5c8b", fg="#FFFFFF", width=15, cursor="hand2")
        self.btnclear.place(x=430, y=480)
        self.fetch_share()


        # search
        Search_Frame = Frame(Main_Frame, bd=2, bg="white")
        Search_Frame.place(x=750, y=40, width=350, height=40)

        self.lblBill = Label(Search_Frame, text="Date", font=("arial", 13, "bold"), bg="#4f5c8b", fg="white")
        self.lblBill.grid(row=0, column=0, sticky=W, padx=1)

        self.txt_Entry_Search = ttk.Entry(Search_Frame, textvariable=self.search_bill, font=('arial', 13, 'bold'), width=12)
        self.txt_Entry_Search.grid(row=0, column=1, sticky=W, padx=2)

        self.btnSearch = Button(Search_Frame, text="Search", font=('arial', 9, 'bold'), bg="#4f5c8b", fg="white",
                                width=10, cursor="hand2", command=self.find_bill)
        self.btnSearch.grid(row=0, column=2)

        # rightframe Bill aria
        RightLabelFrame = LabelFrame(Main_Frame, text="Info Aria", font=("times new romen", 12, "bold"), bg="white",
                                     fg="#b90508")
        RightLabelFrame.place(x=650, y=80, width=450, height=460)

        scroll_y = Scrollbar(RightLabelFrame, orient=VERTICAL)
        self.textarea = Text(RightLabelFrame, yscrollcommand=scroll_y.set, font=("times new romen", 12, "bold"),
                             bg="white", fg="#b90508")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
        self.display_share()



        # =========================================Bottem Frame=========================================


        bottom_Frame = Frame(Main_Frame, relief=GROOVE, bg="white")
        bottom_Frame.place(x=0, y=550, width=1186, height=218)

        share_info_Frame = Frame(bottom_Frame, bd=5, relief=GROOVE, bg="#9FA8B2")
        share_info_Frame.place(x=200, y=10, width=950, height=200)

        #button
        self.btnupdate = Button(bottom_Frame, text="Update", command=self.update_share, height=1, font=('arial', 15, 'bold'),
                                bg="#4f5c8b", fg="#FFFFFF", width=10, cursor="hand2")
        self.btnupdate.place(x=30, y=50)

        self.btndelete = Button(bottom_Frame, text="Delete", command=self.delete_share, height=1, font=('arial', 15, 'bold'),
                                bg="#4f5c8b", fg="#FFFFFF", width=10, cursor="hand2")
        self.btndelete.place(x=30, y=100)

        scroll_x = ttk.Scrollbar(share_info_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(share_info_Frame, orient=VERTICAL)
        self.share_info_table = ttk.Treeview(share_info_Frame, columns=("date", "hari", "rijan", "anita", "rishav", "total_value"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.share_info_table.heading("date", text="Date")
        self.share_info_table.heading("hari", text="Hari")
        self.share_info_table.heading("rijan", text="Rijan")
        self.share_info_table.heading("anita", text="Anita")
        self.share_info_table.heading("rishav", text="Rishav")
        self.share_info_table.heading("total_value", text="Total")

        self.share_info_table["show"] = "headings"

        self.share_info_table.pack(fill=BOTH, expand=1)

        self.share_info_table.column("date", width=30)
        self.share_info_table.column("hari", width=30)
        self.share_info_table.column("rijan", width=30)
        self.share_info_table.column("anita", width=30)
        self.share_info_table.column("rishav", width=30)
        self.share_info_table.column("total_value", width=30)

        self.share_info_table.pack(fill=BOTH, expand=1)
        self.share_info_table.bind("<ButtonRelease-1>", self.get_cursor1)

        self.fetch_share()

    def update_share(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="share_data")
        my_cursor = conn.cursor()
        my_cursor.execute(
            "UPDATE share SET date=%s, hari=%s, rijan=%s, anita=%s, rishav=%s, total_amount=%s WHERE date=%s",
            (self.date.get(), self.hari.get(), self.rijan.get(), self.anita.get(), self.rishav.get(), self.total_value.get(), self.date.get())
        )
        conn.commit()
        messagebox.showinfo("Updated", "Updated Successfully!")
        my_cursor.close()
        conn.close()
        self.fetch_share()

    def fetch_share(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="share_data")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM share")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            if self.share_info_table is not None:
                self.share_info_table.delete(*self.share_info_table.get_children())
                for i in rows:
                    self.share_info_table.insert("", END, value=i)
                conn.commit()
        conn.close()

    def get_cursor1(self, event=""):
        cursor_row = self.share_info_table.focus()
        content = self.share_info_table.item(cursor_row)
        row = content["values"]
        self.date.set(row[0])
        self.hari.set(row[1])
        self.rijan.set(row[2])
        self.anita.set(row[3])
        self.rishav.set(row[4])
        self.total_value.set(row[5])

    def delete_share(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="share_data")
        my_cursor = conn.cursor()
        query = "DELETE FROM share WHERE date=%s"
        value = (self.date.get(),)
        my_cursor.execute(query, value)
        conn.commit()
        conn.close()
        self.fetch_share()
        messagebox.showinfo("Delete", "Deleted successfully")

    def add(self):
        if self.hari.get() == "" or self.rijan.get() == "" or self.anita.get() == "" or self.rishav.get() == "":
            messagebox.showerror("Error", "Enter Share Value for all members")
        elif self.date.get() == "":
            messagebox.showerror("Error", "Enter Date")
        else:
            total_value = float(self.hari.get()) + float(self.rijan.get()) + float(self.anita.get()) + float(self.rishav.get())
            self.display_share()

            self.textarea.insert(END, f"\n\tHari\t\t\t{self.hari.get()}\n\tRijan\t\t\t{self.rijan.get()}\n"
                                     f"\tAnita\t\t\t{self.anita.get()}\n\tRishav\t\t\t{self.rishav.get()}\n"
                                     f"_______________________________________________"
                                     f"\n\tTotal\t\t\t{"%.2f"%total_value}\n"
                                     f"_______________________________________________\n")

    def save(self):
        op=messagebox.askyesno("Save Share","Do you want to save the Share?")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('share/'+str(self.date.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Date:{self.date.get()} saved successfully")
            self.forshare()
            f1.close()
            self.fetch_share()

    def find_bill(self):
        found = "no"
        for filename in os.listdir("share"):
            if filename.split('.')[0]==(self.search_bill.get()):
                with open(os.path.join("share", filename), 'r') as f1:
                    bill_data = f1.read()
                    self.textarea.delete(1.0, END)
                    self.textarea.insert(END, bill_data)
                found = "yes"
                break
        if found == 'no':
            messagebox.showerror("Error", "Invalid share No.")

    def clear(self):
        op=messagebox.askyesno("Clear Share","Do you want to Clear all?")
        if op>0:
            self.textarea.delete(1.0,END)
            self.date.set("")
            self.hari.set("")
            self.rijan.set("")
            self.anita.set("")
            self.rishav.set("")
            self.search_bill.set("")
            self.date.set("")
            self.display_share()

    def display_share(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,f"\n Date:{self.date.get()}")

        self.textarea.insert(END,"\n_______________________________________________")
        self.textarea.insert(END,f"\n\tNames\t\t\tAmount")
        self.textarea.insert(END,"\n_______________________________________________")


    # ==========================================Chart=========================================
   

    def LineGraph(self):
        
        self.date = StringVar()
        self.hari = DoubleVar()
        self.rijan = DoubleVar()
        self.anita = DoubleVar()
        self.rishav = DoubleVar()
        self.total_value = DoubleVar()
        self.fetch_share()

        graph_Frame = Frame(self.root, relief=GROOVE, bg="white")
        graph_Frame.place(x=180, y=0, width=1186, height=556)

        # Connect to the database using SQLAlchemy
        engine = create_engine('mysql+mysqlconnector://root:root@localhost/share_data')
        query = "SELECT date, total_amount FROM share"
        dataframe = pd.read_sql_query(query, engine)

        figure = plt.Figure(figsize=(13, 7), dpi=100)
        figure_plot = figure.add_subplot(1, 1, 1)
        figure_plot.set_xlabel("Date")
        figure_plot.set_ylabel("Total Amount")

        line_graph = FigureCanvasTkAgg(figure, graph_Frame)
        line_graph.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        dataframe.plot(kind="line", x="date", y="total_amount", legend=True, ax=figure_plot, color='r', marker='o', fontsize=10)
        figure_plot.set_title('Date vs. Total Amount')

        #Button
        self.btnback = Button(graph_Frame, text="⬅", command=self.share, height=50, font=('arial', 15, 'bold'), bg="#4f5c8b", fg="white", width=120, cursor="hand2")
        self.btnback.place(x=10, y=10, width=20, height=20)


if __name__ == "__main__":
    root = Tk()
    obj = sharedata(root)
    obj = sharedata(root)
    obj.fetch_data()
    obj.fetch_share()
    root.mainloop()

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import ctypes
import os
import share_data as sharedata

myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class firstpage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x680+780+195")
        self.root.title("Share Data")
        self.root.resizable(0, 0)
        img = PhotoImage(file='image/RJNnobg.png')
        root.iconphoto(False, img)
        self.fp()


        #initializing
        self.firstpage_obj = sharedata()


        new_window = Toplevel(self.login)
        self.firstpage_obj.sharedata(new_window)

        
    def fp(self):
        #frame
        firstpage_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="#9FA8B2")
        firstpage_Frame.place(x=0, y=0, width=700, height=680)


        #image
        loginimg = Image.open("image/RJNnobg.png")
        loginimg = loginimg.resize((80, 80))
        self.photologinimg = ImageTk.PhotoImage(loginimg)

        lbl_loginimg = Label(firstpage_Frame, image=self.photologinimg, bg="#9FA8B2")
        lbl_loginimg.place(x=300, y=10, width=80, height=80)

        

        #button
        self.btnforlogin = Button(firstpage_Frame, text="login", height=50, command=self.login, font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#FFFFFF", width=120, cursor="hand2")
        self.btnforlogin.place(x=276, y=150, width=130, height=44)

        #button2
        self.btnforsignup = Button(firstpage_Frame, text="signup", command=self.signup, height=50, font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#FFFFFF", width=120, cursor="hand2")
        self.btnforsignup.place(x=276, y=250, width=130, height=44)

        

    def login(self):
        login_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="#9FA8B2")
        login_Frame.place(x=0, y=0, width=700, height=680)

        #image
        signupimg = Image.open("image/RJNnobg.png")
        signupimg = signupimg.resize((80, 80))
        self.photosignupimg = ImageTk.PhotoImage(signupimg)

        lbl_signupimg = Label(login_Frame, image=self.photosignupimg, bg="#9FA8B2")
        lbl_signupimg.place(x=300, y=10, width=80, height=80)

        self.btnback = Button(login_Frame, text="<", command=self.fp, height=50, font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#FFFFFF", width=120, cursor="hand2")
        self.btnback.place(x=10, y=10, width=30, height=24)

        #username
        self.lblusername = Label(login_Frame, text="username", font=("arial", 18, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lblusername.place(x=277, y=120)

        self.txtusername = ttk.Entry(login_Frame, font=("arial", 16, "bold"), width=24)
        self.txtusername.place(x=195, y=160)


        #username
        self.lblpassword = Label(login_Frame, text="password", font=("arial", 18, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lblpassword.place(x=277, y=220)

        self.txtpassword = ttk.Entry(login_Frame, font=("arial", 16, "bold"), width=24)
        self.txtpassword.place(x=195, y=260)


        #button
        self.btnlogin = Button(login_Frame, text="login", height=50, font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#FFFFFF", width=120, cursor="hand2")
        self.btnlogin.place(x=276, y=350, width=130, height=44)



        # ===============================================================signup==============================================================

    def signup(self):

        signup_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="#9FA8B2")
        signup_Frame.place(x=0, y=0, width=700, height=680)

        #image
        img2 = Image.open("image/RJNnobg.png")
        img2 = img2.resize((80, 80))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_img2 = Label(signup_Frame, image=self.photoimg2, bg="#9FA8B2")
        lbl_img2.place(x=300, y=10, width=80, height=80)

        self.btnback = Button(signup_Frame, text="<", command=self.fp, height=50, font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#FFFFFF", width=120, cursor="hand2")
        self.btnback.place(x=10, y=10, width=30, height=24)

        #username
        self.lblusername = Label(signup_Frame, text="username", font=("arial", 18, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lblusername.place(x=277, y=120)

        self.txtusername = ttk.Entry(signup_Frame, font=("arial", 16, "bold"), width=24)
        self.txtusername.place(x=195, y=160)


        #username
        self.lblpassword = Label(signup_Frame, text="password", font=("arial", 18, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lblpassword.place(x=277, y=220)

        #login
        self.txtpassword = ttk.Entry(signup_Frame, font=("arial", 16, "bold"), width=24)
        self.txtpassword.place(x=195, y=260)

        #username
        self.lblconfrimpassword = Label(signup_Frame, text="confrim password", font=("arial", 18, "bold"), bg="#9FA8B2",fg="#FFFFFF", bd=4)
        self.lblconfrimpassword.place(x=237, y=320)

        self.txtconfrimpassword = ttk.Entry(signup_Frame, font=("arial", 16, "bold"), width=24)
        self.txtconfrimpassword.place(x=195, y=360)


        #button
        self.btnlogin = Button(signup_Frame, text="Sign up", height=50, font=('arial', 15, 'bold'), bg="#4f5c8b", fg="#FFFFFF", width=120, cursor="hand2")
        self.btnlogin.place(x=276, y=450, width=130, height=44)


       
if __name__ == "__main__":
    root = Tk()
    obj = firstpage(root)
    root.mainloop()

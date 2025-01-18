from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import os
from employee import Employee
from train import train
from face_recognition import Facerecognition
from records import record
from about_us import about
from help import help
import tkinter
class facerec:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognizer")

        
        root.configure(bg="black")
        root.grid_rowconfigure(0,weight=1)
        root.grid_columnconfigure(0,weight=1)

        msg= Label(root, text="Human Face Recognition System For Security",bg="black", fg="White",width=50,height=3,font=('times',35,'italic bold '))
        msg.place(x=-10,y=-50)

        img1=Image.open(r"C:\Users\Lenovo\Desktop\FY project\face\tk images\employee.jpg")
        img1=img1.resize((180,180),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(root,image=self.photoimg1,command=self.employeedetails,cursor="hand2")
        b1.place(x=50,y=100,width=180,height=180)

        b1_1=Button(root,text="Employee Details",command=self.employeedetails,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="green")
        b1_1.place(x=50,y=274,width=180,height=30)



        img2=Image.open(r"C:\Users\Lenovo\Desktop\FY project\face\tk images\facerecognition.jpg")
        img2=img2.resize((180,180),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2=Button(root,command=self.facedata,image=self.photoimg2,cursor="hand2")
        b2.place(x=350,y=100,width=180,height=180)

        b2_1=Button(root,command=self.facedata,text="Recognize Faces",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="green")
        b2_1.place(x=350,y=274,width=180,height=30)



        img3=Image.open(r"C:\Users\Lenovo\Desktop\FY project\face\tk images\record.jpg")
        img3=img3.resize((180,180),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b3=Button(root,image=self.photoimg3,command=self.entryrecord,cursor="hand2")
        b3.place(x=650,y=100,width=180,height=180)

        b3_1=Button(root,text="Records",command=self.entryrecord,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="green")
        b3_1.place(x=650,y=274,width=180,height=30)


        img4=Image.open(r"C:\Users\Lenovo\Desktop\FY project\face\tk images\train.jpg")
        img4=img4.resize((180,180),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b4=Button(root,command=self.traindata,image=self.photoimg4,cursor="hand2")
        b4.place(x=950,y=100,width=180,height=180)

        b4_1=Button(root,command=self.traindata,text="Train Model",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="green")
        b4_1.place(x=950,y=274,width=180,height=30)


        img5=Image.open(r"C:\Users\Lenovo\Desktop\FY project\face\tk images\photos.jpg")
        img5=img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b5=Button(root,image=self.photoimg5,command=self.openimg,cursor="hand2")
        b5.place(x=50,y=380,width=180,height=180)

        b5_1=Button(root,text="Photos",command=self.openimg,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="green")
        b5_1.place(x=50,y=550,width=180,height=30)


        img6=Image.open(r"C:\Users\Lenovo\Desktop\FY project\face\tk images\about us.jpg")
        img6=img6.resize((180,180),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b6=Button(root,command=self.about,image=self.photoimg6,cursor="hand2")
        b6.place(x=350,y=380,width=180,height=180)

        b6_1=Button(root,command=self.about,text="About Us",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="green")
        b6_1.place(x=350,y=550,width=180,height=30)



        img7=Image.open(r"C:\Users\Lenovo\Desktop\FY project\face\tk images\help.jpg")
        img7=img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b7=Button(root,command=self.help,image=self.photoimg7,cursor="hand2")
        b7.place(x=650,y=380,width=180,height=180)

        b7_1=Button(root,command=self.help,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="green")
        b7_1.place(x=650,y=550,width=180,height=30)


        img8=Image.open(r"C:\Users\Lenovo\Desktop\FY project\face\tk images\exit.jpg")
        img8=img8.resize((180,180),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b8=Button(root,image=self.photoimg8,command=self.exit,cursor="hand2")
        b8.place(x=950,y=380,width=180,height=180)

        b8_1=Button(root,text="Exit",command=self.exit,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="green")
        b8_1.place(x=950,y=550,width=180,height=30)

    def employeedetails(self):
        self.new_window=Toplevel(self.root)
        self.app=Employee(self.new_window)

    def facedata(self):
        self.new_window=Toplevel(self.root)
        self.app=Facerecognition(self.new_window)

    def traindata(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)
    
    def openimg(self):
        os.startfile("dataset")

    def entryrecord(self):
        self.new_window=Toplevel(self.root)
        self.app=record(self.new_window)

    def about(self):
        self.new_window=Toplevel(self.root)
        self.app=about(self.new_window)

    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=help(self.new_window)
    
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Quit","Do you want to quit?",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return
        self.new_window=Toplevel(self.root)
        self.app=help(self.new_window)


if __name__=="__main__":
    root=Tk()
    o=facerec(root)
    root.mainloop()

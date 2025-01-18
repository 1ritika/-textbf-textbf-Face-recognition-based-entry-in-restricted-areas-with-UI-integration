from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import cv2

class about:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognizer")

        bimg=Image.open(r"tk images\aboutusbg.jpg")
        bimg=bimg.resize((1520,700),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(bimg)

        bgimg=Label(self.root,image=self.photoimg)
        bgimg.place(x=-100,y=0,width=1500,height=700)

        msg=Label(bgimg, text="About Us",bg="sky blue", fg="red",width=50,height=3,font=('times',35,'bold underline'))
        msg.place(x=0,y=0,width=1400,height=56)

        #main_frame=Frame(self.root,bd=2)
        #main_frame.place(x=20,y=60,width=1000,height=130)

        dev1=Label(self.root,text="Developed By: Ritika Patel(1721BEEC30031)",font=('times new roman',15,' bold '))
        dev1.place(x=50,y=60)

        dev2=Label(self.root,text="Krina Patel(1721BEEC30026)",font=('times new roman',15,' bold '))
        dev2.place(x=178,y=89)
if __name__=="__main__":
    root=Tk()
    o=about(root)
    root.mainloop()
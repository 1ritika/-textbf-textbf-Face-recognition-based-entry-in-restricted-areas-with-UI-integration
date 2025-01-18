from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import cv2

class help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Desk")

        bimg=Image.open(r"tk images\helpbg.jpg")
        bimg=bimg.resize((1280,700),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(bimg)

        bgimg=Label(self.root,image=self.photoimg)
        bgimg.place(x=-100,y=0,width=1500,height=700)

        contact=Label(self.root,text="Contact Us at facialrecog@deepleaning.com",font=('times new roman',20,' bold '),bg="white")
        contact.place(x=430,y=80)
if __name__=="__main__":
    root=Tk()
    o=help(root)
    root.mainloop()
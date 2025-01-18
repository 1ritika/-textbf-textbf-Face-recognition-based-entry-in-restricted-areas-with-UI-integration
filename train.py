from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import cv2
import os
import numpy as np

class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognizer")
    

        bimg=Image.open(r"tk images\trainbg.jpg")
        bimg=bimg.resize((1530,700),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(bimg)

        bgimg=Label(self.root,image=self.photoimg)
        bgimg.place(x=0,y=0,width=1530,height=710)

        msg=Label(bgimg, text="Train Face Recognition Model",bg="sky blue", fg="red",width=50,height=3,font=('times',35,'bold '))
        msg.place(x=0,y=0,width=1400,height=56)

        trainbtn=Button(bgimg,command=self.trainclassifier,text="Train model",cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white",width=40,height=2)
        trainbtn.place(x=380,y=508)

    def trainclassifier(self):
        datadir=("dataset")
        path=[os.path.join(datadir,file) for file in os.listdir(datadir)]

        faces=[]
        ids=[]

        for img in path:
            i=Image.open(img).convert("L") #grayscaleimg
            imagenp=np.array(i,'uint8')
            id=int(os.path.split(img)[1].split('.')[1])

            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training Dataset",imagenp)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        #train and save
        cl=cv2.face.LBPHFaceRecognizer_create()
        cl.train(faces,ids)
        cl.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Classifier successfully trained!!")



if __name__=="__main__":
    root=Tk()
    o=train(root)
    root.mainloop()
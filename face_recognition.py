from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import pyttsx3

class Facerecognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognizer")

        bimg=Image.open(r"tk images\face.jpg")
        bimg=bimg.resize((1530,700),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(bimg)

        bgimg=Label(self.root,image=self.photoimg)
        bgimg.place(x=0,y=0,width=1530,height=710)

        msg=Label(bgimg, text="Recognize Faces",bg="white", fg="green",width=60,height=3,font=('times',35,'bold '))
        msg.place(x=0,y=0,width=1350,height=56)

        detectbtn=Button(bgimg,command=self.recognizeface,text="Start Recognizing",cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white",width=40,height=2)
        detectbtn.place(x=80,y=350)
        

    #entry log
    def recordentry(self,i,n,d):
        global no
        with open("Entry Log.csv","r+",newline="\n") as f:
            datalist=f.readlines()
            namelist=[]
            for l in datalist:
               entry=l.split((","))
            namelist.append(entry[0])
            if (n not in namelist) and (i not in namelist) and (d not in namelist):

                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dt=now.strftime("%H:%M:%S")
                f.writelines(f"{n},{i},{d},{d1},{dt}\n")
                no=n
    def text_to_speech(self, user_text):
            engine = pyttsx3.init()
            engine.say(user_text)
            engine.runAndWait()
    


    def recognizeface(self):
        def drawrec(img,classifier,scalef,minneigh,color,text,cls):
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            feature=classifier.detectMultiScale(gray,scalef,minneigh)

            cord=[]

            for (x,y,w,h) in feature:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=cls.predict(gray[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                con=mysql.connector.connect(host="localhost",username="root",password="Ilovemysql",database="face recognition")
                crsr=con.cursor()
                crsr.execute("select Name from employee where ID="+str(id))
                n=crsr.fetchone()
                n="+".join(n)
                crsr.execute("select ID from employee where ID="+str(id))
                i=crsr.fetchone()
                i="+".join(i)

                crsr.execute("select Department from employee where ID="+str(id))
                d=crsr.fetchone()
                d="+".join(d)
                


                if confidence>70:
                    
                    cv2.putText(img,f"{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.recordentry(i,n,d)
                    self.text_to_speech("Welcome" + n)
                    
                    self.text_to_speech("Opening the gate")

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"UNKNOWN!!",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.text_to_speech("I am sorry, I don't know you!")
                    print("Intruder!!!!")

                cord=[x,y,w,h]
            return cord
        
        def recognize(img,cls,faceCascade):
            cord=drawrec(img,faceCascade,1.1,10,(255,25,255),"Face",cls)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        cls=cv2.face.LBPHFaceRecognizer_create()
        cls.read("classifier.xml")

        cap=cv2.VideoCapture(0)

        while True:
            ret,frame=cap.read()
            frame=recognize(frame,cls,faceCascade)
            cv2.imshow("Welcome to face recognition!",frame)

            if cv2.waitKey(1)==13:
                break
        cap.release()
        cv2.destroyAllWindows()
        
        

if __name__=="__main__":
    root=Tk()
    o=Facerecognition(root)
    root.mainloop()
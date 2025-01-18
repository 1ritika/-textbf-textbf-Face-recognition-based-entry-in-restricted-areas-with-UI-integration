from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import cv2

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognizer")

        #variables
        self.name=StringVar()
        self.id=StringVar()
        self.dep=StringVar()
        self.dob=StringVar()
        self.gender=StringVar()
        self.mob=StringVar()
        self.email=StringVar()

        root.configure(bg="black")
        root.grid_rowconfigure(0,weight=1)
        root.grid_columnconfigure(0,weight=1)

        msg= Label(root, text="Employee Details Manager",bg="black", fg="White",width=50,height=3,font=('times new roman',35,' bold '))
        msg.place(x=0,y=0,width=1230,height=50)

        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=20,y=55,width=1250,height=630)

        lframe=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details",font=('times new roman',25,' bold '))
        lframe.place(x=5,y=5,width=500,height=600)

        searchf=LabelFrame(lframe,bd=2,bg="white",relief=RIDGE,text="Search Database",font=('times new roman',18,' bold '))
        searchf.place(x=5,y=0,width=480,height=155)

        searchl=Label(searchf,text="Search By:",font=('times new roman',15,' bold '),bg="white")
        searchl.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        searchcombo=ttk.Combobox(searchf,width=20,font=('times new roman',13,' bold '),state="readonly")
        searchcombo["values"]=("Select","Employee ID","Mobile No.","Name")
        searchcombo.current(0)
        searchcombo.grid(row=0,column=1,padx=0,pady=10,sticky=W)

        searchentry=ttk.Entry(searchf,width=22,font=('times new roman',13,' bold '))
        searchentry.grid(row=1,column=1,padx=0,pady=10,sticky=W)

        searchbtn=Button(searchf,text="Search",cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white",width=12)
        searchbtn.grid(row=2,column=0,padx=20)

        showallbtn=Button(searchf,text="Show All",cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white",width=12)
        showallbtn.grid(row=2,column=1,padx=3)


        newf=LabelFrame(lframe,bd=2,bg="white",relief=RIDGE,text="Add New Employee",font=('times new roman',18,' bold '))
        newf.place(x=5,y=155,width=480,height=400)

        deplabel=Label(newf,text="Department:",font=('times new roman',13,' bold '),bg="white")
        deplabel.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        newcombo=ttk.Combobox(newf,width=20,textvariable=self.dep,font=('times new roman',12,' bold '),state="readonly")
        newcombo["values"]=("Select Department","Human Resources","Sales","Finance","Project Management")
        newcombo.current(0)
        newcombo.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        namelabel=Label(newf,text="Name:",font=('times new roman',13,' bold '),bg="white")
        namelabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        nameentry=Entry(newf,width=22,textvariable=self.name,font=('times new roman',12,' bold '))
        nameentry.grid(row=1,column=1,padx=10,sticky=W)

        employeeidlabel=Label(newf,text="Employee ID:",font=('times new roman',13,' bold '),bg="white")
        employeeidlabel.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        identry=Entry(newf,width=22,textvariable=self.id,font=('times new roman',12,' bold '))
        identry.grid(row=2,column=1,padx=10,sticky=W)

        doblabel=Label(newf,text="D.O.B.:",font=('times new roman',13,' bold '),bg="white")
        doblabel.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        dobentry=Entry(newf,width=22,textvariable=self.dob,font=('times new roman',12,' bold '))
        dobentry.grid(row=3,column=1,padx=10,sticky=W)

        genderlabel=Label(newf,text="Gender:",font=('times new roman',13,' bold '),bg="white")
        genderlabel.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        gendercombo=ttk.Combobox(newf,width=20,textvariable=self.gender,font=('times new roman',12,' bold '),state="readonly")
        gendercombo["values"]=("Select","Male","Female","Other","Prefer not to say")
        gendercombo.current(0)
        gendercombo.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        Mobilenolabel=Label(newf,text="Mobile No.:",font=('times new roman',13,' bold '),bg="white")
        Mobilenolabel.grid(row=5,column=0,padx=10,pady=5,sticky=W)

        mobilenoentry=Entry(newf,width=22,textvariable=self.mob,font=('times new roman',12,' bold '))
        mobilenoentry.grid(row=5,column=1,padx=10,sticky=W)

        emaillabel=Label(newf,text="Email ID:",font=('times new roman',13,' bold '),bg="white")
        emaillabel.grid(row=6,column=0,padx=10,pady=5,sticky=W)

        emailentry=Entry(newf,width=22,textvariable=self.email,font=('times new roman',12,' bold '))
        emailentry.grid(row=6,column=1,padx=10,sticky=W)

       

        self.radio1=StringVar()

        radiobtn1=ttk.Radiobutton(newf,variable=self.radio1,text="Take Photos",value="Yes")
        radiobtn1.grid(row=7,column=0)

        radiobtn2=ttk.Radiobutton(newf,variable=self.radio1,text="No Photo samples",value="No")
        radiobtn2.grid(row=7,column=1)

        #button labels
        btnf=LabelFrame(lframe,bd=2,bg="white",relief=RIDGE,font=('times new roman',18,' bold '))
        btnf.place(x=10,y=472,width=470,height=82)

        savebtn=Button(btnf,text="Save",command=self.addata,cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white",width=10)
        savebtn.grid(row=0,column=1,padx=3,pady=5)

        updatebtn=Button(btnf,text="Update",command=self.updatedata,cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white",width=10)
        updatebtn.grid(row=0,column=2,padx=3,pady=5)

        deletebtn=Button(btnf,text="Delete",command=self.deletedata,cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white",width=10)
        deletebtn.grid(row=0,column=3,padx=3,pady=5)

        clearbtn=Button(btnf,text="Clear",command=self.cleardata,cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white",width=10)
        clearbtn.grid(row=0,column=4,padx=3,pady=5)

        takephotobtn=Button(btnf,text="Take Photos",command=self.generate,cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white",width=10)
        takephotobtn.grid(row=2,column=1,padx=10)

        updatephotobtn=Button(btnf,text="Update Photos",cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white",width=10)
        updatephotobtn.grid(row=2,column=2,padx=10)

        #right frame
        rframe=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details",font=('times new roman',25,' bold '))
        rframe.place(x=520,y=5,width=720,height=600)

        scrollx=ttk.Scrollbar(rframe,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(rframe,orient=VERTICAL)

        self.employeetable=ttk.Treeview(rframe,column=("Name","Employee ID","Dep","D.O.B.","Gender","Mobile No.","Email","phsample"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.employeetable.xview)
        scrolly.config(command=self.employeetable.yview)

        self.employeetable.heading("Name",text="Name")
        self.employeetable.heading("Employee ID",text="Employee ID")
        self.employeetable.heading("Dep",text="Department")
        self.employeetable.heading("Gender",text="Gender")
        self.employeetable.heading("Mobile No.",text="Mobile No.")
        self.employeetable.heading("D.O.B.",text="D.O.B.")
        self.employeetable.heading("Email",text="Email ID")
        self.employeetable.heading("phsample",text="Photo Samples")

        self.employeetable["show"]="headings"


        self.employeetable.column("Dep",width=100)
        self.employeetable.column("Employee ID",width=100)
        self.employeetable.column("Name",width=100)
        self.employeetable.column("Mobile No.",width=100)
        self.employeetable.column("D.O.B.",width=100)
        self.employeetable.column("Gender",width=100)

        self.employeetable.pack(fill=BOTH,expand=1)
        self.employeetable.bind("<ButtonRelease>",self.getcrsr)
        self.fetchdata()
        

    #get data
    def addata(self):
        if self.dep.get()=="Select Department" or self.name.get()=="" or self.id=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host="localhost",username="root",password="Ilovemysql",database="face recognition")
                crsr=con.cursor()
                crsr.execute("INSERT INTO Employee values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.name.get(),
                                                                            self.id.get(),
                                                                            self.dep.get(),
                                                                            self.dob.get(),
                                                                            self.gender.get(),
                                                                            self.mob.get(),
                                                                            self.email.get(),
                                                                            self.radio1.get()
                                                                                    ))
                con.commit()
                self.fetchdata()
                con.close()
                messagebox.showinfo("Success","Employee details have been added",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to :{str(e)}",parent=self.root)
    #fetch data
    def fetchdata(self):
        con=mysql.connector.connect(host="localhost",username="root",password="Ilovemysql",database="face recognition")
        crsr=con.cursor()
        crsr.execute("select * from employee")
        data=crsr.fetchall()

        if len(data)!=0:
            self.employeetable.delete(*self.employeetable.get_children())
            for i in data:
                self.employeetable.insert("",END,values=i)
            con.commit()
        con.close()
    #get cursor
    def getcrsr(self,event=""):
        cfocus=self.employeetable.focus()
        content=self.employeetable.item(cfocus)
        data=content["values"]

        self.name.set(data[0])
        self.id.set(data[1])
        self.dep.set(data[2])
        self.dob.set(data[3])
        self.gender.set(data[4])
        self.mob.set(data[5])
        self.email.set(data[6])
        self.radio1.set(data[7])
    
    #update data
    def updatedata(self):
        if self.dep.get()=="Select Department" or self.name.get()=="" or self.id=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this employee's details?",parent=self.root)
                if update>0:
                    con=mysql.connector.connect(host="localhost",username="root",password="Ilovemysql",database="face recognition")
                    crsr=con.cursor()
                    crsr.execute("update employee set Name=%s,Department=%s,DOB=%s,Gender=%s,MobileNo=%s,Email=%s,PhotoSamples=%s where (ID=%s)",(
                                                                                                                                                        self.name.get(),
                                                                                                                                                        self.dep.get(),
                                                                                                                                                        self.dob.get(),
                                                                                                                                                        self.gender.get(),
                                                                                                                                                        self.mob.get(),
                                                                                                                                                        self.email.get(),
                                                                                                                                                        self.radio1.get(),
                                                                                                                                                        self.id.get()
                                                                                                                                                     ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Employee details successfully updated!",parent=self.root)
                con.commit()
                self.fetchdata()
                con.close()
            except Exception as e:
                messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)
    #delete data
    def deletedata(self):
        if self.id.get()=="":
            messagebox.showerror("Error","Employee ID required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete this employee's details?",parent=self.root)
                if delete>0:
                    con=mysql.connector.connect(host="localhost",username="root",password="Ilovemysql",database="face recognition")
                    crsr=con.cursor()
                    sql="delete * from employee where id=%s"
                    val=(self.id.get(),)
                    crsr.execute(sql,val)
                else:
                    if not delete:
                        return
                con.commit()
                self.fetchdata()
                con.close()
                messagebox.showinfo("Success","Successfully deleted!",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)
    #clear
    def cleardata(self):
        self.name.set("")
        self.id.set("")
        self.dep.set("Select Department")
        self.dob.set("")
        self.gender.set("Select")
        self.mob.set("")
        self.email.set("")
        self.radio1.set("")
    
    #generate dataset
    def generate(self):
        if self.dep.get()=="Select Department" or self.name.get()=="" or self.id=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host="localhost",username="root",password="Ilovemysql",database="face recognition")
                crsr=con.cursor()
                crsr.execute(f"select * from employee where ID={self.id.get()}")
                res=crsr.fetchall()
                eid=self.id.get()
                print(eid)
                crsr.execute("update employee set Name=%s,Department=%s,DOB=%s,Gender=%s,MobileNo=%s,Email=%s,PhotoSamples=%s where (ID=%s)",(
                                                                                                                                                        self.name.get(),
                                                                                                                                                        self.dep.get(),
                                                                                                                                                        self.dob.get(),
                                                                                                                                                        self.gender.get(),
                                                                                                                                                        self.mob.get(),
                                                                                                                                                        self.email.get(),
                                                                                                                                                        self.radio1.get(),
                                                                                                                                                        self.id.get(),
                                                                                                                                                     ))
                con.commit()
                self.fetchdata()
                self.cleardata()
                con.close()
                #load classifier
                face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                def crop(img):
                    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

                    for (x, y, w, h) in faces:
    	                #print(x,y,w,h)
    	                crop= img[y:y+h, x:x+w] #(ycord_start, ycord_end)
    	                return crop

                cap = cv2.VideoCapture(0)
                img_id=0

                while True:
                # Capture frame-by-frame
                    ret, frame = cap.read()
                    if crop(frame) is not None:
                        img_id+=1
                        face=cv2.resize(crop(frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        filepath="dataset/user."+str(eid)+"."+str(img_id)+".jpg"
                        cv2.imwrite(filepath,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped image",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Dataset generated successfully!")
            except Exception as e:
                messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)
            








if __name__=="__main__":
    root=Tk()
    o=Employee(root)
    root.mainloop()

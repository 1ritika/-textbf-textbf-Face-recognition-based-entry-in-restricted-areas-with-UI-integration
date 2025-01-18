from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import cv2
import os
from tkinter import filedialog
import csv

data=[]

class record:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognizer")
    
        root.configure(bg="black")
        root.grid_rowconfigure(0,weight=1)
        root.grid_columnconfigure(0,weight=1)

        self.name=StringVar()
        self.id=StringVar()
        self.dep=StringVar()
        self.date=StringVar()
        self.time=StringVar()
        

        msg= Label(root, text="Entry Records Manager",bg="black", fg="White",width=50,height=3,font=('times new roman',35,' bold '))
        msg.place(x=0,y=0,width=1230,height=50)

        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=20,y=55,width=1250,height=630)

        lframe=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Employee Details",font=('times new roman',25,' bold '))
        lframe.place(x=5,y=5,width=450,height=590)

        namelabel=Label(lframe,text="Name:",font=('times new roman',15,' bold '),bg="white")
        namelabel.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        nameentry=Entry(lframe,width=22,textvariable=self.name,font=('times new roman',14,' bold '))
        nameentry.grid(row=0,column=1,padx=10,sticky=W)

        employeeidlabel=Label(lframe,text="Employee ID:",font=('times new roman',15,' bold '),bg="white")
        employeeidlabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        identry=Entry(lframe,width=22,textvariable=self.id,font=('times new roman',14,' bold '))
        identry.grid(row=1,column=1,padx=10,sticky=W)

        deplabel=Label(lframe,text="Department:",font=('times new roman',15,' bold '),bg="white")
        deplabel.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        newcombo=ttk.Combobox(lframe,width=20,textvariable=self.dep,font=('times new roman',14,' bold '),state="readonly")
        newcombo["values"]=("Select Department","Human Resources","Sales","Finance","Project Management")
        newcombo.current(0)
        newcombo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        datelabel=Label(lframe,text="Date:",font=('times new roman',15,' bold '),bg="white")
        datelabel.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        dateentry=Entry(lframe,width=22,textvariable=self.date,font=('times new roman',14,' bold '))
        dateentry.grid(row=3,column=1,padx=10,sticky=W)

        timelabel=Label(lframe,text="Time:",font=('times new roman',15,' bold '),bg="white")
        timelabel.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        timeentry=Entry(lframe,textvariable=self.time,width=22,font=('times new roman',14,' bold '))
        timeentry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #button labels
        btnf=LabelFrame(lframe,bd=2,bg="white",relief=RIDGE,font=('times new roman',18,' bold '))
        btnf.place(x=10,y=252,width=430,height=90)

        importbtn=Button(btnf,command=self.importcsv,text="Import csv",cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white",width=17)
        importbtn.grid(row=0,column=0,padx=10,pady=5)

        exportbtn=Button(btnf,command=self.exportcsv,text="Export csv",cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white",width=17)
        exportbtn.grid(row=0,column=2,padx=10,pady=5)

        updatebtn=Button(btnf,text="Update",cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white",width=17)
        updatebtn.grid(row=1,column=0,padx=10,pady=5)

        clearbtn=Button(btnf,command=self.clear,text="Clear",cursor="hand2",font=("times new roman",12,"bold"),bg="blue",fg="white",width=17)
        clearbtn.grid(row=1,column=2,padx=10,pady=5)




        rframe=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Entry Details",font=('times new roman',25,' bold '))
        rframe.place(x=468,y=5,width=770,height=600)

        scrollx=ttk.Scrollbar(rframe,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(rframe,orient=VERTICAL)

        self.entrytable=ttk.Treeview(rframe,column=("Name","Employee ID","Dep","Date","Time"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.entrytable.xview)
        scrolly.config(command=self.entrytable.yview)

        self.entrytable.heading("Name",text="Name")
        self.entrytable.heading("Employee ID",text="Employee ID")
        self.entrytable.heading("Dep",text="Department")
        self.entrytable.heading("Date",text="Date")
        self.entrytable.heading("Time",text="Time")
        

        self.entrytable["show"]="headings"


        self.entrytable.column("Dep",width=100)
        self.entrytable.column("Employee ID",width=100)
        self.entrytable.column("Name",width=100)
        self.entrytable.column("Date",width=100)
        self.entrytable.column("Time",width=100)

        self.entrytable.pack(fill=BOTH,expand=1)
        self.entrytable.bind("<ButtonRelease>",self.getcrsr)

    def fetchdata(self,rows):
        self.entrytable.delete(*self.entrytable.get_children())
        for i in rows:
            self.entrytable.insert("",END,values=i)
        
    def importcsv(self):
        global data
        data.clear()
        fl=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fl) as f:
            csvdata=csv.reader(f,delimiter=",")
            for i in csvdata:
                data.append(i)
            self.fetchdata(data)

    def exportcsv(self):
        try:
            if len(data)<1:
                messagebox.showerror("Error","No data found to export!",parent=self.root)
                return False
            fl=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fl,mode="w",newline="") as f:
                rite=csv.writer(f,delimiter=",")
                for i in data:
                    rite.writerow(i)
                messagebox.showinfo("Success","Data Successfully exported to "+os.path.basename(fl)+"!",parent=self.root)
        except Exception as e:
                messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)

    def getcrsr(self,event=""):
        crsr=self.entrytable.focus()
        content=self.entrytable.item(crsr)
        row=content['values']
        self.name.set(row[0])
        self.id.set(row[1])
        self.dep.set(row[2])
        self.date.set(row[3])
        self.time.set(row[4])

    def clear(self):
        self.name.set("")
        self.id.set("")
        self.dep.set("")
        self.date.set("")
        self.time.set("")


if __name__=="__main__":
    root=Tk()
    o=record(root)
    root.mainloop()
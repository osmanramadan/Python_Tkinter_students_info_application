from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class designwindow:
    def __init__(self,root):
          # main of window
          self.root=root
          self.root.title("عثمان رمضان")
          self.root.geometry("1350x690+1+1")
          self.root.config(background="silver")
          # variables
          self.add=StringVar()
          self.gen=StringVar()
          self.cert=StringVar()
          self.ph=StringVar()
          self.ema=StringVar()
          self.name=StringVar()
          self.num=StringVar()
          self.delete=StringVar()
          self.intr_search=StringVar()
          self.select_search=StringVar()
          # frames
          # main label
          Label1=Label(self.root,text="نظام تسجيل الطلاب",font=("monospace",14,),fg="white",bg="blue")
          Label1.pack(fill=X)
          ###########################  the First frame ######################################
          frame1=Frame(self.root,background="white")
          frame1.place(x=1124,y=30,width=230,height=400)
          Label2=Label(frame1,text="الرقم التسلسلي")
          Label2.pack()
          en1=Entry(frame1,bd="3",textvariable=self.num)
          en1.pack()
          Label2=Label(frame1,text="اسم الطالب")
          Label2.pack()
          en2=Entry(frame1,bd="3",textvariable=self.name)
          en2.pack()
          Label3=Label(frame1,text="ايميل الطالب")
          Label3.pack()
          en3=Entry(frame1,bd="3",textvariable=self.ema)
          en3.pack()        
          Label4=Label(frame1,text="رقم الهاتف")
          Label4.pack()
          en4=Entry(frame1,bd="3",justify="center",textvariable=self.ph)
          en4.pack()
          Labelcert=Label(frame1,text="مؤهل الطالب")
          Labelcert.pack()
          encertrt=Entry(frame1,bd="3",justify="center",textvariable=self.cert)
          encertrt.pack()
          label5=Label(frame1,text="جنس الطالب")
          label5.pack()
          #/////////////////////////////////////////////////////
          combo_gender=ttk.Combobox(frame1,textvariable=self.gen)
          combo_gender['value']=("ذكر","انثي")
          combo_gender.pack()
          #////////////////////
          label6=Label(frame1,text="عنوان الطالب")
          label6.pack()
          en6=Entry(frame1,bd="3",textvariable=self.add)
          en6.pack()
          label7=Label(frame1,text="حذف الطالب")
          label7.pack()
          en7=Entry(frame1,bd="3",textvariable=self.delete)
          en7.pack()
          ###########################  the second frame #################################
          frame2=Frame(self.root)
          frame2.place(x=1124,y=465,width=230,height=230)    
          la1=Label(frame2,text="لوحة التحكم",font=("monoface",14),fg="white",background="blue")
          la1.pack(fill=X)
          ########################### Starting buttons   #################################
          bn1_del=Button(frame2,text="حذف الطالب",width=40,background="#2980B9",command=self.delete_id)
          bn1_del.pack()
          bn2_update=Button(frame2,text="تحديث البيانات",width=40,background="#2980B9",command=self.update)
          bn2_update.pack()
          bn3_empty=Button(frame2,text="افراغ الحقول",width=40,background="#2980B9",command=self.clear)
          bn3_empty.pack()
          bn4_aboutus=Button(frame2,text="من نحن ",width=40,background="#2980B9",command=self.about_us)
          bn4_aboutus.pack()
          bn5_exit=Button(frame2,text=" الخروج من البرنامج",width=40,background="#2980B9",command=root.quit)
          bn5_exit.pack()
          bn6_insert=Button(frame2,text="اضافة طالب",width=40,background="#2980B9" ,command=self.add_student)
          bn6_insert.pack()         
          ##############################  Searching frame    ###############################
          search_frame=Frame(self.root,background="white")
          search_frame.place(x=1,y=2,width=1140,height=100)
          search_label=Label(search_frame,text=": بالاسم البحث عن الطالب",font=("monospace",19),background="white")
          search_label.place(x=870,y=20,width=240,height=30)


          search_entry=Entry(search_frame,justify="center",bd=4,textvariable=self.intr_search)
          search_entry.place(x=610,y=23,height=35,width=150)
          but=Button(search_frame,text="بحث",bg="blue",fg="white",command=self.search)
          but.place(x=490,y=23,height=35,width=120)
          but=Button(search_frame,text="عرض بيانات الطلاب",bg="blue",fg="white",command=self.fetchelements)
          but.place(x=355,y=23,height=35,width=120)
          # details frame students data
          detail=Frame(self.root,bg="white")
          detail.place(x=1,y=110,width=1140,height=600)
          
          ###############################    Set up scroll   ############################
          scroll_x=Scrollbar(detail,orient=HORIZONTAL)
          scroll_y=Scrollbar(detail,orient=VERTICAL)

          ##############################     Treeview        ############################
          self.student_table=ttk.Treeview(detail,columns=("id","name","email","phone","certia","gender","address"),
          xscrollcommand=scroll_x,
          yscrollcommand=scroll_y)
          self.student_table.place(x=1,y=1,width=1130,height=600)
          scroll_x.pack(side=BOTTOM,fill=X)
          scroll_y.pack(side=LEFT,fill=Y)
          scroll_x.config(command=self.student_table.xview)
          scroll_y.config(command=self.student_table.yview)

          # the SHOW OF VIEWTREE 
          #  //////////////////////////////////////////  #/////////////////////   #///////////////////   #/////////
          self.student_table["show"]="headings"
          
          self.student_table.heading('id',text='رقم التسلسلي')
          self.student_table.heading('name',text='الاسم')
          self.student_table.heading('email',text='الاميل')
          self.student_table.heading('phone',text='رقم التلفون')
          self.student_table.heading('certia',text='المؤهل')
          self.student_table.heading('gender',text='الجنس') 
          self.student_table.heading('address',text='العنوان')
          self.student_table.column('address',width=161)
          self.student_table.column('gender',width=161)
          self.student_table.column('certia',width=161)
          self.student_table.column('phone',width=161)
          self.student_table.column('email',width=161)
          self.student_table.column('name',width=161)
          self.student_table.column('id',width=161)
          self.student_table.bind("<ButtonRelease-1>",self.curser_item)
          ######### calling the program    
          self.root.mainloop()
    def add_student(self):
            con=pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="enrol"
                    )
            cur=con.cursor()    
            cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(
              self.num.get(),
              self.name.get(),
              self.ema.get(),
              self.ph.get(),
              self.cert.get(),
              self.gen.get(),
              self.add.get()  ))
            con.commit()   
            self.fetchelements()
            con.close()
            
    def fetchelements(self):
        con=pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="enrol"
                  )
        cur=con.cursor()
        cur.execute("select * from student")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
              self.student_table.insert("",END,value=row)
            con.commit()
        con.close()
        
    def delete_id(self):
      con=pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="enrol"
      )
      cur=con.cursor()
      cur.execute("DELETE FROM `student` WHERE `student`.`id` =%s",self.delete.get())
      con.commit()
      self.fetchelements()
      con.close()
    def update(self):
      con=pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="enrol"
      )
      cur=con.cursor()
      cur.execute("update student set name=%s, email= %s, phone= %s, certia= %s, gender= %s, address=%s where id= %s",(
                  self.name.get(),
                  self.ema.get(),
                  self.ph.get(),
                  self.cert.get(),
                  self.gen.get(),
                  self.add.get(),
                  self.num.get()
      ))
      con.commit()
      self.fetchelements()
      con.close()
    def clear(self):
          self.add.set('')
          self.gen.set('')
          self.cert.set('')
          self.ph.set('')
          self.ema.set('')
          self.name.set('')
          self.num.set('')
    def about_us(self):
        messages=messagebox.showinfo("by osman mamdoh ramadan","the name of school")
    def search(self):
        con=pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="enrol"
      )
        cur=con.cursor()

        cur.execute("SELECT * FROM `student` WHERE `name` like %s",self.intr_search.get())
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
              self.student_table.insert("",END,values=row)           
            con.commit()
        con.close()

    def curser_item(self,jj):
        curser_row=self.student_table.focus()
        contents=self.student_table.item(curser_row)
        Row=contents['values']
        self.num.set(Row[0])
        self.name.set(Row[1])
        self.ema.set(Row[2])
        self.ph.set(Row[3])
        self.cert.set(Row[4])
        self.gen.set(Row[5])
        self.add.set(Row[6])

root=Tk()
designwindow(root)


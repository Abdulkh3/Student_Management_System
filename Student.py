from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Student():
    def __init__(self,window):
        self.window=window
        self.window.title('Student Management System')
        self.window.font = ('DM Sans', 30)
        self.window.geometry("1370x700+0+0")
        title= Label(self.window,text='Student Management System',
            foreground='White', background='black',font=("times new roman",40,"bold"),
              width=70, height=1,bd=9,relief='groove')
        title.pack(side=TOP,fill=X)


        #variables
        self.var_roll=StringVar()
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_dept=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()



        frm_a = Frame(self.window,bd=4,relief="ridge",bg="grey")
        frm_a.place(x=20,y=100,width=550,height=600)
        a_title=Label(frm_a,text='Manage Student',
              foreground='Black', background='White',font=("times new roman",25,"bold"))
        a_title.grid(row=0,columnspan=2,pady=20)


        lbl_roll = Label(frm_a, text='Roll Number', foreground='Black', background='White',font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_roll= Entry(frm_a,textvariable=self.var_roll,font=("times new roman",17,"bold"),bd=5,relief="groove")
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_firstname= Label(frm_a, text='First Name', foreground='Black', background='White',
                         font=("times new roman", 20, "bold"))
        lbl_firstname.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_firstname = Entry(frm_a,textvariable=self.var_fname, font=("times new roman", 17, "bold"), bd=5, relief="groove")
        txt_firstname.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_lastname = Label(frm_a, text='Last Name', foreground='Black', background='White',
                          font=("times new roman", 20, "bold"))
        lbl_lastname.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_lastname = Entry(frm_a,textvariable=self.var_lname, font=("times new roman", 17, "bold"), bd=5, relief="groove")
        txt_lastname.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_depart = Label(frm_a, text='Department', foreground='Black', background='White',
                             font=("times new roman", 20, "bold"))
        lbl_depart.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        txt_depart = Entry(frm_a,textvariable=self.var_dept, font=("times new roman", 17, "bold"), bd=5, relief="groove")
        txt_depart.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(frm_a, text='Gender', foreground='Black', background='White',
                         font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        combo_gender=ttk.Combobox(frm_a,textvariable=self.var_gender,font=("times new roman", 17, "bold"),state='readonly')
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=5, column=1, pady=10, padx=20)

        lbl_contact = Label(frm_a, text='Contact Number', foreground='Black', background='White',
                           font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_contact = Entry(frm_a,textvariable=self.var_contact,font=("times new roman", 17, "bold"), bd=5, relief="groove")
        txt_contact.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(frm_a, text='Address', foreground='Black', background='White',
                            font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.txt_address =Text(frm_a,font=("times new roman", 17, "bold"), bd=5, relief="groove",width="20",height="2")
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        frm_b = Frame(self.window, bd=4, relief="ridge", bg="grey")
        frm_b.place(x=130, y=620, width=250)

        btn_add=Button(frm_b,text="ADD",command=self.add_data,width=10,font="bold")
        btn_add.grid(row=0, column=1, pady=13, padx=10)
        btn_clear = Button(frm_b, text="CLEAR",command=self.clear_data,width=10,font="bold")
        btn_clear.grid(row=0, column=2, pady=13, padx=10)

        frm_c = Frame(self.window, bd=4, relief="ridge", bg="grey")
        frm_c.place(x=600, y=100, width=880, height=600)
        c_title = Label(frm_c, text='Student Detail',
                        foreground='Black', background='White', font=("times new roman", 25, "bold"))
        c_title.grid(row=0, columnspan=4, pady=20)


        frm_d=Frame(frm_c, bd=4, relief="ridge", bg="ivory")
        frm_d.place(x=10, y=70, width=750, height=500)
        scroll_x=Scrollbar(frm_d,orient=HORIZONTAL)
        scroll_y =Scrollbar(frm_d, orient=VERTICAL)
        self.Student_table=ttk.Treeview(frm_d,columns=("roll","FName","LName","Dept","Gender","Contact","Add"),xscrollcommand=scroll_y,yscrollcommand=scroll_x)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll No")
        self.Student_table.heading("FName", text="First Name")
        self.Student_table.heading("LName", text="Last Name")
        self.Student_table.heading("Dept", text="Department")
        self.Student_table.heading("Gender", text="Gender")
        self.Student_table.heading("Contact", text="Contact No")
        self.Student_table.heading("Add", text="Address")

        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("FName", width=100)
        self.Student_table.column("LName",width=100)
        self.Student_table.column("Dept", width=100)
        self.Student_table.column("Gender", width=100)
        self.Student_table.column("Contact", width=100)
        self.Student_table.column("Add", width=150)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):

            if(self.var_roll.get()=="" or self.var_dept.get()=="" or self.var_contact.get()=="" or self.var_fname.get()==""):
               messagebox.showerror("Error","All fields are required")
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Appus@19931993",database="school")
                    myCursor = conn.cursor()
                    myCursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.var_roll.get(),self.var_fname.get(),self.var_lname.get(),self.var_dept.get(),self.var_gender.get(),self.var_contact.get(),self.txt_address.get('1.0',END)))

                    conn.commit()
                    self.fetch_data()
                    self.clear_data()
                    conn.close()
                    messagebox.showinfo("Success","Student has been added!",parent=self.window)
                except EXCEPTION as ae:
                    messagebox.showerror("Error",f"Due To:{str(ae)}",parent=self.window)

    def fetch_data(self):
         conn = mysql.connector.connect(host="localhost", username="root", password="Appus@19931993", database="school")
         myCursor = conn.cursor()
         myCursor.execute("select * from student")
         rows=myCursor.fetchall()
         if len(rows)!=0:
             self.Student_table.delete(*self.Student_table.get_children())
             for row in rows:
                 self.Student_table.insert("",END,values=row)
             conn.commit()
         conn.close()

    def get_cursor(self,event=""):
         cursor_row=self.Student_table.focus()
         content=self.Student_table.item(cursor_row)
         rows=content["values"]

         self.var_roll.set(rows[0])
         self.var_fname.set(rows[1])
         self.var_lname.set(rows[2])
         self.var_dept.set(rows[3])
         self.var_gender.set(rows[4])
         self.var_contact.set(rows[5])
         self.txt_address.delete("1.0",END)
         self.txt_address.insert(END,rows[6])

    def clear_data(self):
        self.var_roll.set("")
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_dept.set("")
        self.var_gender.set("")
        self.var_contact.set("")
        self.txt_address.delete("1.0",END)



window=Tk()
obj=Student(window)
window.mainloop()
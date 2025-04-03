import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

class std():
    def __init__(self,root):
        self.root = root
        self.root.title("Student Record")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        title = tk.Label(self.root, text="Student Record Management System", bd=4, relief="raised", bg="light green", font=("Elephant", 40,"bold"))
        title.pack(side="top", fill="x")

        # option frame

        optFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(230,150,200))
        optFrame.place(width=self.width/3, height=self.height-180, x=50, y=100)

        addBtn = tk.Button(optFrame, command=self.addFrameFun, text="Add_Student", bd=3, relief="raised", bg="light gray", width=20, font=("Arial",20,"bold"))
        addBtn.grid(row=0, column=0, padx=30, pady=25)
        addBtn.bind("<Enter>", lambda e: addBtn.config(bg="light blue"))
        addBtn.bind("<Leave>", lambda e: addBtn.config(bg="light gray"))

        srchBtn = tk.Button(optFrame, command=self.searchFrameFun, text="Search_Student", bd=3, relief="raised", bg="light gray", width=20, font=("Arial",20,"bold"))
        srchBtn.grid(row=1, column=0, padx=30, pady=25)
        srchBtn.bind("<Enter>", lambda e: srchBtn.config(bg="light blue"))
        srchBtn.bind("<Leave>", lambda e: srchBtn.config(bg="light gray"))

        updBtn = tk.Button(optFrame, command=self.updFrameFun, text="Update_Record", bd=3, relief="raised", bg="light gray", width=20, font=("Arial",20,"bold"))
        updBtn.grid(row=2, column=0, padx=30, pady=25)
        updBtn.bind("<Enter>", lambda e: updBtn.config(bg="light blue"))
        updBtn.bind("<Leave>", lambda e: updBtn.config(bg="light gray"))

        allBtn = tk.Button(optFrame, command=self.showAll, text="Show_All", bd=3, relief="raised", bg="light gray", width=20, font=("Arial",20,"bold"))
        allBtn.grid(row=3, column=0, padx=30, pady=25)
        allBtn.bind("<Enter>", lambda e: allBtn.config(bg="light blue"))
        allBtn.bind("<Leave>", lambda e: allBtn.config(bg="light gray"))

        delBtn = tk.Button(optFrame, command=self.delFrameFun, text="Remove_Student", bd=3, relief="raised", bg="light gray", width=20, font=("Arial",20,"bold"))
        delBtn.grid(row=4, column=0, padx=30, pady=25)
        delBtn.bind("<Enter>", lambda e: delBtn.config(bg="light blue"))
        delBtn.bind("<Leave>", lambda e: delBtn.config(bg="light gray"))
    
        # detail Frame
        self.detFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(150,230,120))
        self.detFrame.place(width=self.width/2+50, height=self.height-180, x=self.width/3+100, y=100)

        lbl = tk.Label(self.detFrame, text="Record Details", font=("Arial",30,"bold"), bg=self.clr(150,230,120))
        lbl.pack(side="top", fill="x")

        self.tabFun()

    def tabFun(self):
        tabFrame = tk.Frame(self.detFrame, bd=4, relief="sunken", bg="cyan")
        tabFrame.place(width=self.width/2, height=self.height-280, x=23, y=70)

        x_scrol = tk.Scrollbar(tabFrame, orient="horizontal")
        x_scrol.pack(side="bottom", fill="x")

        y_scrol = tk.Scrollbar(tabFrame, orient="vertical")
        y_scrol.pack(side="right", fill="y")

        self.table = ttk.Treeview(tabFrame, xscrollcommand=x_scrol.set, yscrollcommand=y_scrol.set,
                                  columns=("roll", "name", "sub", "marks"))
        
        x_scrol.config(command=self.table.xview)
        y_scrol.config(command=self.table.yview)

        self.table.heading("roll", text="Roll_No")
        self.table.heading("name", text="Name")
        self.table.heading("sub", text="Subject")
        self.table.heading("marks", text="Marks")
        self.table["show"] = "headings"
        
        self.table.pack(fill="both", expand=1)

    def addFrameFun(self):
        self.addFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(150,180,250))
        self.addFrame.place(width=self.width/3, height=self.height-180, x=self.width/3+80, y=100)

        rnLbl = tk.Label(self.addFrame, text="Roll_No:", bg=self.clr(150,180,250), font=("arial",15,"bold"))
        rnLbl.grid(row=0, column=0, padx=20, pady=25)
        self.rollNo = tk.Entry(self.addFrame, width=18, font=("arial",15,"bold"), bd=3)
        self.rollNo.grid(row=0, column=1, padx=10, pady=25)
        self.rollNo.bind("<FocusIn>", lambda e: self.rollNo.config(bd=5, highlightbackground="blue"))
        self.rollNo.bind("<FocusOut>", lambda e: self.rollNo.config(bd=3, highlightbackground="gray"))
        self.rollNo.bind("<KeyPress-Up>", self.focus_previous)
        self.rollNo.bind("<KeyPress-Down>", self.focus_next)
        self.rollNo.bind("<Return>", lambda e: self.addFun())

        nameLbl = tk.Label(self.addFrame, text="Name:", bg=self.clr(150,180,250), font=("arial",15,"bold"))
        nameLbl.grid(row=1, column=0, padx=20, pady=25)
        self.name = tk.Entry(self.addFrame, width=18, font=("arial",15,"bold"), bd=3)
        self.name.grid(row=1, column=1, padx=10, pady=25)
        self.name.bind("<FocusIn>", lambda e: self.name.config(bd=5, highlightbackground="blue"))
        self.name.bind("<FocusOut>", lambda e: self.name.config(bd=3, highlightbackground="gray"))
        self.name.bind("<KeyPress-Up>", self.focus_previous)
        self.name.bind("<KeyPress-Down>", self.focus_next)
        self.name.bind("<Return>", lambda e: self.addFun())

        subLbl = tk.Label(self.addFrame, text="Subject:", bg=self.clr(150,180,250), font=("arial",15,"bold"))
        subLbl.grid(row=2, column=0, padx=20, pady=25)
        self.sub = tk.Entry(self.addFrame, width=18, font=("arial",15,"bold"), bd=3)
        self.sub.grid(row=2, column=1, padx=10, pady=25)
        self.sub.bind("<FocusIn>", lambda e: self.sub.config(bd=5, highlightbackground="blue"))
        self.sub.bind("<FocusOut>", lambda e: self.sub.config(bd=3, highlightbackground="gray"))
        self.sub.bind("<KeyPress-Up>", self.focus_previous)
        self.sub.bind("<KeyPress-Down>", self.focus_next)
        self.sub.bind("<Return>", lambda e: self.addFun())

        gLbl = tk.Label(self.addFrame, text="Marks:", bg=self.clr(150,180,250), font=("arial",15,"bold"))
        gLbl.grid(row=3, column=0, padx=20, pady=25)
        self.marks = tk.Entry(self.addFrame, width=18, font=("arial",15,"bold"), bd=3)
        self.marks.grid(row=3, column=1, padx=10, pady=25)
        self.marks.bind("<FocusIn>", lambda e: self.marks.config(bd=5, highlightbackground="blue"))
        self.marks.bind("<FocusOut>", lambda e: self.marks.config(bd=3, highlightbackground="gray"))
        self.marks.bind("<KeyPress-Up>", self.focus_previous)
        self.marks.bind("<KeyPress-Down>", self.focus_next)
        self.marks.bind("<Return>", lambda e: self.addFun())

        okBtn = tk.Button(self.addFrame, command=self.addFun, text="Enter", bd=3, relief="raised", font=("Arial",20,"bold"), width=20)
        okBtn.grid(row=4, column=0, padx=30, pady=25, columnspan=2)

    def focus_previous(self, event):
        event.widget.tk_focusPrev().focus()
        return "break"

    def focus_next(self, event):
        event.widget.tk_focusNext().focus()
        return "break"

    def desAdd(self):
        self.addFrame.destroy()

    def addFun(self):
        rn = self.rollNo.get()
        name = self.name.get()
        sub = self.sub.get()
        marks = self.marks.get()

        if rn and name and sub and marks:
            rNo = int(rn)
            try:
                self.dbFun()
                self.cur.execute("insert into student(rollNo,name,sub,marks) values(%s,%s,%s,%s)", (rNo, name, sub, marks))
                self.con.commit()
                tk.messagebox.showinfo("Success", f"Student {name} with Roll_No.{rNo} is Registered!")
                self.root.update()

                self.desAdd()

                self.cur.execute("select * from student where rollNo=%s", rNo)
                row = self.cur.fetchone()
                self.table.delete(*self.table.get_children())
                self.table.insert('', tk.END, values=row)

                self.con.close()
            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")
                self.desAdd()
        else:
            tk.messagebox.showerror("Error", "Please Fill All Input Fields!")
            self.root.update()

    def searchFrameFun(self):
        self.addFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(150,180,250))
        self.addFrame.place(width=self.width/3, height=self.height-350, x=self.width/3+80, y=100)

        optLbl = tk.Label(self.addFrame, text="Select:", bg=self.clr(150,180,250), font=("arial",15,"bold"))
        optLbl.grid(row=0, column=0, padx=20, pady=25)
        self.option = ttk.Combobox(self.addFrame, width=17, values=("rollNo", "Name", "Sub"), font=("Arial",15,"bold"))
        self.option.set("Select Option")
        self.option.grid(row=0, column=1, padx=10, pady=30)

        valLbl = tk.Label(self.addFrame, text="Value:", bg=self.clr(150,180,250), font=("arial",15,"bold"))
        valLbl.grid(row=1, column=0, padx=20, pady=25)
        self.value = tk.Entry(self.addFrame, width=18, font=("arial",15,"bold"), bd=3)
        self.value.grid(row=1, column=1, padx=10, pady=25)

        okBtn = tk.Button(self.addFrame, command=self.searchFun, text="Enter", bd=3, relief="raised", font=("Arial",20,"bold"), width=20)
        okBtn.grid(row=2, column=0, padx=30, pady=25, columnspan=2)

    def searchFun(self):
        opt = self.option.get()
        val = self.value.get()

        if opt == "rollNo":
            rn = int(val)
            try:
                self.dbFun()
                self.cur.execute("select * from student where rollNo=%s", rn)
                row = self.cur.fetchone()
                self.table.delete(*self.table.get_children())
                self.table.insert('', tk.END, values=row)

                self.desAdd()
                self.con.close()
            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")
        else:
            try:
                self.dbFun()
                query = f"select * from student where {opt}=%s "
                self.cur.execute(query, (val))
                data = self.cur.fetchall()
                self.table.delete(self.table.get_children())

                for i in data:
                    self.table.insert('', tk.END, values=i)

                self.desAdd()
                self.con.close()
            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")

    def dbFun(self):
        self.con = pymysql.connect(host="localhost", user="root", passwd="Ojesh@123", database="record")
        self.cur = self.con.cursor()

    def updFrameFun(self):
        self.addFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(150,180,250))
        self.addFrame.place(width=self.width/3, height=self.height-300, x=self.width/3+80, y=100)

        optLbl = tk.Label(self.addFrame, text="Select:", bg=self.clr(150,180,250), font=("arial",15,"bold"))
        optLbl.grid(row=0, column=0, padx=20, pady=25)
        self.option = ttk.Combobox(self.addFrame, width=17, values=("Name", "Sub", "marks"), font=("Arial",15,"bold"))
        self.option.set("Select Option")
        self.option.grid(row=0, column=1, padx=10, pady=30)

        valLbl = tk.Label(self.addFrame, text="New_Value:", bg=self.clr(150,180,250), font=("arial",15,"bold"))
        valLbl.grid(row=1, column=0, padx=20, pady=25)
        self.value = tk.Entry(self.addFrame, width=18, font=("arial",15,"bold"), bd=3)
        self.value.grid(row=1, column=1, padx=10, pady=25)

        rollLbl = tk.Label(self.addFrame, text="Roll_No:", bg=self.clr(150,180,250), font=("arial",15,"bold"))
        rollLbl.grid(row=2, column=0, padx=20, pady=25)
        self.roll = tk.Entry(self.addFrame, width=18, font=("arial",15,"bold"), bd=3)
        self.roll.grid(row=2, column=1, padx=10, pady=25)

        okBtn = tk.Button(self.addFrame, command=self.updFun, text="Enter", bd=3, relief="raised", font=("Arial",20,"bold"), width=20)
        okBtn.grid(row=3, column=0, padx=30, pady=25, columnspan=2)

    def updFun(self):
        opt = self.option.get()
        val = self.value.get() 
        rNo = int(self.roll.get()) 

        try:
            self.dbFun()
            query = f"update student set {opt}=%s where rollNo=%s"
            self.cur.execute(query, (val, rNo))
            self.con.commit()
            tk.messagebox.showinfo("Success", f"Record is Updated for Student with Roll_No.{rNo}")
            self.root.update()

            self.desAdd()

            self.cur.execute("select * from student where rollNo=%s", rNo)
            row = self.cur.fetchone()

            self.table.delete(*self.table.get_children())
            self.table.insert('', tk.END, values=row)

            self.con.close()
             
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error: {e}")

    def showAll(self):
        try:
            self.dbFun()
            self.cur.execute("select * from student")
            data = self.cur.fetchall()
            self.table.delete(*self.table.get_children())

            for i in data:
                self.table.insert('', tk.END, values=i)

            self.con.close()
        
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error: {e}")

    def delFrameFun(self):
        self.addFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(150,180,250))
        self.addFrame.place(width=self.width/3, height=self.height-400, x=self.width/3+80, y=100)

        rnLbl = tk.Label(self.addFrame, text="Roll_No:", bg=self.clr(150,180,250), font=("arial",15,"bold"))
        rnLbl.grid(row=0, column=0, padx=20, pady=25)
        self.rollNo = tk.Entry(self.addFrame, width=18, font=("arial",15,"bold"), bd=3)
        self.rollNo.grid(row=0, column=1, padx=10, pady=25)

        okBtn = tk.Button(self.addFrame, command=self.delFun, text="Enter", bd=3, relief="raised", font=("Arial",20,"bold"), width=20)
        okBtn.grid(row=1, column=0, padx=30, pady=25, columnspan=2)

    def delFun(self):
        rNo = int(self.rollNo.get())

        try:
            self.dbFun()
            self.cur.execute("delete from student where rollNo=%s", rNo)
            self.con.commit()
            tk.messagebox.showinfo("Success", f"Student with Roll_No.{rNo} is Removed")
            self.root.update()

            self.con.close()
            self.desAdd()

        except Exception as e:
            tk.messagebox.showerror("Error", f"Error: {e}")
            self.root.update()

    def clr(self, r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"

root = tk.Tk()
obj = std(root)
root.mainloop()

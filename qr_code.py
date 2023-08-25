from tkinter import*
from tkinter import ttk,messagebox
from resizeimage import resizeimage
from PIL import Image,ImageTk
import qrcode
class qr_code:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x600")
        self.root.maxsize(895,530)
        self.root.title("QR CODE GENERATER   version 0.53      |   Developed by Vinod ")
        
        title=Label(self.root,text="QR Code Generator ",font=("times new roman",25," bold"),bg="darkblue",fg="white",relief=GROOVE,bd=5)
        title.place(x=0,y=0,width=900,height=50)
        
        #================Variable=============================
        
        self.qr_var=StringVar()
        self.name_var=StringVar()
        self.dept_var=StringVar()
        self.desig_var=StringVar()
        
        
        
        
        frame1=LabelFrame(self.root,bd=10,relief=GROOVE)
        frame1.place(x=5,y=65,width=540,height=450)
    
        ti=Label(frame1,text="QR Code Details ",font=("times new roman",18," bold"),bg="green",fg="white",relief=RIDGE,bd=2)
        ti.place(x=5,y=5,width=500,height=30)
        
        #self.lbl_msg=Label(frame1,text=self.msg,font=("times new roman",18),fg="green").place(x=100,y=380)
        
        lbl_qr=Label(frame1,text="QR Code Link",font=("times new roman",16,),fg="black")
        lbl_qr.place(x=10,y=100)

        ent_qr=Entry(frame1,textvariable=self.qr_var,font=("times new roman",16,),fg="black")
        ent_qr.place(x=155,y=100)
           
    
        lbl_name=Label(frame1,text="QR Name",font=("times new roman",16,),fg="black")
        lbl_name.place(x=10,y=160)

        ent_name=Entry(frame1,textvariable=self.name_var,font=("times new roman",16,),fg="black")
        ent_name.place(x=155,y=160)

        lbl_dept=Label(frame1,text="Title",font=("times new roman",16,),fg="black")
        lbl_dept.place(x=10,y=220)

        ent_dept=Entry(frame1,textvariable=self.dept_var,font=("times new roman",16,),fg="black")
        ent_dept.place(x=155,y=220)

        lbl_designation=Label(frame1,text="Information ",font=("times new roman",16,),fg="black")
        lbl_designation.place(x=10,y=280)

        ent_designation=Entry(frame1,textvariable=self.desig_var,font=("times new roman",16,),fg="black")
        ent_designation.place(x=155,y=280)
    
    
        gen_btn=Button(frame1,text="Generate QR",command=self.qr_gen,font=("times new roman",15),bg="purple",fg="white",bd=5,relief=GROOVE)
        gen_btn.place(x=155,y=330)

        clear_btn=Button(frame1,text="Clear",command=self.clear,font=("times new roman",15),bg="grey",fg="white",bd=5,relief=GROOVE)
        clear_btn.place(x=310,y=330)
    
      
   
   
   
   
   
   
   
   #========================== FRME 2 ====================================================

        frame2=LabelFrame(self.root,font=30,bd=10,relief=RIDGE)
        frame2.place(x=545,y=60,width=343,height=450)

        tv=Label(frame2,text="QR Code ",font=("times new roman",18," bold"),bg="green",fg="white",relief=RIDGE,bd=2)
        tv.place(x=5,y=5,width=320,height=30)

        self.qr_code=Label(frame2,text="No QR Code\n\n Available",font=("times new roman",18," bold"),bg="white",fg="black",relief=GROOVE,bd=5)
        self.qr_code.place(x=15,y=85,width=300,height=300)
 
    def qr_gen(self):
       if self.qr_var.get()=="" or self.name_var.get()=="" or self.dept_var.get()=="" or self.desig_var.get()=="":
           messagebox.showerror("Error","  All Field Are Required ")
       else:
           qr_data=(f"Employe : {self.qr_var.get()}\n,Name :{self.name_var.get()}\n,Department :{self.dept_var.get()},Designation :{self.desig_var.get()}")
           qr_code=qrcode.make(qr_data)
          
           qr_code=resizeimage.resize_cover(qr_code,[300,300])
           qr_code.save(self.name_var.get()+".png")
           #self.msg="QR Generated Sucessfully !!!"
           
           self.img=ImageTk.PhotoImage(file=str(self.name_var.get())+".png")
           self.qr_code.config(image=self.img)
           
           
           


    
    
    
    def clear(self):
        self.qr_var.set("")
        self.name_var.set("")
        self.dept_var.set("")
        self.desig_var.set("")




root=Tk()
obj=qr_code(root)
root.mainloop()
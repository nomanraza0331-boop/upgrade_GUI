from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Ragistration form !")


username=StringVar()
Email=StringVar()
Mobile_number=StringVar()
Password=StringVar()
verify_password=StringVar()
gender=StringVar()


gender=StringVar()


def submit_form():
    Skills=[]


     
    if p.get()==1:
        Skills.append("Python")
    if s.get()==1:
         Skills.append("SQL")
    if j.get()==1:
         Skills.append("Java")
    if js.get()==1:
         Skills.append("Javascript")

    print(Skills)
    
     

def function():
    username.get()
    Email.get()
    Mobile_number.get()
    Password.get()
    verify_password.get()


    if username=="" or Email=="" or Mobile_number=="" or Password=="" or verify_password=="":
        messagebox.showerror("Error!" , "please re check information again !")
    elif Password.get()!=verify_password.get():
            messagebox.showerror("Error!","password doen't match check again!")
    else:
        print(f"{username.get()}\n {Email.get()}\n {Mobile_number.get()}\n {Password.get()}\n {verify_password.get()}")
        # messagebox.showinfo("succecfully","your regestration complete")


L1=Label(root,text="Enter username:",font=("Times New Roman",20),padx=10,pady=10)
L1.grid(row=0,column=0)
username=Entry(root,font=("Times New Roman",20,"italic"))
username.grid(row=0,column=1,padx=10,pady=10)

L2=Label(root,text="Enter Email:",font=("Times New Roman",20),padx=10,pady=10)
L2.grid(row=1,column=0)
Email=Entry(root,font=("Times New Roman",20,"italic"))
Email.grid(row=1,column=1,padx=10,pady=10)

L3=Label(root,text="Enter Mobile number:",font=("Times New Roman",20),padx=10,pady=10)
L3.grid(row=2,column=0)
Mobile_number=Entry(root,font=("Times New Roman",20,"italic"))
Mobile_number.grid(row=2,column=1,padx=10,pady=10)

L4=Label(root,text="Enter Password:",font=("Times New Roman",20),padx=10,pady=10)
L4.grid(row=3,column=0)
Password=Entry(root,font=("Times New Roman",20,""),show="*")
Password.grid(row=3,column=1,padx=10,pady=10)

L5=Label(root,text="Enter verify_password:",font=("Times New Roman",20),padx=10,pady=10)
L5.grid(row=4,column=0)
verify_password=Entry(root,font=("Times New Roman",20,"italic"),show="*")
verify_password.grid(row=4,column=1,padx=10,pady=10)

B1=Button(root,text="Submit",font=("Bell MT",15,"bold",),bg="white",fg="green",command=function)
B1.grid(row=5,column=0)
B2=Button(root,text="Exit",font=("Bell MT",15,"bold"),bg="white",fg="red",command=root.destroy)
B2.grid(row=5,column=1)

L6=Label(root,text="Select Gender !",font=("Times New Roman",20))
L6.grid(row=6,column=0)

m=Radiobutton(root,text="Male",font=("Times New Roman",17))
m.grid(row=7,column=0)

f=Radiobutton(root,text="Female",font=("Times New Roman",17))
f.grid(row=7,column=1)

L7=Label(root,text="Select Skill",font=("Times New Roman",20))
L7.grid(row=8,column=0)

p=Checkbutton(root,text="Python",font=("Times New Roman",15))
p.grid(row=9,column=0)

s=Checkbutton(root,text="SQL",font=("Times New Roman",15))
s.grid(row=9,column=1)

j=Checkbutton(root,text="Java",font=("Times New Roman",15))
j.grid(row=10,column=0)

js=Checkbutton(root,text="Javascript",font=("Times New Roman",15))
js.grid(row=10,column=1)


root.mainloop()

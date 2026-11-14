
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Registration Form!")
root.geometry("650x650")

# Variables
gender = StringVar()

p = IntVar()
s = IntVar()
j = IntVar()
js = IntVar()


def submit_form():

    # Get input values
    name = username.get()
    email = Email.get()
    mobile = Mobile_number.get()
    password = Password.get()
    confirm_password = verify_password.get()

    # Get selected skills
    Skills = []

    if p.get() == 1:
        Skills.append("Python")

    if s.get() == 1:
        Skills.append("SQL")

    if j.get() == 1:
        Skills.append("Java")

    if js.get() == 1:
        Skills.append("Javascript")

    # Validation
    if name == "" or email == "" or mobile == "" or password == "" or confirm_password == "":
        messagebox.showerror("Error!", "Please fill all information!")

    elif password != confirm_password:
        messagebox.showerror("Error!", "Passwords don't match!")

    elif gender.get() == "":
        messagebox.showerror("Error!", "Please select your gender!")

    else:
        messagebox.showinfo(
            "Success!",
            "Your registration is completed successfully!"
        )

        print("Username:", name)
        print("Email:", email)
        print("Mobile Number:", mobile)
        print("Password:", password)
        print("Gender:", gender.get())
        print("Skills:", Skills)


# Username
L1 = Label(root, text="Enter username:", font=("Times New Roman", 20))
L1.grid(row=0, column=0, padx=10, pady=10)

username = Entry(root, font=("Times New Roman", 20, "italic"))
username.grid(row=0, column=1, padx=10, pady=10)


# Email
L2 = Label(root, text="Enter Email:", font=("Times New Roman", 20))
L2.grid(row=1, column=0, padx=10, pady=10)

Email = Entry(root, font=("Times New Roman", 20, "italic"))
Email.grid(row=1, column=1, padx=10, pady=10)


# Mobile Number
L3 = Label(root, text="Enter Mobile number:", font=("Times New Roman", 20))
L3.grid(row=2, column=0, padx=10, pady=10)

Mobile_number = Entry(root, font=("Times New Roman", 20))
Mobile_number.grid(row=2, column=1, padx=10, pady=10)


# Password
L4 = Label(root, text="Enter Password:", font=("Times New Roman", 20))
L4.grid(row=3, column=0, padx=10, pady=10)

Password = Entry(root, font=("Times New Roman", 20), show="*")
Password.grid(row=3, column=1, padx=10, pady=10)


# Verify Password
L5 = Label(root, text="Verify Password:", font=("Times New Roman", 20))
L5.grid(row=4, column=0, padx=10, pady=10)

verify_password = Entry(root, font=("Times New Roman", 20), show="*")
verify_password.grid(row=4, column=1, padx=10, pady=10)


# Buttons
B1 = Button(
    root,
    text="Submit",
    font=("Bell MT", 15, "bold"),
    bg="white",
    fg="green",
    command=submit_form
)
B1.grid(row=5, column=0, pady=10)

B2 = Button(
    root,
    text="Exit",
    font=("Bell MT", 15, "bold"),
    bg="white",
    fg="red",
    command=root.destroy
)
B2.grid(row=5, column=1, pady=10)


# Gender
L6 = Label(root, text="Select Gender!", font=("Times New Roman", 20))
L6.grid(row=6, column=0, pady=10)

m = Radiobutton(
    root,
    text="Male",
    font=("Times New Roman", 17),
    variable=gender,
    value="Male"
)
m.grid(row=7, column=0)

f = Radiobutton(
    root,
    text="Female",
    font=("Times New Roman", 17),
    variable=gender,
    value="Female"
)
f.grid(row=7, column=1)


# Skills
L7 = Label(root, text="Select Skills", font=("Times New Roman", 20))
L7.grid(row=8, column=0, pady=10)

Checkbutton(
    root, text="Python",
    font=("Times New Roman", 15),
    variable=p
).grid(row=9, column=0)

Checkbutton(
    root, text="SQL",
    font=("Times New Roman", 15),
    variable=s
).grid(row=9, column=1)

Checkbutton(
    root, text="Java",font=("Times New Roman", 15),variable=j).grid(row=10, column=0)

Checkbutton(
    root, text="Javascript",
    font=("Times New Roman", 15),
    variable=js
).grid(row=10, column=1)


root.mainloop()

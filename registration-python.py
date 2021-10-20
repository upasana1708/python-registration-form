#how to create simple GUI registration form.
#importing tkinter module for GUI application

from tkinter import *
from tkinter import messagebox as tkMessageBox

#Creating object 'root' of Tk()

root = Tk()

#Providing Geometry to the form

root.geometry("500x500")

#Providing title to the form

root.title('Registration form')

#this creates 'Label' widget for Registration Form and uses place() method.

label_0 =Label(root,text="Registration form", width=20, font=("bold",20))

#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position

label_0.place(x=90,y=60)

#this creates 'Label' widget for Fullname and uses place() method.

label_1 =Label(root,text="Full Name", width=20, font=("bold",10))
label_1.place(x=80,y=130)

#this will accept the input string text from the user.

entry_2=Entry(root)
entry_2.place(x=240,y=130)

#this creates 'Label' widget for Email and uses place() method.

label_3 =Label(root,text="Email", width=20, font=("bold",10))
label_3.place(x=68,y=180)

entry_3=Entry(root)
entry_3.place(x=240,y=180)

#this creates 'Label' widget for Gender and uses place() method.

label_4 =Label(root,text="Gender", width=20, font=("bold",10))
label_4.place(x=70,y=230)


#the variable 'var' mentioned here holds Integer Value, by default 0

gender_var=IntVar()
gender_list = ["Male", "Female"]
#this creates 'Radio button' widget and uses place() method

Radiobutton(root, text=gender_list[0], padx= 5, variable= gender_var, value=0).place(x=235,y=230)
Radiobutton(root, text=gender_list[1], padx= 20, variable= gender_var, value=1).place(x=290,y=230)


##this creates 'Label' widget for country and uses place() method.

label_5=Label(root,text="Country",width=20, font=("bold",10))
label_5.place(x=70,y=280)

#this creates list of countries available in the dropdownlist.

list_of_country=[ 'India' ,'US' , 'UK' ,'Germany' ,'Austria']

#the variable 'country_var' mentioned here holds String Value, by default ""

country_var=StringVar()
droplist=OptionMenu(root, country_var, *list_of_country)
droplist.config(width=20)
country_var.set('Select your Country')
droplist.place(x=240,y=280)

##this creates 'Label' widget for Qualification and uses place() method.

label_6=Label(root,text="Qualification", width=20, font=('bold',10))
label_6.place(x=75,y=330)


#the variable 'var1' mentioned here holds Integer Value, by default 0 for unchecked

qualification_var=IntVar()

#this creates Checkbutton widget and uses place() method.

Checkbutton(root,text="Graduate", variable=qualification_var).place(x=230,y=330)


def process():
    f = open("user-registration-details.txt", "a")

    name = entry_2.get()
    email = entry_3.get()
    gender = gender_list[gender_var.get()]
    country = country_var.get()
    qualification = qualification_var.get()

    content_to_save = "{},{},{},{},{}\n".format(name, email, gender, country, qualification)
    f.write(content_to_save)    
    f.close()

    print("Record saved")

    tkMessageBox.showinfo("Response Box", "Details Saved Successfully")


#this creates button for submitting the details provides by the user

Button(root, text='Submit', width=20, bg="black", fg='white', command=process).place(x=180,y=380)


#this will run the mainloop.
root.mainloop()


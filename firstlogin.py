from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

Label(root, text="python registrstion form", font="arial 15 bold").grid(row=0, column=3)

name = Label(root, text="name")
phone = Label(root, text="phone")
gender = Label(root, text="gender")
emergency = Label(root, text="emergemncy")
paymentmode =Label(root, text="paymentmode")

name.grid(row=1, column=2) 
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymenrmodevalue = StringVar

checkvalue = IntVar

nameentry = Entry(root, textvariable = namevalue)
phoneentry = Entry(root, textvariable = namevalue)
genderentry = Entry(root, textvariable = namevalue)
emergencyentry = Entry(root, textvariable = namevalue)
paymentmodeentry = Entry(root, textvariable = namevalue)

nameentry.grid(row =1 , column = 3)
phoneentry.grid(row =2 , column = 3)
genderentry.grid(row =3 , column = 3)
emergencyentry.grid(row =4 , column = 3)
paymentmodeentry.grid(row =5 , column = 3)

checkbtn = Checkbutton(text="rember me ?", variable = checkvalue)
checkbtn.grid(row = 6, column = 3)

Button(text="Submit", command = getvals).grid(row = 7, column = 3)
root.mainloop() 
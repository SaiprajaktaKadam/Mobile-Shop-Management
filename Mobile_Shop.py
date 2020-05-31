# Title of project- Mobile Shop Management
#Project by - Saiprajakta Kadam (187012)
#             Rimzim Gawade (187009)
from tkinter import messagebox
from tkinter import *
import sqlite3
def clear1(event1):
    s1 = str(usernameentry.get())
    s2 = str(passwordentry.get())
    usernameentry.delete(0,str(usernameentry.get()).__len__())
    passwordentry.delete(0,str(passwordentry.get()).__len__())
def log(event):
    if usernameentry.get()=="" or passwordentry.get=="":
        messagebox.showerror("Error","All fields are required")
    elif usernameentry.get()=="sai" and passwordentry.get()=="1234":
        window1=Tk()
        window1.title("Menu Page")
        window1.geometry("300x300")
        window1.configure(bg="blue")
        b1=Button(window1,text="Entry of Mobile",height=2,width=15,command=entryofmob)
        b1.place(x=100,y=25)
        b2=Button(window1,text="Sell the Mobile",height=2,width=15,command=sellmob)
        b2.place(x=100,y=110)
        b3=Button(window1,text="Search the Mobile",height=2,width=15,command=searchmob)
        b3.place(x=100,y=190)
    else:
        messagebox.showerror("Error","Invalid username or password")
def entryofmob():
    window2 = Tk()
    window2.title("Entry of Mobile")
    window2.geometry("600x600")
    window2.configure(bg="violet")
    title = Label(window2, text="Fill Mobile Information", font=(("Times New Roman"), 20), bg="Yellow")
    title.place(x=120, y=10)
    brand = Label(window2, text="Brand", font=(("Arial Black"), 10))
    brand.place(x=60, y=80)
    brandentry = Entry(window2, bd="4")
    brandentry.place(x=180, y=80)
    model = Label(window2, text="Model", font=(("Arial Black"), 10))
    model.place(x=60, y=150)
    modelentry = Entry(window2, bd="4")
    modelentry.place(x=180, y=150)
    price = Label(window2, text="Price per", font=(("Arial Black"), 10))
    price.place(x=60, y=220)
    priceentry = Entry(window2, bd="4")
    priceentry.place(x=180, y=220)
    date = Label(window2, text="Date", font=(("Arial Black"), 10))
    date.place(x=60, y=290)
    dateentry = Entry(window2, bd="4")
    dateentry.place(x=180, y=290)
    quantity = Label(window2, text="Quantity", font=(("Arial Black"), 10))
    quantity.place(x=60, y=360)
    quantityentry = Entry(window2, bd="4")
    quantityentry.place(x=180, y=360)

    def clear2(event2):
        s1 = str(brandentry.get())
        s2 = str(modelentry.get())
        s3 = str(priceentry.get())
        s4 = str(dateentry.get())
        s5 = str(quantityentry.get())
        brandentry.delete(0, str(brandentry.get()).__len__())
        modelentry.delete(0, str(modelentry.get()).__len__())
        priceentry.delete(0, str(priceentry.get()).__len__())
        dateentry.delete(0, str(dateentry.get()).__len__())
        quantityentry.delete(0, str(quantityentry.get()).__len__())

    reset2 = Button(window2, text="Reset", font=(("Calibri")), height="1", width="8")
    reset2.bind('<Button>', clear2)
    reset2.place(x=300, y=420)

    def save1():
        conn = sqlite3.connect("Mobile_Shop.db")
        c = conn.cursor()
        #c.execute("""CREATE TABLE entry_of_mobile4(brand text,model text,price text,date text,quantity integer)""")
        c.execute("INSERT INTO entry_of_mobile4 VALUES(:brand, :model, :price, :date, :quantity)",
                    {'brand': brandentry.get(),
                    'model': modelentry.get(),
                    'price': priceentry.get(),
                    'date': dateentry.get(),
                    'quantity': quantityentry.get()
                    })

        conn.commit()
        conn.close()
        print("Data inserted.......")

    save1 = Button(window2, text="Add Record To Database", font=(("Calibri")), height="1", width="20",
                       command=save1)
    save1.place(x=80, y=420)



def searchmob():
        root = Tk()
        root.title("Search Mobile")
        root.geometry("400x400")
        root.configure(bg="Yellow")
        brand = Label(root, text="Brand", font=(("Arial Black"), 10))
        brand.place(x=60, y=80)
        brandentry = Entry(root, bd="4")
        brandentry.place(x=180, y=80)
        model = Label(root, text="Model", font=(("Arial Black"), 10))
        model.place(x=60, y=150)
        modelentry = Entry(root, bd="4")
        modelentry.place(x=180, y=150)

        def search():
            conn = sqlite3.connect("Mobile_Shop.db")
            c = conn.cursor()
            #c.execute("SELECT price,date,quantity FROM entry_of_mobile4 WHERE brand = brandentry.get(),model = modelentry.get()")
            c.execute("SELECT * FROM entry_of_mobile4")
            data = c.fetchall()
            print(data)
            conn.commit()
            conn.close()

        search1 = Button(root, text="Show Records", font=(("Calibri")), height="1", width="16",command = search)
        search1.place(x=160, y=250)
root=Tk()
root.title("Admin Login")
root.geometry("400x400")
root.configure(bg="Red")
admin=Label(root,text="ADMIN LOGIN",font=(("Times New Roman"),20),bg="Yellow")
admin.place(x=120,y=10)
username=Label(root,text="Username",font=(("Arial Black"),10))
username.place(x=60,y=80)
usernameentry=Entry(root,bd="4")
usernameentry.place(x=180,y=80)
password=Label(root,text="Password",font=(("Arial Black"),10))
password.place(x=60,y=150)
passwordentry=Entry(root,show="*",bd="4")
passwordentry.place(x=180,y=150)
reset1=Button(root,text="Reset",font=(("Calibri")),height="1",width="8")
reset1.bind('<Button>',clear1)
reset1.place(x=220,y=250)
login=Button(root,text="Login",font=(("Calibri")),height="1",width="8")
login.bind('<Button>',log)
login.place(x=80,y=250)
def sellmob():
    window3=Tk()
    window3.title("Sell Mobile")
    window3.geometry("600x600")
    window3.configure(bg="pink")
    title = Label(window3, text="Fill the Information", font=(("Times New Roman"), 20), bg="Yellow")
    title.place(x=120, y=10)
    brand = Label(window3, text="Brand", font=(("Arial Black"), 10))
    brand.place(x=60, y=80)
    brandentry = Entry(window3, bd="4")
    brandentry.place(x=180, y=80)
    model = Label(window3, text="Model", font=(("Arial Black"), 10))
    model.place(x=60, y=150)
    modelentry = Entry(window3,bd="4")
    modelentry.place(x=180, y=150)
    price = Label(window3, text="Price per", font=(("Arial Black"), 10))
    price.place(x=60, y=220)
    priceentry = Entry(window3, bd="4")
    priceentry.place(x=180, y=220)
    date = Label(window3, text="Date", font=(("Arial Black"), 10))
    date.place(x=60, y=290)
    dateentry = Entry(window3, bd="4")
    dateentry.place(x=180, y=290)
    quantity = Label(window3, text="Quantity", font=(("Arial Black"), 10))
    quantity.place(x=60, y=360)
    quantityentry = Entry(window3, bd="4")
    quantityentry.place(x=180, y=360)
    customer = Label(window3, text="Customer Name", font=(("Arial Black"), 10))
    customer.place(x=60, y=430)
    customerentry = Entry(window3, bd="4")
    customerentry.place(x=180, y=430)
    mob = Label(window3, text="Mobile No.", font=(("Arial Black"), 10))
    mob.place(x=60, y=500)
    mobentry = Entry(window3, bd="4")
    mobentry.place(x=180, y=500)

    def clear3():
        s1 = str(brandentry.get())
        s2 = str(modelentry.get())
        s3 = str(priceentry.get())
        s4 = str(dateentry.get())
        s5 = str(quantityentry.get())
        s6 = str(customerentry.get())
        s7 = str(mobentry.get())
        brandentry.delete(0, str(brandentry.get()).__len__())
        modelentry.delete(0, str(modelentry.get()).__len__())
        priceentry.delete(0, str(priceentry.get()).__len__())
        dateentry.delete(0, str(dateentry.get()).__len__())
        quantityentry.delete(0, str(quantityentry.get()).__len__())
        customerentry.delete(0, str(customerentry.get()).__len__())
        mobentry.delete(0, str(mobentry.get()).__len__())

    reset3 = Button(window3, text="Reset", font=(("Calibri")), height="1", width="8",command=clear3)
    reset3.place(x=300, y=560)
    def save2():
        conn = sqlite3.connect("Mobile_Shop.db")
        c = conn.cursor()
        #c.execute("""CREATE TABLE Sell_Mobile1(brand text,model text,price text,date text,quantity integer,customer_name text,mob_no text)""")
        c.execute("INSERT INTO Sell_Mobile1 VALUES(:brand,:model,:price,:date,:quantity,:customer_name,:mob_no)",
        {
                    'brand': brandentry.get(),
                    'model': modelentry.get(),
                    'price': priceentry.get(),
                    'date': dateentry.get(),
                    'quantity': quantityentry.get(),
                    'customer_name': customerentry.get(),
                    'mob_no': mobentry.get()
        })


        conn.commit()
        conn.close()
        print("Data inserted.......")

    save2 = Button(window3, text="Add Record To Database", font=(("Calibri")), height="1", width="20", command=save2)
    save2.place(x=80, y=560)
root.mainloop()


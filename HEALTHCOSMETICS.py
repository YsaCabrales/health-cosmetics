# from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import messagebox
from tkinter import *
import os
import tkinter as tkr
from tkinter.tix import *

#global scope
total_price = 0
prices =[]
products = []

def addtocart(productname, price): #Add item to cart
    global total_price
    tkr.messagebox.showinfo("Cart", "Item successfuly added to Cart")
    total_price += price
    products.append(productname)
    prices.append(price)

def product(window, x, y, photo, price, productname, pricedisplay): #display product
    frame=tkr.Frame(window, bg="pink",width=430,height=230)
    frame.place(x=x,y=y)

    Label(frame, image = photo).place(x=5,y=5)

    Label(frame, text=productname).place(x=230,y=10)
    Label(frame, text=pricedisplay).place(x=230,y=40)

    addtocartbutton = Button(frame, text="Add to Cart", command=lambda: addtocart(productname,price), bg='light green',fg='dark green',font = "calibri").place(x=230,y=95)  

def Maybelline_Cosmetics(): #maybelline screen
    maybelline=Toplevel(main_screen)
    maybelline.title("HEALTH&COSMETICS")
    maybelline.bg=PhotoImage(file="adv prog project\\maybelline_background.png")
    maybelline_image=Label(maybelline,image=maybelline.bg).place(x=0,y=0,relwidth=1,relheight=1)
    maybelline.geometry("1350x700+0+0")
    maybelline.resizable(width=False, height=False)
    
    product(maybelline, 10, 40, mbphoto1, 349, "Fit Me Matte Poreless Foundation", "Php.349")
    product(maybelline, 460, 40, mbphoto2,199, "Hyper Curl Mascara", "Php.199")
    product(maybelline, 910, 40, mbphoto3,249, "Line Tattoo Impact Pen", "Php.249")
    product(maybelline, 10, 450, mbphoto4, 399, "Instant Age Rewind Marvel Edition", "Php.399")
    product(maybelline, 460, 450, mbphoto5,399, "Falsies Lash Lift", "Php.399")
    product(maybelline, 910, 450, mbphoto6,299, "Superstay Matte Ink", "Php.299")
    
def Careline_Cosmetics(): #careline screen
    careline=Toplevel(main_screen)
    careline.title("HEALTH&COSMETICS")
    careline.bg=PhotoImage(file="adv prog project\\careline_background.png")
    careline.bg_image=Label(careline,image=careline.bg).place(x=0,y=0,relwidth=1,relheight=1)
    careline.geometry("1350x700+0+0")
    careline.resizable(width=False, height=False)

    product(careline, 50, 50, clphoto1, 110, "Oil Control Blush", "Php.110")
    product(careline, 500, 50, clphoto2, 299, "Soft Suede Lipstick", "Php.299")
    product(careline, 950, 50, clphoto3, 180, "Play to Slay Palette", "Php.180")
    product(careline, 50, 450, clphoto4, 170, "Skinny Mascara", "Php.170")
    product(careline, 500, 450, clphoto5, 100, "Lip & Cheek Tint", "Php.100")
    product(careline, 950, 450, clphoto6, 180, "Shadow Palette Color Paradise", "Php.180")
    
def EverBilena_Cosmetics(): #eb screen
    eb=Toplevel(main_screen)
    eb.title("HEALTH&COSMETICS")
    eb.bg=PhotoImage(file="adv prog project\\everbilena_background.png")
    eb_image=Label(eb,image=eb.bg).place(x=0,y=0,relwidth=1,relheight=1)
    eb.geometry("1350x700+0+0")
    eb.resizable(width=False, height=False)

    product(eb, 50, 50, ebphoto1, 225, "All Day Liquid Foundation", "Php.225")
    product(eb, 500, 50, ebphoto2, 399, "Beauty Set - City Romance", "Php.399")
    product(eb, 950, 50, ebphoto3, 195, "Kris Blush", "Php.195")
    product(eb, 50, 450, ebphoto4, 50, "Silky Brow Liner", "Php.50")
    product(eb, 500, 450, ebphoto5, 90, "Matte Lipstick", "Php.90")
    product(eb, 950, 450, ebphoto6, 93, "Brow Gel", "Php.93")
    
def Unilab_Health(): #unilab screen
    unilab=Toplevel(main_screen)
    unilab.title("HEALTH&COSMETICS")
    unilab.bg=PhotoImage(file="adv prog project\\unilab_background.png")
    unilab_image=Label(unilab,image=unilab.bg).place(x=0,y=0,relwidth=1,relheight=1)
    unilab.geometry("1350x700+0+0")
    unilab.resizable(width=False, height=False)

    product(unilab, 50, 50, ulphoto1, 7.50, "Bioflu Tablet 500 g", "Php.7.50")
    product(unilab, 500, 50, ulphoto2,129, "Solmux Forte 60ml", "Php.129")
    product(unilab, 950, 50, ulphoto3,29.75, "Dolfenal 500 mg", "Php.29.75")
    product(unilab, 50, 450, ulphoto4, 675, "Enervon 100 Tablets", "Php.675")
    product(unilab, 500, 450, ulphoto5,215, "Allerta 10 Tablets", "Php.215")
    product(unilab, 950, 450, ulphoto6,95, "Diatabs 12 Tablets", "Php.95")
    
def Centrum_Health(): #centrum screen
    centrum=Toplevel(main_screen)
    centrum.title("HEALTH&COSMETICS")
    centrum.bg=PhotoImage(file="adv prog project\\centrum_background.png")
    centrum_image=Label(centrum,image=centrum.bg).place(x=0,y=0,relwidth=1,relheight=1)
    centrum.geometry("1350x700+0+0")
    centrum.resizable(width=False, height=False)

    product(centrum, 50, 50, ctphoto1, 1580, "Centrum Men 112 tablets", "Php.1,580")
    product(centrum, 500, 50, ctphoto2, 1850, "Centrum Women 250 tablets", "Php.1,850")
    product(centrum, 950, 50, ctphoto3, 693, "Centrum Adult Liquid 236 mL", "Php.693")
    product(centrum, 50, 450, ctphoto4, 1450, "Centrum Adult Multivitamin\nSupplement 200 Tablets", "Php.1,450")
    product(centrum, 500, 450, ctphoto5, 1148, "Centrum Chewable Multivitamins\nfor Kids - 80 Tablets", "Php.1,148")
    product(centrum, 950, 450, ctphoto6, 989, "Centrum Silver Multivitamin Tablet", "Php.989")

def RiteMed_Health(): #ritemed screen
    ritemed=Toplevel(main_screen)
    ritemed.title("HEALTH&COSMETICS")
    ritemed.bg=PhotoImage(file="adv prog project\\ritemed_background.png")
    ritemed_image=Label(ritemed,image=ritemed.bg).place(x=0,y=0,relwidth=1,relheight=1)
    ritemed.geometry("1350x700+0+0")
    ritemed.resizable(width=False, height=False)

    product(ritemed, 50, 50, rmphoto1,50, "Isopropyl 70% Alcohol 250 mL", "Php.50")
    product(ritemed, 500, 50, rmphoto2,120, "Ambroxol 15mg syrup 120 mL", "Php.120")
    product(ritemed, 950, 50, rmphoto3,80, "Calming Relief Cream", "Php.80")
    product(ritemed, 50, 450, rmphoto4,113, "Amoxicillin 250 mg 60 mL", "Php.113")
    product(ritemed, 500, 450, rmphoto5,106, "Ascorbic Acid + Zinc 5 mL Syrup", "Php.106")
    product(ritemed, 950, 450, rmphoto6,148, "Hexetidine 120 mL", "Php.148")

def receipt(): 
        global total_price
        receipt=Toplevel(main_screen)
        receipt.title("Item Check Out")
        receipt.bg_image=Label(receipt,bg="pink").place(x=0,y=0,relwidth=1,relheight=1)
        receipt.geometry("455x300+0+0")
        receipt.resizable(width=False,height=False)

        total = str(total_price)
        Label(receipt,text="Total Amount to Pay:", font=60, bg="pink").place(x=150,y=20)
        Label(receipt,text=total_price, font=200, bg="pink").place(x=190,y=70) #display total price
        Label(receipt,text="Payment Amount", font=50, bg="pink").place(x=150,y=100)
        payment=Entry(receipt)
        payment.place(x=150,y=130)

        def checkout(): #checks if payment is enough and displays change
            cash=int(payment.get())
            if cash > total_price:
                change = cash-total_price
                tkr.messagebox.showinfo("CHECK OUT", "Your change is " + str(change) + ".\nThank you shopping!")
            else:
                tkr.messagebox.showerror("CHECK OUT", "Your Payment is insufficient\nPlease try again")

        checkout=Button(receipt, text="Check Out", command=checkout, bg='pink',fg='white',font = "calibri").place(x=170,y=200)

def Cart(): #cart screen
    global products
    global prices
    Cart=Toplevel(main_screen)
    Cart.title("Cart")
    Cart.bg_image=Label(Cart,bg="pink").place(x=0,y=0,relwidth=1,relheight=1)
    Cart.geometry("455x800+0+0")
    Cart.resizable(width=False,height=False)  

    def Removefromcart(): #removes item from cart and substract from total price
        try:
            global total_price
            i = itemincart.curselection()[0]
            itemincart.delete(i)
            item = products[i]
            itemprice = prices[i]
            total_price -= int(itemprice)
            products.remove(item)
            prices.remove(itemprice)
        except:
            tkinter.messagebox.showwarning(title="Cart",message="Select an item to remove")

    frame = Frame(Cart)
    frame.place(x=0,y=100)
    
    proccedbutton = Button(Cart, text="Proceed to Payment", command=receipt, bg='light green',fg='dark green',font = "calibri").place(x=10,y=50) 
    removebutton = Button(Cart, text="Remove Item", command=Removefromcart, bg='pink',fg='white',font = "calibri").place(x=350,y=50)

    itemincart = Listbox(frame, width=400, height=200, bg="pink", font=30)
    itemincart.pack(side=tkr.LEFT)

    x = 0
    for i in range(len(products)): #displays list of items added to cart
        item = str(products[x])
        price = str(prices[x])
        insertitem = item+"---------------------"+price
        itemincart.insert(END, insertitem)
        x += 1
        
    Label(Cart, text="My Cart", bg="pink", font=50).place(x=200,y=5)

def Succesful_Account(): #screen appear on successful login
    Succesful_screen=Toplevel(main_screen)
    Succesful_screen.title("Window 1")
    Succesful_screen.bg=PhotoImage(file="adv prog project\\succesful_account background.png")
    Succesful_screen.bg_image=Label(Succesful_screen,image=Succesful_screen.bg).place(x=0,y=0,relwidth=1,relheight=1)
    Succesful_screen.geometry("1300x690+0+0")
    Succesful_screen.resizable(width=False, height=False)

    def logout(): 
        Succesful_screen.destroy()
        main_screen.deiconify() 

    button1 = PhotoImage(file="adv prog project\\maybelline_logo.png")
    Label1 = Label(Succesful_screen, image=button1)
    Label1.image = button1
    Button1 = Button(Succesful_screen, image = button1, bd = 0, command=Maybelline_Cosmetics)
    Button1.place(x=650,y=100)
    button2 = PhotoImage(file="adv prog project\\careline_logo.png")
    Label2 = Label(Succesful_screen, image=button2)
    Label2.image = button2
    Button2 = Button(Succesful_screen, image = button2, bd = 0, command=Careline_Cosmetics)
    Button2.place(x=880,y=100)
    button3 = PhotoImage(file="adv prog project\\everbilena_logo.png")
    Label3 = Label(Succesful_screen, image=button3)
    Label3.image = button3
    Button3 = Button(Succesful_screen, image = button3, bd = 0,command=EverBilena_Cosmetics)
    Button3.place(x=1100,y=100)
    button4 = PhotoImage(file="adv prog project\\unilab_logo.png")
    Label4 = Label(Succesful_screen, image=button4)
    Label4.image = button4
    Button4 = Button(Succesful_screen, image = button4, bd = 0,command=Unilab_Health)
    Button4.place(x=650,y=400)
    button5 = PhotoImage(file="adv prog project\\centrum_logo.png")
    Label5 = Label(Succesful_screen, image=button5)
    Label5.image = button5
    Button5 = Button(Succesful_screen, image = button5, bd = 0, command=Centrum_Health)
    Button5.place(x=880,y=400)
    button6= PhotoImage(file="adv prog project\\ritemed_logo.png")
    Label6 = Label(Succesful_screen, image=button6)
    Label6.image = button6
    Button6 = Button(Succesful_screen, image = button6, bd = 0,command=RiteMed_Health)
    Button6.place(x=1100,y=400)
    logoutbutton = Button(Succesful_screen,text="Logout",bg='pink',fg='white',font = "calibri", command=logout)
    logoutbutton.place(x=1230,y=5)
    cartbutton = Button(Succesful_screen,text="Cart",bg='pink',fg='white',font = "calibri", command=Cart)
    cartbutton.place(x=1180,y=5)

def user_not_found():
    user_not_found_scrn=Toplevel(main_screen)
    user_not_found_scrn.title("HEALTH&COSMETICS")
    user_not_found_scrn.geometry("250x210")
    Label(user_not_found_scrn,text="USER NOT FOUND",fg="pink",font = "calibri").place(x=70,y=80)
    Button(user_not_found_scrn,text="OK",width = 5,height = 1,bg="pink",fg="white",command=closebtn).place(x=100,y=120)

    def closebtn():
        user_not_found_scrn.destroy()

def Login_user(): #checks if username and password are accounts
    Username=username1.get()
    passwrd=password1.get()
    usrnm.delete(0,END)
    passw.delete(0,END)
    list_of_dir=os.listdir()
    if Username in list_of_dir:
        file1=open(Username,"r")
        verify=file1.read()
        if passwrd != verify:
            user_not_found()    
        else:
            Succesful_Account()
            main_screen.withdraw()
    else:
        user_not_found()   

def CreateAccount():
    def CreateAccount_user():
        name1=Username.get()
        pass1=Password.get()
        file=open(name1,"w")
        file.write(pass1)
        file.close()
        Username2.delete(0,END)
        Password2.delete(0,END)
        tkr.messagebox.showinfo("Account", "Account Successfully created")

    CreateAccount_screen=Toplevel(main_screen)
    CreateAccount_screen.title("Sign Up")
    CreateAccount_screen.geometry("500x550")
    Label(CreateAccount_screen,text="Create Account",height="2",width="300",fg="#D98880",bg = "#FFB6C1",font = "calibri").pack()
    Label(text="").pack()
    Label(CreateAccount_screen,text="FirstName:", height="1", width="20", fg="black", font = "calibri").place(x=10,y=50)
    Label(CreateAccount_screen,text="LastName:", height="1", width="20", fg="black", font = "calibri").place(x=250,y=50)
    Label(CreateAccount_screen,text="Username:", height="1", width="20", fg="black", font = "calibri").place(x=1,y=130)
    Label(CreateAccount_screen,text="Password:", height="1", width="20", fg="black", font = "calibri").place(x=3,y=200)
    Label(CreateAccount_screen,text="Address:", height="1", width="20", fg="black", font = "calibri").place(x=3,y=270)
    Label(CreateAccount_screen,text="Contact Number:", height="1", width="20", fg="black", font = "calibri").place(x=20,y=350)

    FirstName=StringVar()
    FirstName1=Entry(CreateAccount_screen,textvariable=FirstName)
    FirstName1.place(x=50,y=100)
    LastName=StringVar()
    Username=StringVar()
    Password=StringVar()
    Address=StringVar()
    ContactNumber=StringVar()
    LastName2=Entry(CreateAccount_screen,textvariable=LastName)
    LastName2.place(x=300,y=100)
    Username2=Entry(CreateAccount_screen,textvariable=Username, width="62")
    Username2.place(x=50,y=170)
    Password2=Entry(CreateAccount_screen,textvariable=Password)
    Password2.place(x=50,y=240)
    Address2=Entry(CreateAccount_screen,textvariable=Address, width="62")
    Address2.place(x=50,y=310)
    ContactNumber2=Entry(CreateAccount_screen,textvariable=ContactNumber)
    ContactNumber2.place(x=50,y=390)
    Button(CreateAccount_screen,text= "Sign Up", height="1", width="7", bg="pink", fg="white", font = "calibri", command = CreateAccount_user).place(x = 210, y = 450)
 
def Exit():
    Exit = tkr.messagebox.askyesno ("HEALTH&COSMETICS", "Do you really want to Exit?")
    if Exit > 0: 
        main_screen.destroy()
        return

main_screen=Tk() #Log in screen
main_screen.geometry("1300x700+0+0")   
main_screen.title("HEALTH&COSMETICS")
main_screen.bg=PhotoImage(file="adv prog project\\mainscreen background.png")
main_screen.bg_image=Label(main_screen,image=main_screen.bg).place(x=0,y=0,relwidth=1,relheight=1)
Label(main_screen,text="USERNAME:",height="1", width="15", bg="#FFB6C1", fg="white", font = "calibri").place(x=170, y=350)
username1=StringVar()
usrnm=Entry(main_screen, textvariable=username1)
usrnm.place(x=320, y=350, height="25", width="160") 
Label(main_screen,text="PASSWORD:",height="1", width="15", bg="#FFB6C1", fg="white", font = "calibri").place(x=170, y=400)
password1=StringVar()
passw=Entry(main_screen, textvariable=password1, show='*')
passw.place(x=320, y=400, height="25", width="160")
Button(text = "Login", height="1", width="7", bg="#FFB6C1", fg="white", font = "calibri", command = Login_user).place(x = 270, y = 450)
Label(text="").pack()
Button(text = "Create Account", height="1", width="15", bg="#FFB6C1", fg="white", font = "calibri", command = CreateAccount).place(x = 240, y = 500)
Label(text="").pack()
Button(text="X", height="1",width="2", bg ="#FFB6C1", fg = "white", font = "calibri" , command=Exit).place(x = 1300, y = 40)

#cosmetic item images
mbphoto1 = PhotoImage(file = "adv prog project\\maybellinefoundation_img.png")
mbphoto2 = PhotoImage(file = "adv prog project\\maybellinemascara_img.png")
mbphoto3 = PhotoImage(file = "adv prog project\\maybellineeyeliner_img.png")
mbphoto4 = PhotoImage(file = "adv prog project\\maybellineconcealer_img.png")
mbphoto5 = PhotoImage(file = "adv prog project\\maybellinemascara2_img.png")
mbphoto6 = PhotoImage(file = "adv prog project\\maybellineliquidlipstick_img.png")

clphoto1 = PhotoImage(file = "adv prog project\\carelineblush_img.png")
clphoto2 = PhotoImage(file = "adv prog project\\carelinelipstick_img.png")
clphoto3 = PhotoImage(file = "adv prog project\\carelinepalette_img.png")
clphoto4 = PhotoImage(file = "adv prog project\\carelinemascara_img.png")
clphoto5 = PhotoImage(file = "adv prog project\\carelinetint_img.png")
clphoto6 = PhotoImage(file = "adv prog project\\carelinepalette2_img.png")

ebphoto1 = PhotoImage(file = "adv prog project\\everbilenaliquidfoundation_img.png")
ebphoto2 = PhotoImage(file = "adv prog project\\everbilenaliquidlipstick_img.png")
ebphoto3 = PhotoImage(file = "adv prog project\\everbilenapinkpowder_img.png")
ebphoto4 = PhotoImage(file = "adv prog project\\everbilenabrowliner_img.png")
ebphoto5 = PhotoImage(file = "adv prog project\\everbilenamattelipstick_img.png")
ebphoto6 = PhotoImage(file = "adv prog project\\everbilenabrowgel_img.png")

#health item images
ulphoto1 = PhotoImage(file = "adv prog project\\unilabbioflu_img.png")
ulphoto2 = PhotoImage(file = "adv prog project\\unilabsolmux_img.png")
ulphoto3 = PhotoImage(file = "adv prog project\\unilabacid_img.png")
ulphoto4 = PhotoImage(file = "adv prog project\\unilabenervon_img.png")
ulphoto5 = PhotoImage(file = "adv prog project\\unilaballerta_img.png")
ulphoto6 = PhotoImage(file = "adv prog project\\unilabdiatabs_img.png")

ctphoto1 = PhotoImage(file = "adv prog project\\centrummen_img.png")
ctphoto2 = PhotoImage(file = "adv prog project\\centrumwomen_img.png")
ctphoto3 = PhotoImage(file = "adv prog project\\centrumliquid_img.png")
ctphoto4 = PhotoImage(file = "adv prog project\\centrumvitamin_img.png")
ctphoto5 = PhotoImage(file = "adv prog project\\centrumkids_img.png")
ctphoto6 = PhotoImage(file = "adv prog project\\centrumsilver_img.png")

rmphoto1 = PhotoImage(file = "adv prog project\\ritemedalcohol_img.png")
rmphoto2 = PhotoImage(file = "adv prog project\\ritemedambroxol_img.png")
rmphoto3 = PhotoImage(file = "adv prog project\\ritemedcream_img.png")
rmphoto4 = PhotoImage(file = "adv prog project\\ritemedamox_img.png")
rmphoto5 = PhotoImage(file = "adv prog project\\ritemedzinc_img.png")
rmphoto6 = PhotoImage(file = "adv prog project\\ritemedhex_img.png")

main_screen.mainloop()
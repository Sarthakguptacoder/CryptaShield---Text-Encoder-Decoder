from tkinter import *
from tkinter import messagebox
import base64

screen = Tk()
screen.geometry("420x420")
screen.title("cryptashield")
screen.configure(bg="Grey")
def encrypt():
    password=code.get()
    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("Encrypted By Cryptashield")
        screen.geometry("400x250")
        screen1.configure(bg="pink")
        
        message=text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")
        #label
        Label(screen1, text="Your Text Is Encrypted",font="impack 10 bold").place(x=5,y=6)
        #text
        text2 = Text(screen1,font="30",bd=4,wrap=WORD)
        text2.place(x=2,y=30,width=390,height=180)
        #insert
        text2.insert(END,encrypt)
    elif (password==""):
        messagebox.showerror("error","Please Enter The Secret Key")
    elif(password!="1234"):
        messagebox.showerror("Oops","Invailid Secret Key")
def decrypt():
    password=code.get()
    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("Decrypted By Cryptashield")
        screen.geometry("400x250")
        screen2.configure(bg="orange")
        
        message=text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(encode_message)
        encrypt = base64_bytes.decode("ascii")
        #label
        Label(screen2, text="Your Text Is Encrypted",font="impack 10 bold").place(x=5,y=6)
        #text
        text2 = Text(screen2,font="30",bd=4,wrap=WORD)
        text2.place(x=2,y=30,width=390,height=180)
        #insert
        text2.insert(END,encrypt)
    elif (password==""):
        messagebox.showerror("error","Please Enter The Secret Key")
    elif(password!="1234"):
        messagebox.showerror("Oops","Invailid Secret Key")
def reset():
    text1.delete(1.0,END)
    code.set("")

    
#label
Label(screen,text="Enter the text for encryption and decryption",font="areal 14 bold", bg="GREEN").place(x=5, y=6)
#text
text1=Text(screen, font="20")
text1.place(x=5, y=45, width=410, height=120)
#label
Label(screen,text="Enter The Secret Key", font="areal 13 bold").place(x=120,y=185)
#Entry
code=StringVar()
Entry(textvariable=code,bd=4,font="20",show="*").place(x=95,y=220)
#botton
Button(screen,text="Encrypt",font="arial 15 bold",bg="red",fg="white",command=encrypt).place(x=15,y=280,width=180)
Button(screen,text="Decrypt",font="arial 15 bold",bg="blue",fg="white",command=decrypt).place(x=220,y=280,width=180)
Button(screen,text="Reset",font="arial 15 bold",bg="green",fg="white",command=reset).place(x=80,y=350,width=240)
mainloop()

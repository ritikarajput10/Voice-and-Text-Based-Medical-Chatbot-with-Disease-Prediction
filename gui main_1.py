from tkinter import *
import tkinter as tk


from PIL import Image ,ImageTk

from tkinter.ttk import *   #tkinter theames
from pymsgbox import *      #tkinter alerts


#root file

root=tk.Tk()

root.title(" ")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

image2 =Image.open('guimain1.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="skyblue")


from tkinter import messagebox as ms



#define funstions

def chatbot1(): 
        root.destroy()#it is for disease prediction
        from subprocess import call
        call(["python","GUI_Master.py"])



def chatbot():    #for actual chatbot
    root.destroy()
    from subprocess import call
    call(["python","CHAT_1.py"])
    

    
def window():
    root.distroy()
    
#top lable and centre frame

lbl = tk.Label(root, text="Traffic Sign and Ambulance..!", font=('times', 35,' bold '), width=50,height=1,bg="#131e3a",fg="white")
lbl.place(x=0, y=0)



label1 = tk.Label(root, text="WE CARE", font=('times', 45, 'bold'), bg="#bfe8ec", fg="white")
label1.place(x=120, y=100+30)

label2 = tk.Label(root, text="YOUR HEALTH!", font=('times', 45, 'bold'), bg="#bfe8ec", fg="#131e3a")
label2.place(x=120, y=200)

label2 = tk.Label(root, text="“ An ambulance is a vehicle used to transport people who are sick or injured.", font=('times', 15), bg="#bfe8ec", fg="#2e777b")
label2.place(x=80, y=300)



    
d2=tk.Button(root,text="Traffic Sign",command=chatbot1   ,width=15,height=2,bd=2,background="#131e3a",foreground="white",font=("times new roman",14,"bold"))
d2.place(x=120,y=450)
d2=tk.Button(root,text="Ambulance",command=chatbot,width=15,height=2,bd=2,background="#131e3a",foreground="white",font=("times new roman",14,"bold"))
d2.place(x=120,y=550)



 



root.mainloop()

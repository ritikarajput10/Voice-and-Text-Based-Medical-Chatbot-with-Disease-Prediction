import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time


global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

image2 =Image.open('dr4.jpg')
image2 = image2.resize((1600, 800), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=-50, y=0)


root.title(" Disease Prediction System")


#top bar

label_l1 = tk.Label(root, text=" Disease Prediction System",font=("Times New Roman", 35, 'bold'),
                    background="#131e3a", fg="white", width=60, height=1,bd=0)
label_l1.place(x=-30, y=0)


#img1 = ImageTk.PhotoImage(Image.open("hd.jpg"))

#img2 = ImageTk.PhotoImage(Image.open("h11.jpg"))

#img3 = ImageTk.PhotoImage(Image.open("db1.jpeg"))


logo_label = tk.Label()
logo_label.place(x=400, y=200)


#making the changing images
#x = 1

#def move():
	#global x
	#if x == 4:
	#	x = 1
	#if x == 1:
	#	logo_label.config(image=img1)
	#elif x == 2:
	#	logo_label.config(image=img2)
	#elif x == 3:
	#	logo_label.config(image=img3)

	#x = x+1
	#root.after(1000, move)

# calling the function
#move()




#funstions
    
def heart():
          
        
        from subprocess import call
        call(["python","Check_Heart.py"])   #using pretrained models, detects disease or not

def dia():
    
    from subprocess import call
    call(["python","Diabetes1.py"])
    
def window():
    root.destroy()
    from subprocess import call
    call(["python","gui main_1.py"])
    


button2 = tk.Button(root, text="HEART",command=heart,width=14, height=1,font=('times', 20, ' bold '),bd=5, bg="#152238", fg="white")
button2.place(x=530, y=240+48)

button3 = tk.Button(root, text="DIABETES",command=dia,width=14, height=1,font=('times', 20, ' bold '),bd=5, bg="#152238", fg="white")
button3.place(x=530, y=320+58)

button4 = tk.Button(root, text="Exit!",command=window,width=14, height=1,font=('times', 20),bd=0, bg="#dedfe9", fg="#152238")
button4.place(x=530, y=400+70)

root.mainloop()
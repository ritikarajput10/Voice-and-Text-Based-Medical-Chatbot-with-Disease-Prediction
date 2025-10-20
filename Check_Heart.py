from tkinter import *
def Train():
    import tkinter as tk
    import numpy as np
    import pandas as pd

    from sklearn.decomposition import PCA    #dimensionality reduction for feature extraction and visualization of high-dimensional data
    from sklearn.preprocessing import LabelEncoder   #used for encoding categorical labels (classes) into numerical values

    #root file
    root = tk.Tk()

    root.geometry("800x850+250+5")
    root.title("Check Heart Disease")
    root.configure(background="#9a7b4f")
    
    age = tk.IntVar()
    sex = tk.IntVar()
    chest_pain = tk.IntVar()
    restbp = tk.IntVar()
    chol = tk.IntVar()
    fbs = tk.IntVar()
    restecg = tk.IntVar()
    maxhr = tk.IntVar()
    exang = tk.IntVar()
    oldpeak = tk.DoubleVar()
    slope = tk.IntVar()
    ca = tk.IntVar()
    thal = tk.IntVar()
    
    frame_display = tk.LabelFrame(root, text=" --Display-- ", width=600, height=500, bd=5, font=('times', 14, ' bold '),bg="gray")
    frame_display.grid(row=0, column=0, sticky='nw')
    frame_display.place(x=700, y=100)
    
    lbl = tk.Label(root, text="Chestpain=1. Typical 2. Atypical 3.Nontypical \n RestBp=80 to 120 \n Cholestrol=200 to 240 \n Fasting Blood Sugar=Low and high \n RestECG= Low(0) And High(1) \n Average= 220-age  \n Exang= 0 And 1 \n Old peak=1 to 3 \n Slope= 1,2,3 \n Ca=0,1,2,3 \n Thal= Fixed , Normal ,Reversable \n AHD=yes,no"  , font=('times', 14,' bold '), width=35,height=12,bg="gray",fg="white")
    lbl.place(x=800, y=160)
    
    
    #===================================================================================================================
    def window():
      root.destroy()
      from subprocess import call
      call(["python","main.py"])

    def Detect():
        
        
   
        e1=age.get()
        print(e1)
        e2=sex.get()
        print(e2)  
        e3=chest_pain.get()
        print(e3)
        e4=restbp.get()
        print(e4)
        e5=chol.get()
        print(e5)
        e6=fbs.get()
        print(e6)
        e7=restecg.get()
        print(e7)
        e8=maxhr.get()
        print(e8)
        e9=exang.get()
        print(e9)
        e10=oldpeak.get()
        print(e10)
        e11=slope.get()
        print(e11)
        e12=ca.get()
        print(e12)
        e13=thal.get()
        print(e13)
        #########################################################################################
        
        #pretrained model heart_disease_model.joblib(a1) is used for prediction
        from joblib import dump , load
        a1=load(r'HEART_DISEASE_MODEL.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9,e10, e11, e12, e13]])
        print(v)    #1 is have disease, 0 means not
        if v[0]==1:
            print("Yes")
            yes = tk.Label(root,text="Disease \nDetected!\nReport is Generated",background="red",foreground="white",font=('times', 20, ' bold '),width=15)
            yes.place(x=300,y=100)
            
            label_l1 = tk.Label(root, text="LIST OF RECOMMENDED DOCTORS\n\n  1.Dr. Khurana (9090909090) \n\n  2.Dr. Jadhav (7070707070)\n\n 3.Dr. Pawar (7878787878)\n\n 4.Dr. Tikone (9191919191)",font=("Times New Roman", 22, 'bold'),
                                background="#152238", fg="white", width=30, height=10)
            label_l1.place(x=700, y=10)
            
            
            file = open(r"Report.txt", 'w')
            file.write("-----Patient Report-----\n As per input data and system model Heart Disease Detected for Respective Paptient."
                       "\n***Kindly Follow Medicatins***"
                       
                    
                    )
            file.close()
            
        else:
            print("No")
            no = tk.Label(root, text="No Disease \nDetected", background="green", foreground="white",font=('times', 20, ' bold '),width=15)
            no.place(x=500, y=100)
            file = open(r"Report.txt", 'w')
            file.write("-----Patient Report-----\n As per input data and system model No Heart Disease Detected for Respective Paptient."
                       "\n\n***Relax and Follow below mentioned Life Style to be Healthy as You Are!!!***"
                        
                    
                    )
            file.close()
      



    l1=tk.Label(root,text="Age",background="#9a7b4f",font=('times', 20, ' bold '),width=10)
    l1.place(x=5,y=1)
    age=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=age)
    age.place(x=200,y=1)

    l2=tk.Label(root,text="Sex",background="#9a7b4f",font=('times', 20, ' bold '),width=10)
    l2.place(x=5,y=50)
    R1 = Radiobutton(root, text="Male", variable=sex, value=0).place(x=200,y=50)
    R2 = Radiobutton(root, text="Female", variable=sex, value=1).place(x=300,y=50)
    #R3 = Radiobutton(root, text="nontypical", variable=chest_pain, value=3).place(x=200,y=140)

    #sex=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=sex)
    #sex.place(x=200,y=50)

    l3=tk.Label(root,text="Chest Pain",background="#9a7b4f",font=('times', 20, ' bold '),width=10)
    l3.place(x=5,y=100)
   
    R1 = Radiobutton(root, text="Typical", variable=chest_pain, value=1).place(x=200,y=100)
    R2 = Radiobutton(root, text="asymptomatic", variable=chest_pain, value=2).place(x=200,y=120)
    R3 = Radiobutton(root, text="nontypical", variable=chest_pain, value=3).place(x=200,y=140)

    l4=tk.Label(root,text="RestBP",background="#9a7b4f",font=('times', 20, ' bold '),width=10)
    l4.place(x=5,y=150)
    restbp=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=restbp)
    restbp.place(x=200,y=160)

    l5=tk.Label(root,text="Chol",background="#9a7b4f",font=('times', 20, ' bold '),width=10)
    l5.place(x=5,y=200)
    chol=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=chol)
    chol.place(x=200,y=200)

    l6=tk.Label(root,text="FBS",background="#9a7b4f",font=('times', 20, ' bold '),width=10)
    l6.place(x=5,y=250)
    fbs=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20))
    fbs.place(x=200,y=250)

    l7=tk.Label(root,text="RestECG",background="#9a7b4f",font=('times', 20, ' bold '),width=10)
    l7.place(x=5,y=300)
    restecg=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=restecg)
    restecg.place(x=200,y=300)

    l8=tk.Label(root,text="MaxHR",background="#9a7b4f",font=('times', 20, ' bold '),width=10)
    l8.place(x=5,y=350)
    maxhr=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=maxhr)
    maxhr.place(x=200,y=350)

    l9=tk.Label(root,text="ExANG",background="#9a7b4f",font=('times', 20, ' bold '),width=10)
    l9.place(x=5,y=400)
    exang=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=exang)
    exang.place(x=200,y=400)

    l10=tk.Label(root,text="Old Peak",background="#9a7b4f",font=('times', 20, ' bold '),width=10)
    l10.place(x=5,y=450)
    oldpeak=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=oldpeak)
    oldpeak.place(x=200,y=450)

    l11=tk.Label(root,text="Slope",background="#9a7b4f",font=('times', 20, ' bold '),width=10)
    l11.place(x=5,y=500)
    slope=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=slope)
    slope.place(x=200,y=500)

    l12=tk.Label(root,text="Ca",background="#9a7b4f",font=('times', 20, ' bold '),width=10)
    l12.place(x=5,y=550)
    ca=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=ca)
    ca.place(x=200,y=550)

    l13=tk.Label(root,text="Thal",background="#9a7b4f",font=('times', 20, ' bold '),width=10)
    l13.place(x=5,y=600)
    R4 = Radiobutton(root, text="Fixed", variable=thal, value=1).place(x=200,y=600)
    R5 = Radiobutton(root, text="normal", variable=thal, value=2).place(x=200,y=620)
    R6 = Radiobutton(root, text="reversable", variable=thal, value=3).place(x=200,y=640)

    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=500,y=300)
    

    
    button1 = tk.Button(root,text="Back",command=window,font=('times', 20, ' bold '),width=7)
    button1.place(x=1000,y=10)


    root.mainloop()

Train()
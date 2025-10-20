def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd

    from sklearn.decomposition import PCA    #dimentioanlity reduction
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    root.geometry("500x650+800+5")
    root.title("Check Disease")
    root.configure(background="#9a7b4f")
    
 
    
    Glucose=tk.IntVar()
    Blood_Pressure=tk.IntVar()
    Insulin=tk.IntVar()
    DiabetesPedigreeFunction=tk.IntVar()
    Age=tk.IntVar()
    
    frame_display = tk.LabelFrame(root, text=" --Display-- ", width=500, height=300, bd=5, font=('times', 14, ' bold '),bg="gray")
    frame_display.grid(row=0, column=0, sticky='nw')
    frame_display.place(x=700, y=100)
    
    lbl = tk.Label(root, text="Glucose=84 to 140 \n BP= 80 to 120 \n Insulin= \n DiabetesPedigreeFunction="  , font=('times', 14,' bold '), width=20,height=4,bg="gray",fg="white")
    lbl.place(x=730, y=160)
    
    #===================================================================================================================
       
    def window():
       root.destroy()
       from subprocess import call
       call(["python","main.py"])
    
    def Detect():
        e1=Glucose.get()
        e2=Blood_Pressure.get()
        e3=Insulin.get()
        e4=DiabetesPedigreeFunction.get()
        e5=Age.get()
        
        

        from joblib import dump , load
        a1=load("RF_MODEL.joblib")
        v= a1.predict([[e1,e2,e3,e4, e5]])
        if v[0]==1:
            print("Yes")
            yes = tk.Label(root,text="Disease Detected",background="red",foreground="white",font=('times', 20, ' bold '),width=20)
            yes.place(x=50,y=500)
            
            label_l1 = tk.Label(root, text="LIST OF RECOMMENDED DOCTORS\n\n  1.Dr. Wadia (8181818181) \n\n  2.Dr. Sahara (8282828282)\n\n 3.Dr. Gupta (7878787878)\n\n 4.Dr. Khamkar (8585858585)",font=("Times New Roman", 22, 'bold'),
                                background="#152238", fg="white", width=30, height=10)
            label_l1.place(x=700, y=10)
            
            report_file = open(r"Report.txt","w")
            report_file.write("----Patient Report---- \nStatus : Diabetes Detected \n\n****Immidiately Visit Doctor For Consultation.****\n")
            report_file.close()
        else:
            print("No")
            no = tk.Label(root, text="No Disease Detected", background="green", foreground="white",font=('times', 20, ' bold '),width=20)
            no.place(x=50, y=500)
            report_file = open(r"Report.txt","w")
            report_file.write("----Patient Report---- \nStatus : No Diabetes Detected \n\n****")
            report_file.close()





    
    l1=tk.Label(root,text="Glucose",background="#9a7b4f",font=('times', 20, ' bold '),width=14)
    l1.place(x=10,y=50)
    Glucose=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Glucose)
    Glucose.place(x=400,y=50)

    

    l3=tk.Label(root,text="Blood Pressure",background="#9a7b4f",font=('times', 20, ' bold '),width=14)
    l3.place(x=10,y=100)
    Blood_Pressure=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Blood_Pressure)
    Blood_Pressure.place(x=400,y=100)

    l4=tk.Label(root,text="Insulin",background="#9a7b4f",font=('times', 20, ' bold '),width=14)
    l4.place(x=10,y=150)
    Insulin=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Insulin)
    Insulin.place(x=400,y=150)

    l5=tk.Label(root,text="DiabetesPedigreeFunction",background="#9a7b4f",font=('times', 20, ' bold '),width=20)
    l5.place(x=10,y=200)
    DiabetesPedigreeFunction=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=DiabetesPedigreeFunction)
    DiabetesPedigreeFunction.place(x=400,y=200)

    l6=tk.Label(root,text="Age",background="#9a7b4f",font=('times', 20, ' bold '),width=14)
    l6.place(x=10,y=250)
    Age=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Age)
    Age.place(x=400,y=250)

    

    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=200,y=400)
    
    button1 = tk.Button(root,text="Back",command=window,font=('times', 20, ' bold '),width=7)
    button1.place(x=1000,y=10)


    root.mainloop()

Train()
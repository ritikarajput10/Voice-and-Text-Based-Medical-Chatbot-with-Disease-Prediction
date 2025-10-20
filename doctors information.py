import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

from PIL import Image ,ImageTk

from tkinter.ttk import *   #tkinter theames

class DoctorAppointmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor Appointment Booking System")
    
        # Connect to the SQLite database
        self.conn = sqlite3.connect('doctor_appointments.db')
        self.cur = self.conn.cursor()
    
        # Create tables if they don't exist
        self.create_tables()
    
        # Fetch locations and diseases from the database
        self.locations = self.fetch_locations()
        self.diseases = self.fetch_diseases()
    
        # Variables to store user selections
        self.selected_location = tk.StringVar()
        self.selected_disease = tk.StringVar()
        self.selected_doctor = tk.StringVar()
        self.doctor_email = tk.StringVar()
        
        # Create a frame in the center of the window
        self.center_frame = tk.Frame(root)
        self.center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
        # Configure the frame background
        self.center_frame.configure(background="white", width=600, height=400, bd=5)
    
        # Create labels for location and disease
        tk.Label(self.center_frame, text="Select Location:", font=('times', 20, 'bold'), bg="#bfe8ec", fg="white", height=1, width=15).grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.center_frame, text="Enter Disease:", font=('times', 20, 'bold'), bg="#bfe8ec", fg="white", height=1, width=15).grid(row=1, column=0, padx=10, pady=10)
    
        # Create location dropdown
        self.location_dropdown = ttk.Combobox(self.center_frame, textvariable=self.selected_location, values=self.locations, font=('times', 20, 'bold'), height=1, width=15)
        self.location_dropdown.grid(row=0, column=1, padx=10, pady=10)
        self.location_dropdown.set("Select")
    
        # Create disease entry
        self.disease_entry = ttk.Combobox(self.center_frame, textvariable=self.selected_disease, values=self.diseases, font=('times', 20, 'bold'), height=1, width=15)
        self.disease_entry.grid(row=1, column=1, padx=10, pady=10)
    
        # Create button to fetch doctors
        tk.Button(self.center_frame, text="Fetch Doctors", command=self.fetch_doctors, font=('times', 20, 'bold'), bg="#bfe8ec", fg="white", height=1, width=15).grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    
        # Create labels for doctors
        tk.Label(self.center_frame, text="Select Doctor:", font=('times', 20, 'bold'), bg="#bfe8ec", fg="white", height=1, width=15).grid(row=3, column=0, padx=10, pady=10)
    
        # Create doctor dropdown
        self.doctor_dropdown = ttk.Combobox(self.center_frame, textvariable=self.selected_doctor, font=('times', 20, 'bold'), height=1, width=15)
        self.doctor_dropdown.grid(row=3, column=1, padx=10, pady=10)
        self.doctor_dropdown.set("Select")
        # Bind the selection event for the doctor dropdown
        self.doctor_dropdown.bind("<<ComboboxSelected>>", self.update_doctor_email)
    
        # # Create entry for doctor email
        # tk.Label(self.center_frame, text="Doctor's Email:", font=('times', 20, 'bold'), bg="#bfe8ec", fg="white", height=1, width=15).grid(row=4, column=0, padx=10, pady=10)
        # self.doctor_email_entry = tk.Entry(self.center_frame, textvariable=self.doctor_email, font=('times', 20, 'bold'), width=15)
        # self.doctor_email_entry.grid(row=4, column=1, padx=10, pady=10)
    
        # Create button to book appointment
        tk.Button(self.center_frame, text="Book Appointment", command=self.book_appointment, font=('times', 20, 'bold'), bg="#bfe8ec", fg="white", height=1, width=15).grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
        # Create button to go back
        tk.Button(root, text="Back", command=self.back, font=('times', 20, 'bold'), bg="#bfe8ec", fg="white", height=1, width=15).place(relx=0.5, rely=0.9, anchor=tk.CENTER)
            

    def create_tables(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS locations (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL)''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS diseases (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL)''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS doctors (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            location_id INTEGER,
                            disease_id INTEGER,
                            Email TEXT,
                            FOREIGN KEY(location_id) REFERENCES locations(id),
                            FOREIGN KEY(disease_id) REFERENCES diseases(id))''')

        self.conn.commit()
        
    def back(self):
        self.root.destroy()     #for boockingappointment
        from subprocess import call
        call(["python","gui main_1.py"])

    def fetch_locations(self):
        self.cur.execute("SELECT name FROM locations")
        return [row[0] for row in self.cur.fetchall()]

    def fetch_diseases(self):
        self.cur.execute("SELECT name FROM diseases")
        return [row[0] for row in self.cur.fetchall()]

    def fetch_doctors(self):
        location = self.selected_location.get()
        disease = self.selected_disease.get()

        if location and disease:
            doctors_for_location_and_disease = self.fetch_doctors_for_location_and_disease(location, disease)
            if doctors_for_location_and_disease:
                self.doctor_dropdown["values"] = [doctor[0] for doctor in doctors_for_location_and_disease]
                self.doctor_dropdown.set("Select")
                self.update_doctor_email(None)  # Update the email entry with the first doctor's email
                messagebox.showinfo("Success", "Doctors Fetched Successfully.")
            else:
                messagebox.showwarning("Warning", "No doctors found for the selected location and disease.")
        else:
            messagebox.showwarning("Warning", "Please select location and enter disease.")

    def fetch_doctors_for_location_and_disease(self, location, disease):
        self.cur.execute("SELECT name, Email FROM doctors WHERE location_id = (SELECT id FROM locations WHERE name = ?) AND disease_id = (SELECT id FROM diseases WHERE name = ?) ", (location, disease))
        return self.cur.fetchall()

    def book_appointment(self):
        location = self.selected_location.get()
        disease = self.selected_disease.get()
        doctor = self.selected_doctor.get()
        doctor_email = self.doctor_email.get()

        if location and disease and doctor:
            messagebox.showinfo("Success", f"Appointment booked with {doctor} at {location} for {disease}.")
            messagebox.showinfo("Success", f"Mail Send")
            # Here, you would typically save the appointment details to a database, including doctor's email.
        else:
            messagebox.showwarning("Warning", "Please select location, enter disease, and select a doctor.")

    def back(self):
        self.root.destroy()  # Close the current window

    def update_doctor_email(self, event):
        # Event handler to update the doctor's email entry when the doctor selection changes
        selected_doctor = self.selected_doctor.get()
        location = self.selected_location.get()
        disease = self.selected_disease.get()

        if selected_doctor and location and disease:
            doctor_email = self.fetch_doctor_email(selected_doctor, location, disease)
            self.doctor_email.set(doctor_email)

    def fetch_doctor_email(self, selected_doctor, location, disease):
        self.cur.execute("SELECT Email FROM doctors WHERE name = ? AND location_id = (SELECT id FROM locations WHERE name = ?) AND disease_id = (SELECT id FROM diseases WHERE name = ?)", (selected_doctor, location, disease))
        result = self.cur.fetchone()
        
        if result:
            
            print(result[0])
            location = self.selected_location.get()
            disease = self.selected_disease.get()
            doctor = self.selected_doctor.get()
            doctor_email = self.doctor_email.get()
            
            
            
            if location and disease and doctor:
                
                f1 = open("id.txt","r")
                id1 = f1.read()
                print(id1)
                f1.close()
                
                db = sqlite3.connect('evaluation.db')
                cursor = db.cursor()
               
                find_entry = ('SELECT Fullname,Phoneno FROM admin_registration WHERE id = ? ')
                cursor.execute(find_entry, [(id1)])
                result1 = cursor.fetchall()
                name=list(result1)
                print(str(name[0]))
            
                import smtplib
                from email.message import EmailMessage
                import imghdr
    
                Sender_Email = "rr3346459@gmail.com"
                Reciever_Email = result[0]
                Password ='cgtpqlenlfhvkhwm'
                newMessage = EmailMessage()    #creating an object of EmailMessage class
                newMessage['Subject'] = "Request for Doctor's Appointment Booking" #Defining email subject
                newMessage['From'] = Sender_Email  #Defining sender email
                newMessage['To'] = Reciever_Email  #Defining reciever email
    
    
                import requests 
    
    
                newMessage.set_content(f'Doctor name,\n {doctor},\n I am writing to request an appointment with you for a medical consultation. I am currently experiencing {disease}. I believe that a consultation with you would help me address my health issues and improve my well-being.\n I am available [provide your preferred date(s) and time(s) for the appointment]. Please let me know if any of these dates and times are suitable for you. If none of these dates work, kindly suggest an alternative date and time that would be convenient for you.\n Please also let me know if there are any specific preparations that I need to make prior to the consultation, such as fasting or bringing any medical records.\n I look forward to hearing from you soon and thank you in advance for your time and attention.\n Sincerely,\n {name}:')
    
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    
                    smtp.login(Sender_Email, Password)              
                    smtp.send_message(newMessage)
                

            return result[0]
        else:
            return ""

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Appointment")
   

    w,h = root.winfo_screenwidth(),root.winfo_screenheight()
    root.geometry("%dx%d+0+0"%(w,h))
    root.configure(background="skyblue")

    image2 =Image.open('guimain1.jpg')
    image2 =image2.resize((w,h), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image

    background_label.place(x=0, y=0)
    app = DoctorAppointmentApp(root)
    root.mainloop()

import smtplib
from email.message import EmailMessage
import imghdr

Sender_Email = "rr3346459@gmail.com"
Reciever_Email = "rr3346459@gmail.com"
Password ='cgtpqlenlfhvkhwm'
newMessage = EmailMessage()    #creating an object of EmailMessage class
newMessage['Subject'] = "Appointment Fixed...Mail sent sucessfully" #Defining email subject
newMessage['From'] = Sender_Email  #Defining sender email
newMessage['To'] = Reciever_Email  #Defining reciever email


import requests 


newMessage.set_content('Doctor name,\n [Dr.Patil],\n I am writing to request an appointment with you for a medical consultation. I am currently experiencing [briefly mention the symptoms or health concerns you are facing]. I believe that a consultation with you would help me address my health issues and improve my well-being.\n I am available [provide your preferred date(s) and time(s) for the appointment]. Please let me know if any of these dates and times are suitable for you. If none of these dates work, kindly suggest an alternative date and time that would be convenient for you.\n Please also let me know if there are any specific preparations that I need to make prior to the consultation, such as fasting or bringing any medical records.\n I look forward to hearing from you soon and thank you in advance for your time and attention.\n Sincerely,\n [Akshata]:')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage)

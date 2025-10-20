import nltk  #text to text (nlp)
from textblob import TextBlob  #provide api for nlp
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from PIL import Image , ImageTk     #image procressing lib
from keras.models import load_model
model = load_model('TRIAL_MODEL.h5')    #loads pre trained model
import json
import random
import sqlite3
import tkinter as tk
import pyttsx3 
import PIL.Image
import speech_recognition as sr
#import PyAudio

converter = pyttsx3.init() 

converter.setProperty('rate', 150) 

converter.setProperty('volume', 1.0) 

intents = json.loads(open('intents2.json').read())

words = pickle.load(open('WORDS.pkl','rb'))
classes = pickle.load(open('CLASSES.pkl','rb'))



# step1: clean sentence (lemmatize words)

def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

#step 2: Bag of words (BoW) array representing the presence of words in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

# step 3: List of predicted intents along with probabilities
def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

#step 4 : A randomly selected response based on the predicted intent
def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result




#step 5: Chatbot response and relevant doctor information
def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    if 'chicken pox' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='CHICKEN POX'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'FEVER' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='FEVER'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'COUGH' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='COUGH'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'COLD' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='COLD'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Contact Dermatitis' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Contact Dermatitis'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Eye Allergies' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Eye Allergies'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Sinus Infection' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Sinus Infection'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Allergic Rhinitis' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Allergic Rhinitis'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Food Allergy' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Food Allergy'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Anaphylaxis' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Anaphylaxis'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'Acne' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Acne'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
     
    if 'Eczema' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Eczema'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'hives' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='hives'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'dark circles' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='dark circles'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'Blackheads' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Blackheads'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'psoriasis' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='psoriasis'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'dry, cracked skin' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='dry, cracked skin'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    
    if 'ulcers' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='ulcers'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'rosacea' in res:
        db = sqlite3.connect(r'Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='rosacea'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'open sores or lesions' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='open sores or lesions'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'ringworm' in res:
        db = sqlite3.connect(r'D:/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='ringworm'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d   
    else:
        print(res)
        return res 





#Creating GUI with tkinter

import tkinter
from tkinter import *

def doctors():
   from subprocess import call
   call(["python","doctors information.py"]) 

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.configure(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    
        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: \n" + str(res) + '\n')
        
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        




# voice based communication 

from translate import Translator 
def To_English():
    global file
    pass_text = detect_text()
    en_blob = TextBlob(str(pass_text))
    translated = (en_blob.translate(to='en'))
    print(translated)
    To_English_label = tk.Label(root,text=str(translated),font=('Times New Roman',12,'italic'),width=47,height=30,bg='green4',fg='white')
    To_English_label.place(x=905,y=50)
def SPEECH():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        
        import time
            #language = 'mr'
            #Lang1=c.get()
            #translator= Translator(from_lang=Lang1,to_lang=language)
            #translation = translator.translate(text)
        global file
            
            #en_blob = TextBlob(str(text))
            #translated = (en_blob.translate(to='en'))
            #print(translated)
        time.sleep(1)
        translator= Translator(from_lang="English",to_lang="English")
        translation = translator.translate(text)
        print(translation)
        print(type(translation))
        print('You Said : {}'.format(translation))
        # en_blob = TextBlob(str(translation))
        # translated = (en_blob.translate(to='en'))
        # translated = str(translated)
        # print(str(translated))
        # print(type(translated))
       
        
    #msg = listen()
    # print(msg)
    # en_blob = TextBlob(str(msg))
    # translated = (en_blob.translate(to='en'))
    # print(translated)
    language = 'en'
    # Lang1=c.get()
    # translator= Translator(from_lang=Lang1,to_lang='en-US')
    # translation = translator.translate(msg)
    # print(translation)
    EntryBox.delete("0.0",END)

    if translation != '':
        ChatLog.configure(state=NORMAL)
        ChatLog.insert(END, "You: " + translation + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    
        res = chatbot_response(translation)
        ChatLog.insert(END, "Bot:\n " + "\n"+ str(res)+ '\n\n')
        converter.say(str(res)) 
        converter.runAndWait() 

            
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    
base = tk.Toplevel()
base.title("Medical Chat bot")

#base.configure(background="#A9A9A9")
#base.geometry("1600x900")
base.resizable(width=tk.TRUE, height=tk.TRUE)
w, h = base.winfo_screenwidth(), base.winfo_screenheight()
base.geometry("%dx%d+0+0" % (w, h))
load_bg = PIL.Image.open(r"chatbot.jpg")
load_bg = load_bg.resize((w,h))
render_bg = ImageTk.PhotoImage(load_bg)
bg = tk.Label(base, image = render_bg)
bg.image = render_bg
bg.place(x=0,y=0)

# head_icon=ImageTk.PhotoImage(file="D:/icon1.jpg")
# #Create Chat window
ChatLog = tk.Text(base, bd=2, bg="white",fg="black", height="15", width="150", font="Arial",)

#ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = tk.Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = tk.Button(base, font=("Verdana",12,'bold'), text="Send", width="15", 
                    bd=0, bg="#bca89f", activebackground="green",fg='#ffffff',
                    command= send)

#Create the box to enter message
EntryBox = tk.Text(base,bd=1, bg="pink",fg="black",width="5", height="1", font=("Arial",15))
EntryBox.place(x=200, y=500)
#EntryBox.bind("<Return>", send)

c=StringVar()
#Place all components on the screen
head = tk.Label(base,width=60,text="Voice Based Medical Assistant ChatBot",font=("times",30,'bold',"italic"),fg="black",height=1)
head.place(x=0,y=0)
scrollbar.place(x=1070,y=100, height=500)
ChatLog.place(x=150,y=100, height=500, width=930)
SendButton.place(x=200, y=430, height=80)
EntryBox.place(x=150, y=500, height=100, width=930)


# head = tk.Label(base,width=20,text="Voice Communication",font=("times",20,"italic"),bg="black",fg="white")
# head.place(x=590,y=540)
#label_1 = Label(base, text="Select Language",height=2,width=20,font=("bold", 10),bg='Olive',fg='black')
#label_1.place(x=700,y=660)

list1 = ['English'];

droplist=OptionMenu(base,c, *list1)
droplist.config(height=2,width=20)
c.set('Select language') 
droplist.place(x=400,y=500)
#Button(frame_alpr1, text='After Selecting Language... Press Button and Talk....',height=5,width=50,font=('times', 14, ' bold '),bg='brown',fg='white',command=translate_text).place(x=30,y=180)

button2 = tk.Button(base,text="... Press Button and Talk....",command=SPEECH,font=('Times New Roman',15,'bold'),width=20,bg='#6a4a3a',fg='white')
button2.place(x=600,y=500)


button3 = tk.Button(base, text="Doctors information",command=doctors,width=15, height=1,font=('times', 15, ' bold '), bg="#6a4a3a", fg="white")
button3.place(x=870, y=500)


  

# def prediction_emotion():
#     #clear_img()
#     #update_label("Model Training Start...............")

#     start = time.time()

#     result = validate.files_count()
#     #validate.files_count()
#     end = time.time()
#     #print("---" + result)
    

#     msg = '\n' + str(result) + '\n'

#     update_label(msg)
#################################################################################################################
def window():
    #root.destroy()
    base.destroy()
    from subprocess import call
    call(["python","gui main_1.py"])


button1 = tk.Button(base,text="Back",command=window,font=('times', 20, ' bold '),width=7)
button1.place(x=1200,y=400)

# button4 = tk.Button(base, text="Prediction",command=prediction_emotion, width=12, height=1, bg="brown4", fg="white",font=('times', 15, ' bold '))
# button4.place(x=1400, y=400)

base.mainloop()


# Voice and Text-Based Medical Chatbot

A **Voice and Text-Based Medical Chatbot** that provides medical advice, disease prediction, BMI calculation, and appointment booking using **Natural Language Processing (NLP)** and **Machine Learning**. It supports both **voice** and **text** interactions to make healthcare accessible and interactive.

---

## **Features**

### 1. Voice and Text Interaction
- **Voice/Speech Recognition:** Converts spoken input into text using Automatic Speech Recognition (ASR).
- **Natural Language Processing (NLP):** Understands user intent from text or speech and provides human-like responses.
- Supports queries like symptom checking, BMI calculation, appointment booking, and disease risk assessment.

### 2. BMI Calculator
- Calculates Body Mass Index (BMI) using:
  $$
  BMI = \frac{\text{Weight (kg)}}{\text{Height (m)}^2}
  $$
- Classifies weight status:
  - Underweight
  - Normal
  - Overweight
  - Obese

### 3. Appointment Booking
- Guides users to schedule appointments with doctors after a preliminary risk assessment.
- Sends confirmation emails for booked appointments.

---

## **Disease Prediction**
Predicts **Heart Disease** and **Diabetes** risk using advanced machine learning algorithms.

### Support Vector Machine (SVM)
- **Type:** Supervised learning (classification)
- **Mechanism:** Finds an optimal hyperplane to separate classes in high-dimensional feature space.
- **Use Case:** Classifies users into 'disease present' or 'disease absent' categories based on features like age, blood pressure, glucose level, BMI, and symptoms.

### XGBoost (Extreme Gradient Boosting)
- **Type:** Ensemble learning algorithm
- **Mechanism:** Sequentially builds decision trees where each tree corrects errors from previous ones.
- **Use Case:** Provides high-accuracy predictions for heart disease and diabetes risk.

---

## **Technologies Used**
- **Python:** Core language for chatbot logic
- **Libraries:** `SpeechRecognition`, `pyttsx3`, `sklearn`, `xgboost`, `pandas`, `numpy`, `flask` (for web integration)
- **Machine Learning Models:** SVM, XGBoost
- **NLP:** Natural Language Understanding for intent recognition

---

## **How It Works**
1. User interacts via voice or text.
2. NLP engine analyzes the input and extracts intent and symptoms.
3. BMI is calculated if requested.
4. Disease prediction models (SVM/XGBoost) estimate the risk of heart disease or diabetes.
5. Appointment booking is suggested based on the prediction.
6. Responses are provided via text and/or speech output.

---

## **Setup and Installation**

1. Install required libraries:

```bash
pip install -r requirements.txt
```

2. Run the chatbot:

```bash
python CHAT_1.py
```

---

## **Usage**

* Type or speak your symptoms to the chatbot.
* Ask for BMI calculation or appointment booking.
* Get predictions for heart disease or diabetes risk in real-time.

---

## **Project Benefits**

* Provides accessible healthcare guidance.
* Automates administrative tasks like appointment booking.
* Helps users monitor health indicators (BMI, disease risk) proactively.
* Can assist doctors by pre-screening patients and collecting symptoms efficiently.

---

## **Future Enhancements**

* Integration with telemedicine platforms.
* Multi-language support.
* Expanded disease prediction (more conditions).
* Mobile app integration for wider accessibility.

---


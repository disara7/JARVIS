#  program to translate speech to text and text to speech

import speech_recognition as sr
import pyttsx3

import os

OPENAI_KEY = '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'

import openai 
openai.api_key = OPENAI_KEY

#function to convert text to speech

def SpeakText(command):

    #initiate the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

#initiate the recognizer
r = sr.Recognizer()

def record_text():
#loop in case of errors
    while(1):
        try:
            #use microphone as source of imput
            with sr.Microphone() as source2:

                #prepare recognizer to recieve imput
                r.adjust_for_ambient_noise(source2, duration=0.20)

                print("I'm listening")

                #listenis for the user's input
                audio2 = r.listen(source2)

                #using google to recognize audio
                MyText = r.recognize_google(audio2)

                return MyText
            
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")

def sent_to_chatGPT(messages, model="gpt-3.5-turbo"):

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message

messages = [{"role": "user", "content": "please act like Jarvis from Iron Man."}]
while(1):
    text = record_text()
    messages.append({"role": "user", "content": text})
    response = sent_to_chatGPT(messages)
    SpeakText(response)

    print(response)
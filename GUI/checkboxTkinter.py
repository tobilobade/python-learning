# # from tkinter import *

# # window=Tk()

# # window.title('My window')

# # window.geometry('100x100')




# # l=Label(window,bg="White",width=20,text="empty")

# # l.pack()




# # def print_selection():

# #     if(var1.get() == 1) & (var2.get() == 0):

# #         l.config(text='I love python')

# #     elif (var1.get() == 0) & (var2.get()==1):

# #         l.config(text="I love C++")

# #     elif (var1.get()==0) & (var2.get()==0):

# #         l.config(text="I do not anything")

# #     else:

# #         l.config(text="I love both")





# # var1=IntVar()

# # var2=IntVar()




# # c1=Checkbutton(window,text="Python",variable=var1,onvalue=1,offvalue=0,command=print_selection)

# # c2=Checkbutton(window,text="C++",variable=var2,onvalue=1,offvalue=0,command=print_selection)




# # c1.pack()

# # c2.pack()

# # window.mainloop()

# import tkinter as tk
# import speech_recognition as sr

# def recognize_speech():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         audio = recognizer.listen(source)
#     try:
#         recognized_text = recognizer.recognize_google(audio)
#         text_entry.delete(1.0, tk.END)  # Clear previous text
#         text_entry.insert(tk.END, recognized_text)
#     except sr.UnknownValueError:
#         text_entry.delete(1.0, tk.END)  # Clear previous text
#         text_entry.insert(tk.END, "Speech recognition could not understand audio")
#     except sr.RequestError as e:
#         text_entry.delete(1.0, tk.END)  # Clear previous text
#         text_entry.insert(tk.END, f"Could not request results from Google Speech Recognition service; {e}")

# # Create the main Tkinter window
# window = tk.Tk()
# window.title("Speech Recognition")

# # Create a text entry field
# text_entry = tk.Text(window, height=10, width=50)
# text_entry.pack()

# # Create a button to start speech recognition
# recognize_button = tk.Button(window, text="Recognize Speech", command=recognize_speech)
# recognize_button.pack()

# # Start the Tkinter event loop
# window.mainloop()

import tkinter as tk
import speech_recognition as sr
from gtts import gTTS
import io

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        recognized_text = recognizer.recognize_google(audio)
        text_entry.delete(1.0, tk.END)  # Clear previous text
        text_entry.insert(tk.END, recognized_text)
        convert_to_speech(recognized_text)
    except sr.UnknownValueError:
        text_entry.delete(1.0, tk.END)  # Clear previous text
        text_entry.insert(tk.END, "Speech recognition could not understand audio")
    except sr.RequestError as e:
        text_entry.delete(1.0, tk.END)  # Clear previous text
        text_entry.insert(tk.END, f"Could not request results from Google Speech Recognition service; {e}")

def convert_to_speech(text):
    tts = gTTS(text=text, lang='en')
    speech_stream = io.BytesIO()
    tts.save(speech_stream)
    speech_stream.seek(0)
    # Perform operations with the speech_stream, e.g., save it to a file or play it using an audio player

# Create the main Tkinter window
window = tk.Tk()
window.title("Speech Recognition and Text-to-Speech")

# Create a text entry field
text_entry = tk.Text(window, height=10, width=50)
text_entry.pack()

# Create a button to start speech recognition
recognize_button = tk.Button(window, text="Recognize Speech", command=recognize_speech)
recognize_button.pack()

# Start the Tkinter event loop
window.mainloop()

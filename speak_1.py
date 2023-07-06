#badger
import pyttsx3

def say(A1):
	b1=pyttsx3.init()
	print(A1)
	b1.say(A1)
	b1.runAndWait()
def ask(A1):
	b1=pyttsx3.init()
	b1.say(A1)
	b1.runAndWait()
	b2=input(A1)
	return b2
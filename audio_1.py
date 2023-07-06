#badger
import speech_recognition as sr

class audio():
	def listen():
		b1=sr.Recognizer()
		with sr.Microphone() as b2:
			b1.energy_threshhold=1
			b1.adjust_for_ambient_noise(b2)
			b3=b1.listen(b2,timeout=10)
			b4=""
			try:
				b4=b1.recognize_google(b3)
			except Exception as A:
				print("ERROR: "+str(A)+"!")
			except ValueError as A:
				print("ERROR: VALUE ERROR!")
				print("ERROR: "+str(A))
			except:
				raise Exception("ERROR: COULD NOT COMPREHEND INPUT!")
		return b4
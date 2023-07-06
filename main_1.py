#badger
from var_1 import *#morse

if __name__=="__main__":
	set_title("CONVERT_MORSE_1!")

	print("1: Type the input")
	print("2: Say the input")
	a1:str=input("/>")

	clear()

	text:str=""
	if a1=="1":
		text=input("Input: ")
	elif a1=="2":
		echo("Say the input...")
		try:
			text=audio.listen()
		except:
			print(Exception)
	else:
		print("An error occured in the program. The input could have been out of range. The only possible inputs are either 1 or 2.")

	msg:morse=morse(text)

	msg.set_encrypt()

	print("Input: "+msg.text)
	print("Morse code conversion: "+msg.encrypt)

	#msg.say()

	#say(msg)

	#Beep(1000,100)

	pause()
#fix listen, speak, and beep

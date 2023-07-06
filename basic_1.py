#badger
from os import system#pause
from ctypes import windll#title

def pause():
	system("pause")

def clear():
	system("cls")

def echo(text:str):
	print(text,end="")

def set_title(text):
	windll.kernel32.SetConsoleTitleW(text)
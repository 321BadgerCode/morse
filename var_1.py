#badger
from winsound import Beep#beep
import enum#enum
from audio_1 import *
from basic_1 import *
from speak_1 import *

class morse():
        __define:str={"a":".-",
                "b":"-...",
                "c":"-.-.",
                "d":"-..",
                "e":".",
                "f":"..-.",
                "g":"--.",
                "h":"....",
                "i":"..",
                "j":".---",
                "k":"-.-",
                "l":".-..",
                "m":"--",
                "n":"-.",
                "o":"---",
                "p":".--.",
                "q":"--.-",
                "r":".-.",
                "s":"...",
                "t":"-",
                "u":"..-",
                "v":"...-",
                "w":".--",
                "x":"-..-",
                "y":"-.--",
                "z":"--..",
                "1":".----",
                "2":"..---",
                "3":"...--",
                "4":"....-",
                "5":".....",
                "6":"-....",
                "7":"--...",
                "8":"---..",
                "9":"----.",
                "0":"-----",
                ",":"--..--",
                ".":".-.-.-",
                "?":"..--..",
                "/":"-..-.",
                "-":"-....-",
                "(":"-.--.",
                ")":"-.--.-"}
        def __get_type(self):
                if list(self.__define)[0] in self.text:
                        self.type2=self.type1(self.type1.ascii1)
                else:
                        self.type2=self.type1(self.type1.morse)
        def __init(self):
                self.__get_type()

        class type1(enum.Enum):
                none:int=0
                ascii1:int=1
                morse:int=2
        text:str=""
        type2:type1=type1(type1.none)
        encrypt:str=""
        decrypt:str=""
        def __init__(self,text:str):
                self.text=text
                self.__init()
        def set_encrypt(self):
                self.encrypt=""
                for a in self.text:
                        if a!=" ":
                                self.encrypt+=self.__define[a]+" "
                        else:
                                self.encrypt+=" "
         
                return self.encrypt
        def set_decrypt(self,text:str):
                self.text+=" "
                self.encrypt=""
                citext:str=""
                
                for a in self.text:
                        if (a!=" "):
                                b:int=0
                                citext+=a
                        else:
                                b+=1
                                if b==2 :
                                        self.decrypt+=" "
                                else:
                                        self.decrypt+=list(self.__define.keys())[list(self.__define.values()).index(citext)]
                                        citext=""
         
                return self.decrypt
        def say(self):
                if self.type2==self.type1.ascii1:
                        #speak(self.text)
                        print("Doesn't work right now :(")
                else:
                        for a in range(len(self.text)):
                                if self.text[a]==".":
                                        Beep(1000,100)
                                elif self.text[a]=="-":
                                        Beep(1000,1000)

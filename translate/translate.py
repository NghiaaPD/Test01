from tkinter import*
from PIL import Image,ImageTk
from googletrans import Translator
import pyttsx3

system = Tk()
system.title("Tkinter Translate")
system.geometry("600x700")
system.iconbitmap("t1.ico")

bot = pyttsx3.init()
voices = bot.getProperty("voices")
bot.setProperty("voice", voices[1].id)


background = Image.open("yy.png")
background_size = background.resize((600,700))
background_ImageTk = ImageTk.PhotoImage(background_size)
background_Label = Label(system,image = background_ImageTk)
background_Label.place(x=0,y=0)

Label_title = Label(system,text="Tkinter Dịch",font=("Arial Bold",15),bg="#26323E",fg="white",height=3)
Label_title.place(relx=.5,rely=.08,anchor="c")

Text_input = Text(system,width=50,height = 8,font=("Lato-Black",10))
Text_input.place(relx=.2,rely=.25,anchor="w")

Text_output = Text(system,width=50,height = 8,font=("Lato-Black",10))
Text_output.place(relx=.2,rely=.7,anchor="w")

def delate():
    Text_input.delete(0.0,END)
    Text_output.delete(0.0,END)
Button_clear = Button(system,text="Xóa Sạch",font=("Arial Bold",10),bg='#ABBEB8',fg="white",bd=0,command=delate)
Button_clear.place(relx=.2,rely=.43)
def translate():
    translate_input = Text_input.get(0.0,END)
    translate = Translator()
    change_language = translate.translate(translate_input,src="vi",dest="en")
    final = change_language.text
    Text_output.insert(END,final)
Button_translate = Button(system,text="Dịch Ra",font=("Arial Bold",10),bg="#AFBCB4",fg="white",bd=0,command=translate)
Button_translate.place(relx=.7,rely=.43)

def clicked():
    bot = pyttsx3.init()
    voices = bot.getProperty("voices")
    bot.setProperty("voice", voices[1].id)
    bot.say(Text_input.get(0.0,END))
    bot.runAndWait()
def click():
    voices = bot.getProperty("voices")
    bot.setProperty("voice", voices[0].id)
    bot.say(Text_output.get(0.0,END))
    bot.runAndWait()
    
Button_voice_1 = Button(system,text="đọc",font=("Arial Bold",10),bg="#1F1F27",fg="white",bd=0,command=clicked)
Button_voice_1.place(relx=.21,rely=.30)

Button_voice_2 = Button(system,text="đọc",font=("Arial Bold",10),bg="#1F1F27",fg="white",bd=0,command=click)
Button_voice_2.place(relx=.21,rely=.75)

system = mainloop()
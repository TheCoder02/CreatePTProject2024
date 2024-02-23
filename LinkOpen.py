from tkinter import *
from time import *
from NotificationMaker import *
import webbrowser
def popup_maker(title, link, text):
   pop = Tk()
   pop.title(title)
   def onClick():
       webbrowser.open(link)

   button = Button(pop,text=text,width = 50,height = 10,bg = 'white',fg = 'black',command=onClick)
   button.pack()
   pop.mainloop()
   return pop

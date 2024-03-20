from tkinter import *
import time
import random
from NotificationMaker import *
import webbrowser
def popup_maker(title, link, text, number):
   pop = Tk()
   pop.title(title)
   def timedWindows(number):
      for i in range(1):
         for i in range(number):
            x = random.randint(0,1820)
            y = random.randint(0,980)
            pop2 = Tk()
            pop2.geometry('200x50'+'+'+str(x)+'+'+str(y))
            pop2.title(title)
            
            timedWindow = Button(
            pop2,
            text = 'You got Hacked!',
            bg = 'White',
            fg = 'Black',
            height = 10,
            width = 50
            )
            
            timedWindow.pack()      
      pop.destroy()
      pop2.mainloop()
      
   button = Button(
   pop,
   text = text,
   width = 50,
   height = 10,
   bg = 'white',
   fg = 'black',
   command = timedWindows(number)
   )
   
   button.pack()
   pop.mainloop()
   return pop

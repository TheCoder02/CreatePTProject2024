from tkinter import *
from time import *
import webbrowser
def popup_maker():
   popup = Tk()

   def onClick():
       webbrowser.open("file:///C:/Users/lg255111/OneDrive%20-%20Lamar%20Consolidated%20ISD/2023-2024/Computer%20Science/CreatePT%20Ideas/info.html")

   button = Button(popup,text="You have a virus, click here to run diagnostics!",width = 50,height = 10,bg = 'white',fg = 'black',command=onClick)
   button.pack()
   popup.mainloop()
   
   
#sleep(5)
#popup.destroy()
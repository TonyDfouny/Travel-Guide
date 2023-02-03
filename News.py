from tkinter import*
import tkinter
from tkinter import ttk
from APIS import nynews
from datetime import date,datetime,timedelta
from PIL import ImageTk ,Image


class news:
    def __init__(self,main):
        self.main=main
        today=date.today()
        def back():
            self.main.deiconify()
            fenetre.destroy()
            
    
        new=nynews(today.strftime('20%y%m%d'))
        news=new['response']['docs']
        d=1
        while len(news)<10 or d<=4:
            before=date.today() - timedelta(days=d)
            new=nynews(before.strftime('20%y%m%d'))
            news=new['response']['docs']
            d+=1
         

        fenetre=tkinter.Toplevel(self.main)
        fenetre.title('Local News')
        image5=ImageTk.PhotoImage(Image.open("newsim.jpeg")) 
        Label(fenetre, image=image5).place(x=0,y=0) 
        
        Label(fenetre,text="Latest News:",font=("apple chancery",25)).grid(sticky=W)
       
        i=0
        while i<len(news):
            Label(fenetre,text=(news[i]['abstract']+'\n'+news[i]['pub_date'][:19])).grid(padx=10,pady=10,sticky=W)
            i+=1
        reference=new['copyright']
        
        Label(fenetre,text=reference,).grid()
        Button(fenetre,text='Back',command=back).grid()
        
        fenetre.mainloop()
        





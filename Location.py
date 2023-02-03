from APIS import *
from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import ImageTk ,Image

class locatio:
    def __init__(self,main):
        self.main=main

        def clearFrame(frame):
            
            for widget in frame.winfo_children():
               widget.destroy()

        def Search(event=None):
            clearFrame(result)
            loc=location(place.get(),city.get())
            i=0
            latlong=''
            
            try:
                while i<len(loc):
                    name=loc[i]['display_name'].split(',')
                    ttk.Label(result,text=name[0]+'\n'+name[1]+name[2]+name[3]).grid(columnspan=5,sticky=W)
                    lat=loc[i]['lat']
                    long=loc[i]['lon']
                    latlong=latlong+'|'+lat+','+long
                    i+=1
            except KeyError:
                messagebox.showerror('Error','No location or places were found for the given input')
            except IndexError:
                messagebox.showerror('Error','No location or places were found for the given input')
            Map=staticmap(latlong)
            with open('map.png', 'wb') as file:
                file.write(Map.content)
            statmap=ImageTk.PhotoImage(Image.open('map.png'))
            ttk.Label(result,image=statmap).grid(row=0,column=100,rowspan=10)
            result.mainloop()
        def Back():
            self.main.deiconify()
            fenetre.destroy()
            
            
            
        fenetre=tkinter.Toplevel(self.main)
        fenetre.title('Places Loc')
        fenetre.bind('<Return>',Search)

        search=tkinter.Frame(fenetre)
        search.grid()
        result=tkinter.Frame(search)
        result.grid(row=1,columnspan=5,padx=15,pady=15)
        place=StringVar()
        city=StringVar()
        Label(search,text='Place:').grid(row=0,column=0,padx=12,pady=12)
        Entry(search,textvariable=place).grid(row=0,column=1,padx=12,pady=12,sticky=(W))
        Label(search,text='City:').grid(padx=12,pady=12,row=0,column=2)
        Entry(search,textvariable=city).grid(padx=12,pady=12,row=0,column=3,sticky=(W))
        Button(search,text='Search',command=Search).grid(padx=12,pady=12,row=0,column=4,sticky=(E))
        Button(search,text='Back',command=Back).grid(padx=12,pady=12,row=0,column=5)
       
        
        fenetre.mainloop()




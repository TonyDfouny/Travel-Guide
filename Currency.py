import tkinter
from tkinter import*
from tkinter import ttk
from APIS import *
from PIL import ImageTk ,Image
import os
from tkinter import messagebox



class curency:
    def __init__(self,main):
        self.main=main
        def calcule(event=None):
            try:
                total.set(montant.get()*float(currency(currence1.get(),currence2.get())))
            except tkinter.TclError:
                messagebox.showerror('Error','Please input numbers only!')
                
        def enable(evt):
            combo2['state']='readonly'
        def currence(evt):       
            currence1.get()
            currence2.get()
            convert['state']='!disabled'     
        def back():
            self.main.deiconify()
            fenetre.destroy()
        image2=ImageTk.PhotoImage(Image.open("currencyim.jpeg"))    
        fenetre=tkinter.Toplevel(self.main)
        fenetre.bind('<Return>',calcule)
        fenetre.title('Currency Converter')
        montant=IntVar()
        total=IntVar()
        currence1=StringVar()
        currence2=StringVar()
        
        Label(fenetre, image=image2).place(x=0,y=0)
        image1=ImageTk.PhotoImage(Image.open("arrow.png"))
        Label(fenetre,text="Currency Converter",font=("apple chancery",25)).grid(row=0,column=1)
        Entry(fenetre,textvariable=montant).grid(row=1,column=1)
        combo1=ttk.Combobox(fenetre,textvariable=currence1,values=listeall,state='readonly')
        combo1.grid(row=2,column=0)
        combo1.bind('<<ComboboxSelected>>',enable)
        Label(fenetre,image=image1).grid(row=2,column=1)
        combo2= ttk.Combobox(fenetre,textvariable=currence2,values=listeall,state='disabled')
        combo2.bind('<<ComboboxSelected>>',currence)
        combo2.grid(row=2,column=2)
        Label(fenetre,text="Result").grid(row=3,column=0)
        Label(fenetre,textvariable=total).grid(row=3,column=1)
        convert=ttk.Button(fenetre,text='Convert',command=calcule,state='disabled')
        convert.grid(row=4,column=1)
        Button(fenetre,text='Back',command=back).grid(row=5,column=10)
        fenetre.mainloop()


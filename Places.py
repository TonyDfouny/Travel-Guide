from tkinter import*
from tkinter import ttk
import tkinter
from PIL import ImageTk,Image
import os

class place:

    def __init__(self,city,main):
        self.city=city
        self.main=main

    def create(self):
        self.main.withdraw()
        
        liste=[]
        listes=os.listdir()
        for i in listes:
            if self.city in i:
                liste.append(i)
        fen=Toplevel(self.main)
        fen.title('Choses a Faire a '+self.city)
        with open(self.city+'.txt',"r" ,encoding='utf-8') as a:
            contenu=a.read()
            texte=ttk.Label(fen,text=contenu)
            texte.grid(row=0,column=0)
        r=1
        d={1:'a',2:'b',3:'c',4:'d'}
        c=1
        s=W
        for j in liste:
            if c==3:
                r=2
            if r==2 and c==3:
                s=W
            if '.jpg' in j: 
                d[c]=ImageTk.PhotoImage(Image.open(j).resize((400,200)))
                Label(fen,image=d[c]).grid(row=r,column=0,columnspan=2,sticky=s)
                s=E
                c=c+1
        def Back():
            self.main.deiconify()
            fen.destroy()
            
        Button(fen,text='Back',command=Back).grid(row=0,column=1)
        fen.mainloop()

  

class tourisme:
    def __init__(self,main):
        
        self.main=main
        def Back():
            self.main.deiconify()
            fenetre_tourisme.destroy()
        fenetre_tourisme=tkinter.Toplevel(self.main)
        fenetre_tourisme.title("Le Tourisme au Liban")
        frame1=Frame(fenetre_tourisme)
        frame1.grid(row=0,column=0)
        label_titre=Label(frame1,text='Le Tourisme au Liban',font=('Apple chancery',30),foreground='green')
        label_titre.grid(row=1,column=0,rowspan=2,pady=40)

        fenetre_tourisme.columnconfigure(0,weight=1)
        fenetre_tourisme.rowconfigure(0,weight=1)
        frame2=Frame(fenetre_tourisme)
        frame2.grid(row=1,column=0,sticky=(W,N,S,E))
        listes=os.listdir()
        liste=[]
        for i in listes:
            if '.txt' in i:
                liste.append(i.split('.txt')[0])
        
        r=1
        c=0
        for j in liste:
            if r%4==0:
                r=1
                c+=1
            
            ttk.Button(frame2,text=j,command=place(j,fenetre_tourisme).create,width=15).grid(row=r,column=c)
            r+=1
        labelliban=ttk.Label(frame2,text='  Que faire au Liban?',font=('Verdana',20))
        labelliban.grid(row=0,column=0,sticky=W,pady=20)
        image1=ImageTk.PhotoImage(Image.open('lebanon2.jpg'))
        labelimage1=Label(frame1,image=image1)
        labelimage1.grid(row=0,column=0)
        ttk.Button(frame2,text='Back',command=Back).grid(row=3,column=100)
        fenetre_tourisme.mainloop()



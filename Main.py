from tkinter import *
from PIL import ImageTk ,Image
from Location import*
from News import*
from Currency import*
from Places import*


class page:
    def __init__(self,main,fonction):
        self.main=main
        self.fonction=fonction
        
    def Changepage(self):
        self.main.withdraw()
        self.fonction(self.main)

def Exit():
    fenetre.destroy()
    
    
fenetre = Tk()
fenetre.title('projet info')
image5=ImageTk.PhotoImage(Image.open("mainim2.jpeg")) 
Label(fenetre, image=image5).place(x=0,y=0)


label5=Label(fenetre,text='Travel Guide',font=('apple chancery',25))
label5.grid(row=1,column=2)


img1=ImageTk.PhotoImage(Image.open ("maps logo.png").resize((200,200)))
button1=Button(fenetre,image=img1,command=page(fenetre,locatio).Changepage)
button1.grid(row=2,column=1,padx=20,pady=20)
label1=Label(fenetre, text = 'Maps',background='white', font =('Verdana', 15))
label1.grid(row=3,column=1)


img2=ImageTk.PhotoImage(Image.open ("converter logo.png").resize((200,200)))
button2=Button(fenetre,image=img2,command=page(fenetre,curency).Changepage)
button2.grid(row=2,column=3,padx=20,pady=20)
label2=Label(fenetre, text = 'Currency Converter',background='white', font =('Verdana', 15))
label2.grid(row=3,column=3)


img3=ImageTk.PhotoImage(Image.open ("news logo.png").resize((200,200)))
button3=Button(fenetre,image=img3,command=page(fenetre,news).Changepage)
button3.grid(row=4,column=1,padx=20,pady=20)
label3=Label(fenetre, text = 'News',background='white', font =('Verdana', 15))
label3.grid(row=5,column=1)


img4=ImageTk.PhotoImage(Image.open ("lebanon logo.jpeg").resize((200,200)))
button4=Button(fenetre,image=img4,command=page(fenetre,tourisme).Changepage)
button4.grid(row =4,column=3,padx=20,pady=20)
label4=Label(fenetre, text = 'Places',background='white', font =('Verdana', 15))
label4.grid(row=5,column=3)


btn=Button(fenetre,text="Exit",command=Exit,width=15)
btn.grid(row=6,column=2)

fenetre.mainloop()

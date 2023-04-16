from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.geometry('800x480')
root.config(bg='#114A9C')

fontObj = tkFont.Font(size=20,family = 'Arial Bold')
l = Label(root, text="EDOSA", height =2,fg = 'White', bg = '#114A9C',font=fontObj)
l.pack(padx=10,pady=10,side=TOP, fill=BOTH)

Play = Frame(root)
Stop= Frame(root)
Pause = Frame(root)
Home =Frame(root)

def change_to_home():
  Home.pack(fill='both', expand=1)
  Play.pack_forget()
  Pause.pack_forget()
  Stop.pack_forget()
  

def change_to_play():
  Play.pack(fill='both', expand=1)
  Pause.pack_forget()
  Stop.pack_forget()

def change_to_stop():
  Stop.pack(fill='both', expand=1)
  Play.pack_forget()
  Pause.pack_forget()

def change_to_pause():
  Pause.pack(fill='both', expand=1)
  Play.pack_forget()
  Stop.pack_forget()


label1 = Label(Play, text="Play",width = 22,height = 22, font=23,bg='#114A9C',fg='white')
label1.pack(fill = 'both')

label2 = Label(Stop, text="Stop", foreground="white",width = 22,height = 22,bg='#114A9C', font =23)
label2.pack(fill = 'both')

label3 = Label(Pause, text="Pause", foreground="white",width = 22,height = 22,bg='#114A9C', font =23)
label3.pack(fill = 'both')

label4 = Label(Pause, text="Home", foreground="white",width = 22,height = 22,bg='#114A9C', font =23)
label4.pack(fill = 'both')


b4= tkFont.Font(size=10,family = 'Arial Bold')
b4=Button(root, text = "Play", command=change_to_home, height = 2, width = 13, bg = 'Green', fg = 'black', font=b4)
b4.place(x=2, y=40)

b= tkFont.Font(size=10,family = 'Arial Bold')
b=Button(root, text = "Play", command=change_to_play, height = 2, width = 13, bg = 'Green', fg = 'black', font=b)
b.place(x=225, y=420)


b3= tkFont.Font(size=10,family = 'Arial Bold')
b3=Button(root, text = "Stop", command=change_to_stop, height = 2, width = 13, bg = 'red', fg = 'black', font=b3)
b3.place(x=350, y=420)

b2= tkFont.Font(size=10,family = 'Arial Bold')
b2=Button(root, text = "Pause/Resume", command=change_to_pause, height = 2, width = 13, bg = 'Yellow', fg = 'black', font=b2)
b2.place(x=475, y=420)

root.mainloop()

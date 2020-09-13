import tkinter as tk
import simpleplayer as sp

def playmp4():
    sp.play(e.get())

window = tk.Tk()
window.title('simle player')
window.geometry('300x100')
b = tk.Button(window,text='play',width = 15, height = 2,command = playmp4)
b.pack()

e = tk.Entry(window)
e.pack()


window.mainloop()
import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl

class MasterPanel:

    def __init__(self):
        self.aplicaion = tk.Tk()
        w, h = self.aplicaion.winfo_screenwidth()/2, self.aplicaion.winfo_screenheight()/2
        self.aplicaion.geometry("%dx%d+0+0" % (w, h))
        self.aplicaion.config(bg='#fcfcfc')
        self.aplicaion.iconbitmap('Img/DntLogo.ico')
        self.aplicaion.resizable(width=True, height=True)
        utl.centrar_ventana(self.aplicaion,960,540)
        logo = utl.leer_imagen("Img/DntLogo.png", (200, 200))



        self.aplicaion.mainloop()
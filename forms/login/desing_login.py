import tkinter as tk
from tkinter import ttk
import util.generic as utl

class DesingLogin:

	def __init__(self):
		# Inicir tkinter
		self.aplicaion = tk.Tk()
		# Titulo de la ventana
		self.aplicaion.title('Log In')
		# self.aplicaion.overrideredirect(True)
		# logo de la ventana
		self.aplicaion.iconbitmap('Img/DntLogo.ico')
		# Tamaño y posicion de la ventana
		utl.centrar_ventana(self.aplicaion,400,600)
		# Bloquear tamño de la ventana
		self.aplicaion.resizable(0,0)

		logo = utl.leer_imagen("Img/DntLogo.png", (150, 150))

		# frame_logo
		frame_logo = tk.Frame(self.aplicaion, bd=0, height=150, relief=tk.SOLID, padx=10, pady=10,bg='#3a7ff6')
		frame_logo.pack(side="top",expand=tk.FALSE,fill=tk.BOTH)
		label = tk.Label(frame_logo, image=logo,bg='#3a7ff6' )
		label.place(x=0,y=0,relwidth=1, relheight=1)
		# fin frame_logo

		# frame_form
		frame_form = tk.Frame(self.aplicaion, bd=0, relief=tk.SOLID, bg='#fff')
		frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
		# fon frame_form

		# frame_form_top
		frame_form_top = tk.Frame(frame_form,height=50, bd=0, relief=tk.SOLID,bg='black')
		frame_form_top.pack(side="top",fill=tk.X)
		title = tk.Label(frame_form_top, text="Odonto Sofware",font=('Impact', 30), fg="#fff",bg='#3a7ff6',pady=10)
		title.pack(expand=tk.FALSE,fill=tk.BOTH)
		# fin frame_form_top

		#frame_form_fill
		frame_form_fill = tk.Frame(frame_form,height = 50,  bd=0, relief=tk.SOLID,bg='#fff')
		frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

		etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario:", font=('Times', 14) ,fg="black",bg='#fff', anchor="w")
		etiqueta_usuario.pack(fill=tk.X, padx=20,pady=(50, 1))
		self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
		self.usuario.focus()
		self.usuario.pack(fill=tk.X, padx=20,pady=10)

		etiqueta_password = tk.Label(frame_form_fill, text="Contraseña:", font=('Times', 14),fg="black",bg='#fff' , anchor="w")
		etiqueta_password.pack(fill=tk.X, padx=20,pady=1)
		self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
		self.password.pack(fill=tk.X, padx=20,pady=10)
		self.password.config(show="●")

		inicio = tk.Button(frame_form_fill,text="Iniciar sesion",font=('Times', 15),bg='#3a7ff6', bd=0,fg="#fff",command=self.ingresar)
		inicio.pack(fill=tk.X, padx=10,pady=10)
		registro = tk.Button(frame_form_fill,text="Registrar",font=('Times', 15),bg='#fff', bd=0,fg="#3a7ff6",command=self.userRegister)
		registro.pack(fill=tk.X, padx=10,pady=10)

		# frame_salir
		frame_salir = tk.Frame(frame_form_fill,height=20, bd=0, relief=tk.SOLID,bg='#fff')
		frame_salir.pack(side="bottom",expand=tk.FALSE,fill=tk.BOTH)
		salir = tk.Button(frame_salir,text="Salir",font=('Times', 15),bg='#fff', bd=0,fg="grey",command=self.aplicaion.destroy)
		salir.pack(side="right",fill=tk.X)

		self.aplicaion.mainloop()
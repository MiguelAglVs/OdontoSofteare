from tkinter import messagebox
from forms.master.form_master import MasterPanel
from forms.login.desing_login import DesingLogin
from forms.register.form_register import FormRegister
from modelo.conexion import conexionDB
# from werkzeug.security import generate_password_hash, check_password_hash

conexion = conexionDB()

class FormLogin(DesingLogin):

	def __init__(self):
		super().__init__()

	def validar(self):
		usu = self.usuario.get()
		password = self.password.get()
		return len(usu) != 0 and len(password) != 0

	def ingresar(self):
		usu = self.usuario.get()
		password = self.password.get()
		if self.validar():
			query = (f"SELECT * FROM usuarios WHERE usuario=? AND pass=?")
			parameters = (usu,password)
			usuario = conexion.run_query(query, parameters)
			# if usu not in usuario:
			if usuario.fetchall():
				messagebox.showinfo(message=f"Bienvenido {usu}.",title="Mensaje")
				self.aplicaion.destroy()
				MasterPanel()
			else:
				messagebox.showerror(message="El usuario o la contraseña son incorrectos.",title="Ups!, algo ha salido mal")
			# else:
			# 	messagebox.showerror(message=f"El usuario {usu} ya se encuentra registrado.",title="Ups!, algo ha salido mal")
		else:
			messagebox.showerror(message="El usuario y la contraseña son requeridos.",title="Ups!, algo ha salido mal")

	def userRegister(self):
		FormRegister()
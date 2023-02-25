from tkinter import messagebox
from forms.register.desing_register import DesingRegister
from modelo.conexion import conexionDB
# from werkzeug.security import generate_password_hash

conexion = conexionDB()

class FormRegister(DesingRegister):

	def validar(self):
		usu = self.usuario.get()
		password = self.password.get()
		return len(usu) != 0 and len(password) != 0

	def registrar(self):
		if self.validar():
			usu = self.usuario.get()
			password = self.password.get()
			confpass = self.confirmation.get()
			if password == confpass:
				query = (f"INSERT INTO usuarios (usuario,pass) VALUES (?,?)")
				parameters = (usu,password)
				conexion.run_query(query,parameters)
				self.ventana.destroy()
				messagebox.showinfo(message=f"El usuario {usu} registrado exitosamente.",title="Mensaje")
			else:
				self.message['text'] = 'Las contraseñas no coinciden.'
				self.password.delete(0)
				self.confirmation.delete(0)
				self.password.focus()
		else:
			self.message['text'] = 'Todos los campos son obligatorios.'
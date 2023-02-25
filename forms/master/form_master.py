import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import util.generic as utl
from modelo.conexion import conexionDB
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime

conexion = conexionDB()

class MasterPanel:

    def __init__(self):
        self.aplicacion = tk.Tk()
        w, h = self.aplicacion.winfo_screenwidth()/2, self.aplicacion.winfo_screenheight()/2
        self.aplicacion.geometry("%dx%d+0+0" % (w, h))
        self.aplicacion.title('Odonto Software JMC')
        self.aplicacion.config(bg='#f2f2f2')
        self.aplicacion.iconbitmap('Img/DntLogo.ico')
        self.aplicacion.resizable(width=False, height=True)
        utl.centrar_ventana(self.aplicacion,1366,769)
        self.idPaciente = None

        self.tabs = ttk.Notebook(self.aplicacion,)
        self.tabs.pack(fill='both', expand=True)

        self.pacientes = ttk.Frame(self.tabs, border=2)
        self.tabs.add(self.pacientes,text='Pacientes')

        self.citas = ttk.Frame(self.tabs)
        self.tabs.add(self.citas,text='Citas')

        #===================== Inicio Formulario =====================
        frame_fondo = tk.Frame(self.pacientes, bd=0,relief=tk.SOLID, bg='#fff')
        frame_fondo.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        frame_form = tk.Frame(frame_fondo, bd=0, relief=tk.SOLID, bg='#fff')
        frame_form.grid(row=0, column=0, sticky='E')

        frame = LabelFrame(frame_form, text='Registrar nuevo paciente', font=('Times', 15, 'bold'),bg='#fff')
        frame.grid(column=0,row=0,padx=(20,10), pady=10)

        Label(frame, text='Documento:* ', font=('Times', 12),bg='#fff').grid(row=1,column=0,sticky='W',padx=10, pady=(10,5))
        self.svdocument = StringVar()
        self.documento = ttk.Entry(frame, width=50, font=('Times', 14), textvariable=self.svdocument).grid(row=1,column=1,padx=10, pady=(10,5))

        Label(frame, text='Nombre:* ', font=('Times', 12),bg='#fff').grid(row=2,column=0,sticky='W',padx=10, pady=(10,5))
        self.svnombre = StringVar()
        self.nombre = ttk.Entry(frame, width=50, font=('Times', 14),textvariable=self.svnombre).grid(row=2,column=1,padx=10, pady=(10,5))

        Label(frame, text='Primer apellido:* ', font=('Times', 12),bg='#fff').grid(row=3,column=0,sticky='W',padx=10, pady=(10,5))
        self.svapellido = StringVar()
        self.apellido = ttk.Entry(frame, width=50, font=('Times', 14),textvariable=self.svapellido).grid(row=3,column=1,padx=10, pady=(10,5))

        Label(frame, text='Segundo apellido: ', font=('Times', 12),bg='#fff').grid(row=4,column=0,sticky='W',padx=10, pady=(10,5))
        self.svsapellido = StringVar()
        self.sapellido = ttk.Entry(frame, width=50, font=('Times', 14),textvariable=self.svsapellido).grid(row=4,column=1,padx=10, pady=(10,5))

        Label(frame, text='Correo: ', font=('Times', 12),bg='#fff').grid(row=5,column=0,sticky='W',padx=10, pady=(10,5))
        self.svcorreo = StringVar()
        self.correo = ttk.Entry(frame, width=50, font=('Times', 14),textvariable=self.svcorreo).grid(row=5,column=1,padx=10, pady=(10,5))

        Label(frame, text='Telefono:* ', font=('Times', 12),bg='#fff').grid(row=6,column=0,sticky='W',padx=10, pady=(10,5))
        self.svtelefono = StringVar()
        self.telefono = ttk.Entry(frame, width=50, font=('Times', 14),textvariable=self.svtelefono).grid(row=6,column=1,padx=10, pady=(10,5))

        Label(frame, text='Fecha de nacimiento: ', font=('Times', 12),bg='#fff').grid(row=7,column=0,sticky='W',padx=10, pady=(10,5))
        self.svfnacimiento = StringVar()
        self.fnacimiento = ttk.Entry(frame, width=50, font=('Times', 14),textvariable=self.svfnacimiento).grid(row=7,column=1,padx=10, pady=(10,5))

        Label(frame, text='Edad: ', font=('Times', 12),bg='#fff').grid(row=8,column=0,sticky='W',padx=10, pady=(10,5))
        self.svedad = StringVar()
        self.edad = ttk.Spinbox(frame, width=48,from_=1, to=100, font=('Times', 14),textvariable=self.svedad).grid(row=8,column=1,padx=10, pady=(10,5))
        self.svedad.set('0')

        Label(frame, text='Antecedentes: ', font=('Times', 12),bg='#fff').grid(row=9,column=0,sticky='W',padx=10,pady=(10,0))
        self.svantecedentes = StringVar()
        self.antecedentes = ttk.Entry(frame, width=50, font=('Times', 14),textvariable=self.svantecedentes).grid(row=9,column=1,padx=10, pady=(10,5))

        self.message = tk.Label(frame, text="", font=('Times', 12), fg="green", bg='#fff', anchor="center")
        self.message.grid(column=0, row=10,sticky='w', padx=20, pady=(10,20))

        self.btnGuardar = tk.Button(frame, text="Registrar",width=10, font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", cursor='hand2',command=self.add_pacientes, activebackground='#fff', activeforeground='#3a7ff6')
        self.btnGuardar.grid(column=1, row=10,columnspan=2,sticky='N', padx=20, pady=(10,20))

        self.btnCancelar = tk.Button(frame, text="Cancelar",width=10, font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", cursor='hand2',command=self.limpiarRegistro, activebackground='#fff', activeforeground='#3a7ff6')
        self.btnCancelar.grid(column=1, row=10,columnspan=2, padx=20, pady=(10,20), sticky='E')
        #===================== Fin Formulario =====================

        #===================== Inicio Opciones =====================
        frame_botones = tk.Frame(frame_fondo, bd=0, relief=tk.SOLID, bg='#fff')
        frame_botones.grid(row=0,column=1,sticky='NW')

        frame_butons =  LabelFrame(frame_botones,text='Opciones del paciente', font=('Times', 15, 'bold'),bg='#fff')
        frame_butons.grid(column=1,row=0,padx=(10,20), pady=10)

        Label(frame_butons, text='Buscar documento: ', font=('Times', 12),bg='#fff').grid(row=0,column=0,sticky='W',padx=10, pady=(10,5))
        self.DBuscar = StringVar()
        self.EntrybuscarC = ttk.Entry(frame_butons, width=50, font=('Times', 14), textvariable=self.DBuscar).grid(row=1,column=0,padx=10, pady=(10,5))

        Label(frame_butons, text='Buscar apellido: ', font=('Times', 12),bg='#fff').grid(row=2,column=0,sticky='W',padx=10, pady=(10,5))
        self.ABuscar = StringVar()
        self.EntrybuscarA = ttk.Entry(frame_butons, width=50,font=('Times', 14), textvariable=self.ABuscar).grid(row=3,column=0,padx=10, pady=10)

        self.btnBuscar = tk.Button(frame_butons, text="Buscar",width=10, font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", cursor='hand2', activebackground='#fff', activeforeground='#3a7ff6', command=self.get_pacientes)
        self.btnBuscar.grid(column=0, row=4, padx=10, pady=10,sticky=NSEW)

        self.btnEditar = tk.Button(frame_butons, text="Editar",width=20, font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", cursor='hand2', activebackground='#fff', activeforeground='#3a7ff6',command=self.editarPaciente)
        self.btnEditar.grid(column=0, row=5, padx=(10,0),pady=10,sticky='WN')

        self.btnEliminar = tk.Button(frame_butons, text="Eliminar",width=20, font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", cursor='hand2', activebackground='#fff', activeforeground='#3a7ff6', command=self.eliminarPaciente)
        self.btnEliminar.grid(column=0, row=5,padx=(0,10),pady=10,sticky='EN')

        self.btnActuaizar = tk.Button(frame_butons, text="Actualizar",width=20, font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", cursor='hand2',command=self.editardatos, activebackground='#fff', activeforeground='#3a7ff6')
        self.btnActuaizar.grid(column=0, row=6, padx=(10,0),pady=10,sticky='WN')

        self.btnHisria = tk.Button(frame_butons, text="Historial",width=20, font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", cursor='hand2', activebackground='#fff', activeforeground='#3a7ff6',command=self.historiaMed)
        self.btnHisria.grid(column=0, row=6 ,padx=(0,11),pady=10,sticky='EN')
        #===================== fin Opciones =====================

        #===================== Inicio Tabla =====================
        frame_tabla = tk.Frame(frame_fondo, bd=0, relief=tk.SOLID, bg='#fff')
        frame_tabla.grid(row=1,column=0, columnspan=2,sticky=NSEW)

        self.tabla = ttk.Treeview(frame_tabla, column=('Documento','Nombre', 'Primer apellido', 'Segundo apellido', 'Correo', 'Telefono', 'Fecha de nacimiento', 'edad', 'Antecedentes'))
        self.tabla.grid(row=11,column=0, columnspan=10,sticky='nse', padx=(20,0), pady=10)
        self.scroll = ttk.Scrollbar(frame_tabla, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=11,column=11,sticky='nse',padx=(0,10), pady=10)
        self.tabla.config(yscrollcommand=self.scroll.set)
        self.tabla.tag_configure('evenrow', background='#3a7ff6')

        self.tabla.heading('#0',text='Id')
        self.tabla.heading('#1',text='Documento')
        self.tabla.heading('#2',text='Nombre')
        self.tabla.heading('#3',text='Primer apellido')
        self.tabla.heading('#4',text='Segundo apellido')
        self.tabla.heading('#5',text='Correo')
        self.tabla.heading('#6',text='Telefono')
        self.tabla.heading('#7',text='F. nacimiento')
        self.tabla.heading('#8',text='edad')
        self.tabla.heading('#9',text='Antecedentes')

        self.tabla.column('#0', anchor=W, width=50)
        self.tabla.column('#1', anchor=W, width=80)
        self.tabla.column('#2', anchor=W, width=120)
        self.tabla.column('#3', anchor=W, width=120)
        self.tabla.column('#4', anchor=W, width=120)
        self.tabla.column('#5', anchor=W, width=250)
        self.tabla.column('#6', anchor=W, width=80)
        self.tabla.column('#7', anchor=W, width=100)
        self.tabla.column('#8', anchor=W, width=50)
        self.tabla.column('#9', anchor=W, width=300)

        self.get_pacientes()
        #===================== Fin Tabla =====================

        #===================== Inicio Citas =====================
        frames_citas = tk.Frame(self.citas, bd=0,relief=tk.SOLID, bg='#fff')
        frames_citas.pack(side="left", expand=tk.YES, fill=tk.BOTH)

        frame_form = tk.Frame(frames_citas, bd=0, relief=tk.SOLID, bg='#fff')
        frame_form.grid(row=0, column=0, sticky='W')

        frame_campos = LabelFrame(frame_form, text='Agendar cita', font=('Times', 15, 'bold'),bg='#fff')
        frame_campos.grid(column=0,row=0,padx=20, pady=10)

        Label(frame_campos, text='Documento: ', font=('Times', 12),bg='#fff').grid(row=1,column=0,sticky='W',padx=10, pady=(10,5))
        self.svdocumentcita = StringVar()
        self.Entrydocumento = ttk.Entry(frame_campos, width=55, font=('Times', 14), textvariable=self.svdocumentcita).grid(row=1,column=1,padx=10, pady=(10,5))
        self.svdocumentcita.set('')

        Label(frame_campos, text='Nombre completo: ', font=('Times', 12),bg='#fff').grid(row=2,column=0,sticky='W',padx=10, pady=(10,5))
        self.svnombrecita = StringVar()
        self.Entrynombre = ttk.Entry(frame_campos, width=55, font=('Times', 14),textvariable=self.svnombrecita).grid(row=2,column=1,padx=10, pady=(10,5))

        Label(frame_campos, text='Correo: ', font=('Times', 12),bg='#fff').grid(row=3,column=0,sticky='W',padx=10, pady=(10,5))
        self.svcorreocita = StringVar()
        self.Entrycorreo = ttk.Entry(frame_campos, width=55, font=('Times', 14),textvariable=self.svcorreocita).grid(row=3,column=1,padx=10, pady=(10,5))

        Label(frame_campos, text='Telefono: ', font=('Times', 12),bg='#fff').grid(row=4,column=0,sticky='W',padx=10, pady=(10,5))
        self.svtelefonocita = StringVar()
        self.Entrytelefono = ttk.Entry(frame_campos, width=55, font=('Times', 14),textvariable=self.svtelefonocita).grid(row=4,column=1,padx=10, pady=(10,5))

        frameCalendario = tk.Frame(frames_citas, width=500, height=100,bd=0,relief=tk.SOLID, bg='#fff')
        frameCalendario.grid(row=0,column=1,sticky='N')

        self.svCalendario = StringVar(frameCalendario, Calendar.date.today().strftime("%d/%m/%y"))
        self.calendar = tc.Calendar(frameCalendario, selectmode='day', year=2022, month=1, day=1, date_pattern='dd/mm/yy',textvariable=self.svCalendario, headersbackground='#3a7ff6')
        self.calendar.pack(ipady=75,ipadx=190,padx=(0,20), pady=20,fill='both', expand=True)
        self.svCalendario.trace('w', self.enviarFecha)

        Label(frame_campos, text='Fecha: ', font=('Times', 12),bg='#fff').grid(row=5,column=0,sticky='W',padx=10, pady=(10,5))
        self.svdia = StringVar()
        self.Entrydia = ttk.Entry(frame_campos, width=55, font=('Times', 14),textvariable=self.svdia, state='disable').grid(row=5,column=1,padx=10, pady=(10,5))

        self.hora_opciones=['6:00 A.m.','6:30 A.m.','7:00 A.m.',
            '7:30 A.m.','8:00 A.m.','8:30 A.m.','9:00 A.m.',
            '9:30 A.m.','10:00 A.m.','10:30 A.m.','11:00 A.m.',
            '11:30 A.m.','1:30 P.m.','2:00 P.m.','2:30 P.m.',
            '3:00 P.m.','3:30 P.m.','4:00 P.m.','4:30 P.m.',
            '5:00 P.m.','5:30 P.m.','6:00 P.m.']

        Label(frame_campos, text='Hora: ', font=('Times', 12),bg='#fff').grid(row=8,column=0,sticky='W',padx=10, pady=(10,5))
        self.svhora = StringVar()
        self.hora = ttk.Spinbox(frame_campos, width=53, font=('Times', 14),values=self.hora_opciones,textvariable=self.svhora).grid(row=8,column=1,padx=10, pady=(10,5))
        self.svhora.set('6:00 A.m.')

        self.messageCitas = tk.Label(frame_campos, text="", font=('Times', 12), fg="green", bg='#fff', anchor="center")
        self.messageCitas.grid(column=0, row=10,sticky='w', padx=20, pady=(10,20))

        self.btnGuardar = tk.Button(frame_campos, text="Agendar",width=10, font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", cursor='hand2', activebackground='#fff', activeforeground='#3a7ff6', command=self.agendar)
        self.btnGuardar.grid(column=1, row=10,columnspan=2,sticky='E', padx=20, pady=(10,20))

        self.btnEditar = tk.Button(frame_campos, text="Editar",width=10, font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", cursor='hand2', activebackground='#fff', activeforeground='#3a7ff6', command=self.editarAgenda)
        self.btnEditar.grid(column=1, row=10,columnspan=2,sticky='W', padx=20, pady=(10,20))

    #===================== Inicio tabla citas =====================

        frame_table = tk.Frame(frames_citas, bd=0, relief=tk.SOLID, bg='#fff')
        frame_table.grid(row=1, column=0,columnspan=2, sticky='ns')

        self.tablaCita = ttk.Treeview(frame_table, column=('Documento','Nombre Completo', 'Correo','Telefono', 'fecha', 'hora'))
        self.tablaCita.grid(row=5,column=0,sticky='nse', padx=(20,0), pady=10)
        self.scrollCita = ttk.Scrollbar(frame_table, orient='vertical', command=self.tablaCita.yview)
        self.scrollCita.grid(row=5,column=5,sticky='nse',padx=(0,10), pady=10)
        self.tablaCita.configure(yscrollcommand=self.tablaCita.set)
        self.tablaCita.tag_configure('evenrow', background='#3a7ff6')

        self.tablaCita.heading('#0',text='Id')
        self.tablaCita.heading('#1',text='Documento')
        self.tablaCita.heading('#2',text='Nombre completo')
        self.tablaCita.heading('#3',text='Correo')
        self.tablaCita.heading('#4',text='Telefono')
        self.tablaCita.heading('#5',text='Fecha')
        self.tablaCita.heading('#6',text='Hora')

        self.tablaCita.column('#0', anchor=W, width=50)
        self.tablaCita.column('#1', anchor=W, width=100)
        self.tablaCita.column('#2', anchor=W, width=150)
        self.tablaCita.column('#3', anchor=W, width=250)
        self.tablaCita.column('#4', anchor=W, width=130)
        self.tablaCita.column('#5', anchor=W, width=80)
        self.tablaCita.column('#6', anchor=W, width=80)

        self.get_agenda()

        self.btnselecionarcita = tk.Button(frame_table, text="Seleccionar",width=10, font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", cursor='hand2', activebackground='#fff', activeforeground='#3a7ff6',command=self.llamar_Cita)
        self.btnselecionarcita.grid(column=0, row=6,columnspan=2, padx=20, pady=(10,20),sticky='W')

        self.btnEliminarCita = tk.Button(frame_table, text="Eliminar",width=10, font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", cursor='hand2', activebackground='#fff', activeforeground='#3a7ff6', command=self.dell_cita)
        self.btnEliminarCita.grid(column=0, row=6,columnspan=2, padx=20, pady=(10,20),sticky='E')

    # #===================== Fin tabla citas =====================

    def agendar(self):
        doc = self.svdocumentcita.get()
        nom = self.svnombrecita.get()
        mail = self.svcorreocita.get()
        tel = self.svtelefonocita.get()
        day = self.svdia.get()
        time = self.svhora.get()
        if doc.isdigit() != True:
            messagebox.showerror(message="Documento invalido.",title="Ups!, algo ha salido mal")
        elif '@' not in mail:
            messagebox.showerror(message="El formato del correo es invalido.",title="Ups!, algo ha salido mal")
        elif len(tel) < 10 or len(tel) > 10:
            messagebox.showerror(message="El numero de telefono debe ser de 10 cifras.",title="Ups!, algo ha salido mal")
        else:
            query = f'INSERT INTO Agenda (Documento,Nombre,Correo,Telefono,Fecha,Hora) VALUES (?,?,?,?,?,?)'
            parameters = (doc,nom,mail,tel,day,time)
            conexion.run_query(query, parameters)
            self.svdocumentcita.set('')
            self.svnombrecita.set('')
            self.svcorreocita.set('')
            self.svtelefonocita.set('')
            self.svdia.set('')
            self.svhora.set('6:00 A.m.')
        self.get_agenda()

    def get_agenda(self):
        registros = self.tablaCita.get_children()
        for elemnt in registros:
            self.tablaCita.delete(elemnt)
        query = f'SELECT * FROM Agenda'
        conexion.run_query(query)
        db_rows = conexion.run_query(query)
        for row in db_rows:
            self.tablaCita.insert('', 0, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))

    def editarAgenda(self):
        idCita = self.tablaCita.item(self.tablaCita.selection())['text']
        doc = self.svdocumentcita.get()
        nom = self.svnombrecita.get()
        mail = self.svcorreocita.get()
        tel = self.svtelefonocita.get()
        day = self.svdia.get()
        time = self.svhora.get()
        query = f'UPDATE Agenda SET Documento = ?, Nombre = ?, Correo = ?, Telefono = ?, Fecha = ?, Hora = ? WHERE idCita = {idCita}'
        parameters = (doc, nom, mail, tel, day, time)
        conexion.run_query(query, parameters)
        self.svdocumentcita.set('')
        self.svnombrecita.set('')
        self.svcorreocita.set('')
        self.svtelefonocita.set('')
        self.svdia.set('')
        self.svhora.set('6:00 A.m.')
        self.idCita = None
        self.get_agenda()


    def llamar_Cita(self):
        try:
            self.idPaciente = self.tablaCita.item(self.tablaCita.selection())['text']
            self.documentcita = self.tablaCita.item(self.tablaCita.selection())['values'][0]
            self.nombrecita = self.tablaCita.item(self.tablaCita.selection())['values'][1]
            self.correocita = self.tablaCita.item(self.tablaCita.selection())['values'][2]
            self.telefonocita = self.tablaCita.item(self.tablaCita.selection())['values'][3]
            self.diacita = self.tablaCita.item(self.tablaCita.selection())['values'][4]
            self.horacita = self.tablaCita.item(self.tablaCita.selection())['values'][5]

            self.svdocumentcita.set(self.documentcita)
            self.svnombrecita.set(self.nombrecita)
            self.svcorreocita.set(self.correocita)
            self.svtelefonocita.set(self.telefonocita)
            self.svdia.set(self.diacita)
            self.svhora.set(self.horacita)
        except:
            messagebox.showerror(message="Error al editar paciente.",title="Ups!, algo ha salido mal")

    def dell_cita(self):
        self.idCita = self.tablaCita.item(self.tablaCita.selection())['text']
        if self.idCita == '':
            messagebox.showerror(message="Seleccioné la historia que desea eliminar.",title="Ups!, algo ha salido mal")
        else:
            msg_box = messagebox.askquestion('Eliminar', f'¿Esta seguro de eliminar la cita: {self.idCita}?',icon='warning')
            if msg_box == 'yes':
                query = f'DELETE FROM Agenda WHERE idCita = {self.idCita}'
                conexion.run_query(query)
        self.get_agenda()

    # #===================== Fin Citas =====================

    def historiaMed(self):
        self.idPaciente = self.tabla.item(self.tabla.selection())['text']
        if self.idPaciente == '':
            messagebox.showerror(message="Seleccioné un paciente para ver el historial.",title="Ups!, algo ha salido mal")
        else:
            self.topHistoriaMedica = Toplevel()
            self.topHistoriaMedica.title('Historia del paciente')
            self.topHistoriaMedica.iconbitmap('Img/DntLogo.ico')
            self.topHistoriaMedica.resizable(0,0)
            self.topHistoriaMedica.config(bg='#fff')

            self.tablaHistoria = ttk.Treeview(self.topHistoriaMedica, column=('Apellidos',' Fecha Historia','Motivo','Examen Previo','Tratamiento','Detalle'))
            self.tablaHistoria.grid(row=0, column=0, columnspan=7,sticky='nse')
            self.scrollHistoria = ttk.Scrollbar(self.topHistoriaMedica, orient='vertical', command=self.tablaHistoria.yview)
            self.scrollHistoria.grid(row=0,column=8,sticky='nse')

            self.tablaHistoria.configure(yscrollcommand=self.scrollHistoria.set)

            self.tablaHistoria.heading('#0', text='Id')
            self.tablaHistoria.heading('#1', text='Apellidos')
            self.tablaHistoria.heading('#2', text='Fecha y hora')
            self.tablaHistoria.heading('#3', text='Motivo')
            self.tablaHistoria.heading('#4', text='Examen Previo')
            self.tablaHistoria.heading('#5', text='Tratamiento')
            self.tablaHistoria.heading('#6', text='Detalles')

            self.tablaHistoria.column('#0', anchor=W, width=50)
            self.tablaHistoria.column('#1', anchor=W, width=120)
            self.tablaHistoria.column('#2', anchor=W, width=110)
            self.tablaHistoria.column('#3', anchor=W, width=120)
            self.tablaHistoria.column('#4', anchor=W, width=250)
            self.tablaHistoria.column('#5', anchor=W, width=200)
            self.tablaHistoria.column('#6', anchor=W, width=500)

            registros = self.tablaHistoria.get_children()
            for elemnt in registros:
                self.tabla.delete(elemnt)

            self.get_historial()

            self.btnAgregarH = tk.Button(self.topHistoriaMedica, text='Agregar historia', width=20, font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", cursor='hand2', activebackground='#fff', activeforeground='#3a7ff6', command=self.topAgregarH)
            self.btnAgregarH.grid(row=2, column=0,padx=10,pady=5)

            self.btnEditarH = tk.Button(self.topHistoriaMedica, text='Editar historia', width=20, font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", cursor='hand2', activebackground='#fff', activeforeground='#3a7ff6', command=self.topEditar)
            self.btnEditarH.grid(row=2, column=1,padx=10,pady=5)

            self.btnEliminarH = tk.Button(self.topHistoriaMedica, text='Eliminar historia', width=20, font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", cursor='hand2', activebackground='#fff', activeforeground='#3a7ff6', command=self.dell_historial)
            self.btnEliminarH.grid(row=2, column=2,padx=10,pady=5)

            self.btnSalirH = tk.Button(self.topHistoriaMedica, text='Salir', width=20, font=('Times', 15), bg='#fff', bd=0, fg="grey", cursor='hand2', activebackground='#fff', activeforeground='#3a7ff6', command=self.topHistoriaMedica.destroy)
            self.btnSalirH.grid(row=2, column=5,padx=10,pady=5, sticky='E')

    def topAgregarH(self):
        self.topAgregarHistoria = Toplevel()
        self.topAgregarHistoria.title('Agregar historia')
        self.topAgregarHistoria.iconbitmap('Img/DntLogo.ico')
        self.topAgregarHistoria.resizable(0,0)

        frames_historia = tk.Frame(self.topAgregarHistoria, bd=0,relief=tk.SOLID, bg='#fff')
        frames_historia.pack(side="left", expand=tk.YES, fill=tk.BOTH)

        self.frameDatosH = tk.LabelFrame(frames_historia,text='Agregar historia',font=('Times', 15, 'bold'),bg='#fff')
        self.frameDatosH.grid(row=0, column=0, sticky='W', padx=20, pady=(20,5))

        Label(self.frameDatosH, text='Motivo de consulta: ', font=('Times', 12),bg='#fff').grid(row=0,column=0,sticky='W',padx=10, pady=(10,5))
        self.svMotivo = StringVar()
        self.entryMotivo = ttk.Entry(self.frameDatosH, width=50, font=('Times', 14), textvariable=self.svMotivo).grid(row=0,column=1,padx=10, pady=(10,5))

        Label(self.frameDatosH, text='Enfermedad actual: ', font=('Times', 12),bg='#fff').grid(row=1,column=0,sticky='W',padx=10, pady=(10,5))
        self.svExamenP = StringVar()
        self.entryExamenP = ttk.Entry(self.frameDatosH, width=50, font=('Times', 14), textvariable=self.svExamenP).grid(row=1,column=1,padx=10, pady=(10,5))

        Label(self.frameDatosH, text='Tratamiento: ', font=('Times', 12),bg='#fff').grid(row=2,column=0,sticky='W',padx=10, pady=(10,5))
        self.svTratamiento = StringVar()
        self.entryTratamiento = ttk.Entry(self.frameDatosH, width=50, font=('Times', 14), textvariable=self.svTratamiento).grid(row=2,column=1,padx=10, pady=(10,5))

        Label(self.frameDatosH, text='Anexos: ', font=('Times', 12),bg='#fff').grid(row=3,column=0,sticky='W',padx=10, pady=(10,5))
        self.svDetalle = StringVar()
        self.entryDetalle = ttk.Entry(self.frameDatosH, width=50, font=('Times', 14), textvariable=self.svDetalle).grid(row=3,column=1,padx=10, pady=(10,5))

        Label(self.frameDatosH, text='Fecha y hora: ', font=('Times', 12),bg='#fff').grid(row=4,column=0,sticky='W',padx=10, pady=(10,5))
        self.svFechaH = StringVar()
        self.entryFechaH = ttk.Entry(self.frameDatosH, width=50, font=('Times', 14), textvariable=self.svFechaH, state='disable').grid(row=4,column=1,padx=10, pady=(10,5))
        self.svFechaH.set(datetime.today().strftime('%d/%m/%y %I:%M %p'))

        frame_fhistoria = tk.Frame(frames_historia, bd=0,relief=tk.SOLID, bg='#fff')
        frame_fhistoria.grid(row=1, column=0, sticky='W', padx=20, pady=20)

        self.btnGuardarH = tk.Button(frame_fhistoria, text='Guardar historia', width=20, font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", cursor='hand2', activebackground='#fff', activeforeground='#3a7ff6',command=self.agregarH)
        self.btnGuardarH.grid(row=0, column=0,padx=10,pady=5,sticky='W')

        self.btnSalirA = tk.Button(frame_fhistoria, text='Cancelar', width=20, font=('Times', 15), bg='#fff', bd=0, fg="grey", cursor='hand2', activebackground='#fff', activeforeground='#3a7ff6', command=self.topAgregarHistoria.destroy)
        self.btnSalirA.grid(row=0, column=1,padx=(120,20),pady=5, sticky='E')

    def agregarH(self):
        self.idPaciente = self.tabla.item(self.tabla.selection())['text']
        motivo = self.svMotivo.get()
        examen = self.svExamenP.get()
        tratamiento = self.svTratamiento.get()
        detalle = self.svDetalle.get()
        fyh = self.svFechaH.get()
        query = f'INSERT INTO Historial (idPaciente,fechaHistoria,motivo,examen,tratamiento,detalle) VALUES ({self.idPaciente},?,?,?,?,?)'
        parameters = (fyh,motivo,examen,tratamiento,detalle)
        conexion.run_query(query, parameters)
        self.topAgregarHistoria.destroy()
        self.get_historial()

    def get_historial(self):
        self.idPaciente = self.tabla.item(self.tabla.selection())['text']
        registros = self.tablaHistoria.get_children()
        for elemnt in registros:
            self.tablaHistoria.delete(elemnt)
        query = f'SELECT h.IdHistoria, p.PApellido || " " || p.SApellido as Apellidos, h.fechaHistoria, h.motivo, h.examen, h.tratamiento, h.detalle FROM Historial h INNER JOIN Pacientes p ON p.IdPaciente = h.IdPaciente WHERE p.IdPaciente = {self.idPaciente}'
        conexion.run_query(query)
        db_rows = conexion.run_query(query)
        for row in db_rows:
            self.tablaHistoria.insert('', 0, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6]))

    def dell_historial(self):
        self.idHistoria = self.tablaHistoria.item(self.tablaHistoria.selection())['text']
        if self.idHistoria == '':
            messagebox.showerror(message="Seleccioné la historia que desea eliminar.",title="Ups!, algo ha salido mal")
        else:
            msg_box = messagebox.askquestion('Eliminar', f'¿Esta seguro de eliminar la historia con el id: {self.idHistoria}?',icon='warning')
            if msg_box == 'yes':
                query = f'DELETE FROM Historial WHERE idHistoria = {self.idHistoria}'
                conexion.run_query(query)
        self.get_historial()

    def topEditar(self):
        self.idHistoria = self.tablaHistoria.item(self.tablaHistoria.selection())['text']
        if self.idHistoria == '':
            messagebox.showerror(message="Seleccioné la historia a editar.",title="Ups!, algo ha salido mal")
        else:
            self.topEditarHistoria = Toplevel()
            self.topEditarHistoria.title('Editar historia')
            self.topEditarHistoria.iconbitmap('Img/DntLogo.ico')
            self.topEditarHistoria.resizable(0,0)

            frames_historia = tk.Frame(self.topEditarHistoria, bd=0,relief=tk.SOLID, bg='#fff')
            frames_historia.pack(side="left", expand=tk.YES, fill=tk.BOTH)

            self.frameDatosH = tk.LabelFrame(frames_historia,text='Editar historia',font=('Times', 15, 'bold'),bg='#fff')
            self.frameDatosH.grid(row=0, column=0, sticky='W', padx=20, pady=(20,5))

            Label(self.frameDatosH, text='Motivo de consulta: ', font=('Times', 12),bg='#fff').grid(row=0,column=0,sticky='W',padx=10, pady=(10,5))
            self.svMotivoE = StringVar()
            self.entryMotivoE = ttk.Entry(self.frameDatosH, width=50, font=('Times', 14), textvariable=self.svMotivoE).grid(row=0,column=1,padx=10, pady=(10,5))
            self.svMotivoE.set(self.tablaHistoria.item(self.tablaHistoria.selection())['values'][2])

            Label(self.frameDatosH, text='Enfermedad actual: ', font=('Times', 12),bg='#fff').grid(row=1,column=0,sticky='W',padx=10, pady=(10,5))
            self.svExamenPE = StringVar()
            self.entryExamenPE = ttk.Entry(self.frameDatosH, width=50, font=('Times', 14), textvariable=self.svExamenPE).grid(row=1,column=1,padx=10, pady=(10,5))
            self.svExamenPE.set(self.tablaHistoria.item(self.tablaHistoria.selection())['values'][3])

            Label(self.frameDatosH, text='Tratamiento: ', font=('Times', 12),bg='#fff').grid(row=2,column=0,sticky='W',padx=10, pady=(10,5))
            self.svTratamientoE = StringVar()
            self.entryTratamientoE = ttk.Entry(self.frameDatosH, width=50, font=('Times', 14), textvariable=self.svTratamientoE).grid(row=2,column=1,padx=10, pady=(10,5))
            self.svTratamientoE.set(self.tablaHistoria.item(self.tablaHistoria.selection())['values'][4])

            Label(self.frameDatosH, text='Anexos: ', font=('Times', 12),bg='#fff').grid(row=3,column=0,sticky='W',padx=10, pady=(10,5))
            self.svDetalleE = StringVar()
            self.entryDetalleE = ttk.Entry(self.frameDatosH, width=50, font=('Times', 14), textvariable=self.svDetalleE).grid(row=3,column=1,padx=10, pady=(10,5))
            self.svDetalleE.set(self.tablaHistoria.item(self.tablaHistoria.selection())['values'][5])

            Label(self.frameDatosH, text='Fecha y hora: ', font=('Times', 12),bg='#fff').grid(row=4,column=0,sticky='W',padx=10, pady=(10,5))
            self.svFechaHE = StringVar()
            self.entryFechaHE = ttk.Entry(self.frameDatosH, width=50, font=('Times', 14), textvariable=self.svFechaHE, state='disable').grid(row=4,column=1,padx=10, pady=(10,5))
            self.svFechaHE.set(self.tablaHistoria.item(self.tablaHistoria.selection())['values'][1])

            frame_fhistoria = tk.Frame(frames_historia, bd=0,relief=tk.SOLID, bg='#fff')
            frame_fhistoria.grid(row=1, column=0, sticky='W', padx=20, pady=20)

            self.btnGuardarH = tk.Button(frame_fhistoria, text='Editar historia', width=20, font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff", cursor='hand2', activebackground='#fff', activeforeground='#3a7ff6',command=self.editar)
            self.btnGuardarH.grid(row=0, column=0,padx=10,pady=5,sticky='W')

            self.btnSalirA = tk.Button(frame_fhistoria, text='Cancelar', width=20, font=('Times', 15), bg='#fff', bd=0, fg="grey", cursor='hand2', activebackground='#fff', activeforeground='#3a7ff6', command=self.topEditarHistoria.destroy)
            self.btnSalirA.grid(row=0, column=1,padx=(120,20),pady=5, sticky='E')

    def editar(self):
        self.idHistoria = self.tablaHistoria.item(self.tablaHistoria.selection())['text']
        motivo = self.svMotivoE.get()
        examen = self.svExamenPE.get()
        tratamiento = self.svTratamientoE.get()
        detalle = self.svDetalleE.get()
        fyh = self.svFechaHE.get()
        query = f'UPDATE Historial SET fechaHistoria = ?, motivo = ?, examen = ?, tratamiento = ?, detalle = ? WHERE idHistoria = {self.idHistoria}'
        parameters = (fyh,motivo,examen,tratamiento,detalle)
        conexion.run_query(query, parameters)
        self.topEditarHistoria.destroy()
        self.get_historial()

    def get_pacientes(self):
        doc =  self.DBuscar.get()
        ape = self.ABuscar.get()
        registros = self.tabla.get_children()
        for elemnt in registros:
            self.tabla.delete(elemnt)
        if len(doc) == 0 and len(ape) == 0:
            query = 'SELECT * FROM Pacientes WHERE estado = 1'
            db_rows = conexion.run_query(query)
            for row in db_rows:
                self.tabla.insert('', 0, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
        elif len(doc) > 0:
                query = f'SELECT * FROM Pacientes WHERE documento = {doc}'
                db_rows = conexion.run_query(query)
                for row in db_rows:
                    self.tabla.insert('', 0, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
                self.DBuscar.set('')
        elif len(ape) > 0:
                query = f'SELECT * FROM Pacientes WHERE PApellido = "{ape}"'
                db_rows = conexion.run_query(query)
                for row in db_rows:
                    self.tabla.insert('', 0, text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
                self.ABuscar.set('')

    def validation(self):
        doc = self.svdocument.get()
        nom = self.svnombre.get()
        ape = self.svapellido.get()
        tel = self.svtelefono.get()
        return len(doc) != 0 and len(nom) != 0 and len(ape) != 0 and len(tel) != 0

    def add_pacientes(self):
        doc = self.svdocument.get()
        nom = self.svnombre.get()
        ape = self.svapellido.get()
        sap = self.svsapellido.get()
        corr = self.svcorreo.get()
        tel = self.svtelefono.get()
        fnaci = self.svfnacimiento.get()
        edad = self.svedad.get()
        antec = self.svantecedentes.get()
        if self.validation():
            if doc.isdigit() != True:
                messagebox.showerror(message="Documento invalido.",title="Ups!, algo ha salido mal")
            elif '@' not in corr:
                messagebox.showerror(message="El formato del correo es invalido.",title="Ups!, algo ha salido mal")
            elif len(tel) < 10 or len(tel) > 10:
                print('El numero de telefono debe ser de 10 cifras')
            elif edad.isdigit() != True and len(edad) > 2:
                print('El la edad es incorrecta')
            else:
                query = 'INSERT INTO Pacientes (documento,nombre,PApellido,SApellido,correo,telefono,fechaNacimiento,edad,antecedentes,estado) VALUES (?,?,?,?,?,?,?,?,?,1)'
                parameters = (doc, nom, ape, sap, corr, tel, fnaci, edad, antec)
                conexion.run_query(query, parameters)
                self.svdocument.set('')
                self.svnombre.set('')
                self.svapellido.set('')
                self.svsapellido.set('')
                self.svcorreo.set('')
                self.svtelefono.set('')
                self.svfnacimiento.set('')
                self.svedad.set('0')
                self.svantecedentes.set('')
                messagebox.showeinfo(message="Paciente agregado.",title="Mensaje")
                self.get_pacientes()
        else:
            messagebox.showerror(message="Algunos campos son requeridos.",title="Ups!, algo ha salido mal")
        self.get_pacientes()

    def editardatos(self):
        idPaciente = self.tabla.item(self.tabla.selection())['text']
        doc = self.svdocument.get()
        nom = self.svnombre.get()
        ape = self.svapellido.get()
        sap = self.svsapellido.get()
        corr = self.svcorreo.get()
        tel = self.svtelefono.get()
        fnaci = self.svfnacimiento.get()
        edad = self.svedad.get()
        antec = self.svantecedentes.get()
        if self.validation():
            query = f'UPDATE Pacientes SET documento = ?, nombre = ?, PApellido = ?, SApellido = ?, correo = ?, telefono = ?, fechaNacimiento = ?, edad = ?, antecedentes = ?, estado = 1 WHERE idPaciente = {idPaciente}'
            parameters = (doc, nom, ape, sap, corr, tel, fnaci, edad, antec)
            conexion.run_query(query, parameters)
            self.svdocument.set('')
            self.svnombre.set('')
            self.svapellido.set('')
            self.svsapellido.set('')
            self.svcorreo.set('')
            self.svtelefono.set('')
            self.svfnacimiento.set('')
            self.svedad.set('0')
            self.svantecedentes.set('')
            self.message['text'] = 'Paciente Atualizado.'
            self.idPaciente = None
            self.get_pacientes()
        else:
            self.get_pacientes()

    def editarPaciente(self):
        try:
            self.idPaciente = self.tabla.item(self.tabla.selection())['text']
            self.documentoPaciente = self.tabla.item(self.tabla.selection())['values'][0]
            self.nombrePaciente = self.tabla.item(self.tabla.selection())['values'][1]
            self.apellidoPaciente = self.tabla.item(self.tabla.selection())['values'][2]
            self.sapellidoPaciente = self.tabla.item(self.tabla.selection())['values'][3]
            self.corroPaciente = self.tabla.item(self.tabla.selection())['values'][4]
            self.telefonoPaciente = self.tabla.item(self.tabla.selection())['values'][5]
            self.fechaNPaciente = self.tabla.item(self.tabla.selection())['values'][6]
            self.edadPaciente = self.tabla.item(self.tabla.selection())['values'][7]
            self.antecPaciente = self.tabla.item(self.tabla.selection())['values'][8]

            self.svdocument.set(self.documentoPaciente)
            self.svnombre.set(self.nombrePaciente)
            self.svapellido.set(self.apellidoPaciente)
            self.svsapellido.set(self.sapellidoPaciente)
            self.svcorreo.set(self.corroPaciente)
            self.svtelefono.set(self.telefonoPaciente)
            self.svfnacimiento.set(self.fechaNPaciente)
            self.svedad.set(self.edadPaciente)
            self.svantecedentes.set(self.antecPaciente)
        except:
            messagebox.showerror(message="Error al editar paciente.",title="Ups!, algo ha salido mal")

    def eliminarPaciente(self):
        self.idPaciente = self.tabla.item(self.tabla.selection())['text']
        msg_box = messagebox.askquestion('Eliminar', '¿Esta seguro de eliminar el paciente?',icon='warning')
        if msg_box == 'yes':
            query = f'UPDATE Pacientes SET estado = 0 WHERE idPaciente = {self.idPaciente}'
            conexion.run_query(query)
            messagebox.showinfo(message="El paciente se elimino logicamente.",title="Eliminado")
        self.editardatos()

    def limpiarRegistro(self):
        self.svdocument.set('')
        self.svnombre.set('')
        self.svapellido.set('')
        self.svsapellido.set('')
        self.svcorreo.set('')
        self.svtelefono.set('')
        self.svfnacimiento.set('')
        self.svedad.set('0')
        self.svantecedentes.set('')

    def enviarFecha(self, *args):
        self.svdia.set('' + self.svCalendario.get())
        if len(self.calendar.get_date()) > 1:
            self.svCalendario.trace('w')

        self.aplicacion.mainloop()
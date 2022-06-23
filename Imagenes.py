from tkinter import Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import StringVar, Scrollbar, Frame
import time

class Ventana(Frame):
    def __init__(self,master, *args):
        super().__init__(master, *args)

        menu = True
        color = True


        self.frame_inicio = Frame(self.master, bg='black', width=50, height=45)
        self.frame_inicio.grid_propagate(0)
        self.frame_inicio.grid(column=0, row=0, sticky='nsew')
        self.frame_menu = Frame(self.master, bg='black', width=50)
        self.frame_menu.grid_propagate(0)
        self.frame_menu.grid(column=0, row=1, sticky='nsew')
        self.frame_top = Frame(self.master, bg='black', height=50)
        self.frame_top.grid(column=1, row=0, sticky='nsew')
        self.frame_principal = Frame(self.master, bg='black')
        self.frame_principal.grid(column=1, row=1, sticky='nsew')
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.rowconfigure(0, weight=1)

        #self.widgets()

    def pantalla_inicial(self):
        self.paginas.select([self.frame_uno])

    def menu_lateral(self):
        if self.menu is True:
            for i in range(50, 170, 10):
                self.frame_menu.config(width=i)
                self.frame_inicio.config(width=i)
                self.frame_menu.update()
                clik_inicio = self.bt_cerrar.grid_forget()
                if clik_inicio is None:
                    self.bt_inicio.grid(column=0, row=0, padx=10, pady=10)
                    self.bt_inicio.grid_propagate(0)
                    self.bt_inicio.config(width=i)
            self.menu = False
        else:
            for i in range(170, 50, -10):
                self.frame_menu.config(width=i)
                self.frame_inicio.config(width=i)
                self.frame_menu.update()
                clik_inicio = self.bt_inicio.grid_forget()
                if clik_inicio is None:
                    self.frame_menu.grid_propagate(0)
                    self.bt_cerrar.grid(column=0, row=0, padx=10, pady=10)
                    self.bt_cerrar.grid_propagate(0)
                    self.bt_cerrar.config(width=i)
            self.menu = True

    def widgets(self):
        self.imagen_inicio = PhotoImage(file='inicio.png')
        self.imagen_menu = PhotoImage(file='menu.png')
        self.imagen_datos = PhotoImage(file='datos.png')
        self.imagen_registrar = PhotoImage(file='escribir.png')
        self.imagen_actualizar = PhotoImage(file='actualizar.png')
        self.imagen_buscar = PhotoImage(file='buscar.png')

        self.logo = PhotoImage(file='logo.png')
        self.imagen_uno = PhotoImage(file='imagen_uno.png')
        self.imagen_dos = PhotoImage(file='imagen_dos.png')

        self.bt_inicio = Button(self.frame_inicio, image=self.imagen_inicio, bg='black', activebackground='black',
                                bd=0,
                                command=self.menu_lateral)
        self.bt_inicio.grid(column=0, row=0, padx=5, pady=10)
        self.bt_cerrar = Button(self.frame_inicio, image=self.imagen_menu, bg='black', activebackground='black',
                                bd=0,
                                command=self.menu_lateral)
        self.bt_cerrar.grid(column=0, row=0, padx=5, pady=10)

        # BOTONES Y ETIQUETAS DEL MENU LATERAL
        Button(self.frame_menu, image=self.imagen_datos, bg='black', activebackground='black', bd=0,
               command=self.pantalla_datos).grid(column=0, row=1, pady=20, padx=10)
        Button(self.frame_menu, image=self.imagen_registrar, bg='black', activebackground='black', bd=0,
               command=self.pantalla_escribir).grid(column=0, row=2, pady=20, padx=10)
        Button(self.frame_menu, image=self.imagen_actualizar, bg='black', activebackground='black', bd=0,
               command=self.pantalla_actualizar).grid(column=0, row=3, pady=20, padx=10)
        Button(self.frame_menu, image=self.imagen_buscar, bg='black', activebackground='black', bd=0,
               command=self.pantalla_buscar).grid(column=0, row=4, pady=20, padx=10)

        Label(self.frame_menu, text='Base Datos', bg='black', fg='DarkOrchid1',
              font=('Lucida Sans', 12, 'bold')).grid(
            column=1, row=1, pady=20, padx=2)
        Label(self.frame_menu, text='Registrar', bg='black', fg='DarkOrchid1',
              font=('Lucida Sans', 12, 'bold')).grid(
            column=1, row=2, pady=20, padx=2)
        Label(self.frame_menu, text=' Actualizar', bg='black', fg='DarkOrchid1',
              font=('Lucida Sans', 12, 'bold')).grid(
            column=1, row=3, pady=20, padx=2)
        Label(self.frame_menu, text='Eliminar', bg='black', fg='DarkOrchid1',
              font=('Lucida Sans', 12, 'bold')).grid(
            column=1, row=4, pady=20, padx=2)

if __name__ == "__main__":
    ventana = Tk()
    ventana.title('')
    ventana.minsize(height=475, width=795)
    ventana.geometry('1000x500+180+80')
    ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logo.png'))
    app = Ventana(ventana)
    app.mainloop()
from tkinter import Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import StringVar, Scrollbar, Frame
from tkinter import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
import os

ListaGraf = ["De Barras Contadora", "Dispersion", "Histograma", "Histogramas con graficas de distribucion"]

Cancer = {"ID": "id",
          "Diagnostico": "diagnosis",
          "Radio Promedio": "radius_mean",
          "Textura Promedio": "texture_mean",
          "Perimetro Promedio": "perimeter_mean",
          "Area Promedio": "area_mean",
          "Suavidad Promedio": "smoothness_mean",
          "Compactado Promedio": "compactness_mean",
          "Concavidad Promedio": "concavity_mean",
          "Promedio de los Puntos concavos": "concave points mean",
          "Simetria Promedio": "symmetry_mean",
          "Promedios de Fractales": "fractal_dimension_mean",
          "Radio": "radius_se",
          "Textura": "texture",
          "Perimetro": "perimeter_se",
          "Area": "area-se",
          "Suavidad": "smoothness_se",
          "Compactado": "compactness_se",
          "Concavidad": "concavity_se",
          "Puntos Concavos": "concave points_se",
          "Simetria": "symmetry_se",
          "Fractales": "fractal_dimension_se",
          "Peor Radio": "radius_worst",
          "Peor Textura": "texture_worst",
          "Peor Perimetro": "perimeter_worst",
          "Peor Area": "area_worst",
          "Peor Suavidad": "smoothness_worst",
          "Peor Compactado": "compactness_worst",
          "Peor Concavidad": "concavity_worst",
          "Peores Puntos Concavos": "concave points_worst",
          "Peor Simetria": "symmetry_worst",
          "Peores Fractales": "fractal_dimension_worst"
          }

Diabetes = {

    "Embarazos": "Pregnancies",
    "Glucosa": "Glucose",
    "Presion Sanguinea": "BloodPressure",
    "Grosor de la Piel": "SkinThickness",
    "Insulina": "Insulin",
    "BMI": "BMI",
    "Grado de la Diabetes": "DiabetesPedigreeFunction",
    "Edad": "Age",
    "Resultado": "Outcome"
                 ""
}

Vino = {
    "Acidez Arreglada": "fixed acidity",
    "Acidez Volatil": "volatile acidity",
    "Acido Citrico": "citric acid",
    "Azucar Residual": "residual sugar",
    "Cloridos": "chlorides",
    "Libre de Acido Sulfurico": "free sulfur dioxide",
    "Total de Acido Sulfurico": "total sulfur dioxide",
    "Densidad": "density",
    "pH": "pH",
    "Sulfatos": "sulphates",
    "Alcohol": "alcohol",
    "Calidad": "Calidad",
    "Id": "Id"

}

Iris = {"Id": "Id",
        "Largo del Sepalo": "SepalLengthCm",
        "Ancho del Sepalo": "SepalWidthCm",
        "Largo del Petalo": "PetalLengthCm",
        "Ancho del Petalo": "PetalWidthCm",
        "Especies": "Species"}

CSV = {"Cancer": "data.csv",
       "Iris": "iris.csv",
       "Vino": "WineQT.csv",
       "Diabetes": "diabetes.csv"}

class Ventana(Frame):
    presentacion = ["Cancer", "Iris", "Diabetes", "Vino"]
    i = 0
    text = presentacion[i]
    def __init__(self, master, *args):
        super().__init__(master, *args)

        self.menu = True
        self.color = True

        self.combobox = StringVar()
        self.grafica_type = StringVar()
        self.colorificar = StringVar()
        self.ejex = StringVar()
        self.ejey = StringVar()
        self.valor = StringVar()

        self.frame_inicio = Frame(self.master, bg='gray25', width=50, height=50)
        self.frame_inicio.grid_propagate(0)
        self.frame_inicio.grid(column=0, row=0, sticky='nsew')
        self.frame_menu = Frame(self.master, bg='gray25', width=50)
        self.frame_menu.grid_propagate(0)
        self.frame_menu.grid(column=0, row=1, sticky='nsew')
        self.frame_top = Frame(self.master, bg='gray25', height=50)
        self.frame_top.grid(column=1, row=0, sticky='nsew')
        self.frame_principal = Frame(self.master, bg='gray25')
        self.frame_principal.grid(column=1, row=1, sticky='nsew')
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.rowconfigure(0, weight=1)

        self.widgets()

    def pantalla_inicial(self):
        if not self.menu:
            for i in range(150, 45, -10):
                self.frame_menu.config(width=i)
                self.frame_inicio.config(width=i)
                self.frame_menu.update()
            self.menu = True
        self.paginas.select([self.frame_uno])

    def pantalla_datos(self):
        if not self.menu:
            for i in range(150, 45, -10):
                self.frame_menu.config(width=i)
                self.frame_inicio.config(width=i)
                self.frame_menu.update()
            self.menu = True
        self.paginas.select([self.frame_dos])
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.columnconfigure(1, weight=1)
        self.db()

    def pantalla_cancer(self):
        self.paginas.select([self.frame_cancer])
        self.frame_cancer.columnconfigure(0, weight=1)
        self.frame_cancer.columnconfigure(1, weight=1)

    def pantalla_diabetes(self):
        self.paginas.select([self.frame_diabetes])
        self.frame_diabetes.columnconfigure(0, weight=1)
        self.frame_diabetes.columnconfigure(1, weight=1)

    def pantalla_vino(self):
        self.paginas.select([self.frame_vino])
        self.frame_vino.columnconfigure(0, weight=1)
        self.frame_vino.columnconfigure(1, weight=1)

    def pantalla_iris(self):
        self.paginas.select([self.frame_iris])
        self.frame_iris.columnconfigure(0, weight=1)
        self.frame_iris.columnconfigure(1, weight=1)

    def pantalla_graficar(self):
        if not self.menu:
            for i in range(150, 45, -10):
                self.frame_menu.config(width=i)
                self.frame_inicio.config(width=i)
                self.frame_menu.update()
            self.menu = True
        self.paginas.select([self.frame_tres])
        self.frame_tres.columnconfigure(0, weight=1)
        self.frame_tres.columnconfigure(1, weight=1)

    def pantalla_graficar1(self):
        self.paginas.select([self.frame_graficar2])
        self.frame_graficar2.columnconfigure(0, weight=1)
        self.frame_graficar2.columnconfigure(1, weight=1)

    def pantalla_graficar2(self):
        self.paginas.select([self.frame_graficar3])
        self.frame_graficar3.columnconfigure(0, weight=1)
        self.frame_graficar3.columnconfigure(1, weight=1)

    def pantalla_analisis(self):
        if not self.menu:
            for i in range(150, 45, -10):
                self.frame_menu.config(width=i)
                self.frame_inicio.config(width=i)
                self.frame_menu.update()
            self.menu = True
        self.paginas.select([self.frame_cuatro])
        self.frame_cuatro.columnconfigure(0, weight=1)
        self.frame_cuatro.columnconfigure(1, weight=1)

    def pantalla_cancer_analisis(self):
        self.paginas.select([self.frame_cancer_analisis])

    def menu_lateral(self):
        if self.menu:
            for i in range(50, 150, 10):
                self.frame_menu.config(width=i)
                self.frame_inicio.config(width=i)
                self.frame_menu.update()

            self.menu = False
        else:
            for i in range(150, 45, -10):
                self.frame_menu.config(width=i)
                self.frame_inicio.config(width=i)
                self.frame_menu.update()
            self.menu = True

    def widgets(self):
        self.imagen_inicio = PhotoImage(file='inicio.png')
        self.imagen_menu = PhotoImage(file='menu.png')
        self.imagen_datos = PhotoImage(file='base_datos.png')
        self.imagen_graficas = PhotoImage(file='graficas.png')
        self.imagen_analisis = PhotoImage(file='analisis.png')

        self.imagen_cancer = PhotoImage(file='cancerv2.png')
        self.imagen_iris = PhotoImage(file='irisv2.png')
        self.imagen_diabetes = PhotoImage(file='diabetesv2.png')
        self.imagen_vino = PhotoImage(file='vinov2.png')

        self.Regresar = PhotoImage(file='button_regresarv2.png')
        self.Regresar2 = PhotoImage(file='button_regresarv1.png')
        self.Ingresar = PhotoImage(file='button_ingresarv1.png')
        self.Graficar = PhotoImage(file='button_graficarv1.png')

        self.imagen_cancer1 = PhotoImage(file='cancerv2.png')
        self.imagen_iris1 = PhotoImage(file='irisv2.png')
        self.imagen_diabetes1 = PhotoImage(file='diabetesv2.png')
        self.imagen_vino1 = PhotoImage(file='vinov2.png')

        self.logo = PhotoImage(file='logscreanv2.png')

        self.bt_inicio = Button(self.frame_inicio, image=self.imagen_menu, bg='gray25', activebackground='gray25', bd=0,
                                command=self.menu_lateral)
        self.bt_inicio.grid(column=0, row=0, pady=13, padx=8)

        Label(self.frame_inicio, text='Menu', bg='gray25', fg='gray69', font=('Verdana', 10), anchor="w")\
            .grid(column=1, row=0, pady=10, padx=10)

        # BOTONES Y ETIQUETAS DEL MENU LATERAL

        Button(self.frame_menu, image=self.imagen_inicio, bg='gray25', activebackground='gray25', bd=0,
               command=self.pantalla_inicial).grid(column=0, row=1, pady=20, padx=7)
        Button(self.frame_menu, image=self.imagen_datos, bg='gray25', activebackground='gray25', bd=0,
               command=self.pantalla_datos).grid(column=0, row=2, pady=20, padx=7)
        Button(self.frame_menu, image=self.imagen_graficas, bg='gray25', activebackground='gray25', bd=0,
               command=self.pantalla_graficar).grid(column=0, row=3, pady=20, padx=7)
        Button(self.frame_menu, image=self.imagen_analisis, bg='gray25', activebackground='gray25', bd=0,
               command=self.pantalla_analisis).grid(column=0, row=4, pady=20, padx=7)

        Label(self.frame_menu, text='Inicio', bg='gray25', fg='gray69', font=('Verdana', 10), anchor="w")\
            .grid(column=1, row=1, pady=20, padx=2)
        Label(self.frame_menu, text='Bases', bg='gray25', fg='gray69', font=('Verdana', 10), anchor="w")\
            .grid(column=1, row=2, pady=20, padx=2)
        Label(self.frame_menu, text='Gráficas', bg='gray25', fg='gray69', font=('Verdana', 10), anchor="w")\
            .grid(column=1, row=3, pady=20, padx=2)
        Label(self.frame_menu, text='Análisis', bg='gray25', fg='gray69', font=('Verdana', 10),anchor="w")\
            .grid(column=1, row=4, pady=20, padx=2)

        #############################  CREAR  PAGINAS  ##############################
        estilo_paginas = ttk.Style()
        estilo_paginas.configure("TNotebook", background='gray15', foreground='gray15', padding=0, borderwidth=0)
        estilo_paginas.theme_use('default')
        estilo_paginas.configure("TNotebook", background='gray15', borderwidth=0)
        estilo_paginas.configure("TNotebook.Tab", background="gray15", borderwidth=0)
        estilo_paginas.map("TNotebook", background=[("selected", 'gray15')])
        estilo_paginas.map("TNotebook.Tab", background=[("selected", 'gray15')], foreground=[("selected", 'gray15')]);

        # CREACCION DE LAS PAGINAS
        self.paginas = ttk.Notebook(self.frame_principal, style='TNotebook')  # , style = 'TNotebook'
        self.paginas.grid(column=0, row=0, sticky='nsew')
        self.frame_uno = Frame(self.paginas, bg='gray15')
        self.frame_dos = Frame(self.paginas, bg='gray15')
        self.frame_tres = Frame(self.paginas, bg='gray15')
        self.frame_cuatro = Frame(self.paginas, bg='gray15')
        self.frame_cinco = Frame(self.paginas, bg='gray15')

        self.frame_cancer = Frame(self.paginas, bg='gray15')
        self.frame_diabetes = Frame(self.paginas, bg='gray15')
        self.frame_vino = Frame(self.paginas, bg='gray15')
        self.frame_iris = Frame(self.paginas, bg='gray15')

        self.frame_graficar2 = Frame(self.paginas,bg='gray15')
        self.frame_graficar3 = Frame(self.paginas,bg='gray15')

        self.frame_cancer_analisis = Frame(self.paginas, bg='gray15')
        self.frame_diabetes_analisis = Frame(self.paginas, bg='gray15')
        self.frame_vino_analisis = Frame(self.paginas, bg='gray15')
        self.frame_iris_analisis = Frame(self.paginas, bg='gray15')

        self.paginas.add(self.frame_uno)
        self.paginas.add(self.frame_dos)
        self.paginas.add(self.frame_tres)
        self.paginas.add(self.frame_cuatro)
        self.paginas.add(self.frame_cinco)

        self.paginas.add(self.frame_cancer)
        self.paginas.add(self.frame_diabetes)
        self.paginas.add(self.frame_vino)
        self.paginas.add(self.frame_iris)

        self.paginas.add(self.frame_graficar2)
        self.paginas.add(self.frame_graficar3)

        self.paginas.add(self.frame_cancer_analisis)
        self.paginas.add(self.frame_diabetes_analisis)
        self.paginas.add(self.frame_vino_analisis)
        self.paginas.add(self.frame_iris_analisis)



        ##############################         PAGINAS       #############################################

        ######################## FRAME TITULO #################
        self.titulo = Label(self.frame_top, text='DB interpreter 3000', bg='gray25',
                            fg='gray80', font=('Courier', 15))
        self.titulo.pack(expand=5)

        ######################## VENTANA PRINCIPAL #################

        Label(self.frame_uno, text='Análisis de bases de datos', bg='gray15', fg='gray80',
              font=('Verdana', 30)).pack(expand=1)
        Label(self.frame_uno, image=self.logo, bg='gray15').pack(expand=1)

        #######################  CANCER  ####################
        self.frame_cancer.grid_rowconfigure(0, weight=1)
        Label(self.frame_cancer, text='Cancer',bg='gray15', fg='gray80',font=('Verdana', 25))\
            .grid(columnspan=2, column=0, row=2, pady=10)
        Label(self.frame_cancer, anchor="w", text='En esta base de datos se analizan\n'
                                                  'caracteríticas como el diametro de\n'
                                                  'la aureola o la rugosidad de la misma\n '
                                                  'para analizar si un caso tiene o no\n'
                                                  'cancer de mama'
              , bg='gray15', fg='gray80', font=('Verdana', 13))\
            .grid(columnspan=1,column=0, row=3, pady=0)
        Label(self.frame_cancer, image=self.imagen_cancer1, bg='gray15') \
            .grid(columnspan=1, column=1, row=3, pady=0)

        Button(self.frame_cancer, command=self.pantalla_datos, image=self.Regresar,bg='gray15', activebackground='gray15', bd=0)\
            .grid(columnspan=2, column=0, row=5, pady=30)

        self.frame_cancer.grid_rowconfigure(6, weight=2)

        #######################  Iris  ####################
        self.frame_iris.grid_rowconfigure(0, weight=1)
        Label(self.frame_iris, text='Iris', bg='gray15', fg='gray80', font=('Verdana', 25)) \
            .grid(columnspan=2, column=0, row=2, pady=10)
        Label(self.frame_iris, anchor="w", text='En esta base de datos se analizan\n'
                                                  'caracteríticas como el diámetro de\n'
                                                  'del pépato y el sépalo como el ancho\n '
                                                  'de los mismos para clasificar a cuál\n'
                                                  'de las tres familias registradas\n'
                                                  'pertenece la flor'
              , bg='gray15', fg='gray80', font=('Verdana', 13)) \
            .grid(columnspan=1, column=0, row=3, pady=0)
        Label(self.frame_iris, image=self.imagen_iris1, bg='gray15') \
            .grid(columnspan=1, column=1, row=3, pady=0)

        Button(self.frame_iris, command=self.pantalla_datos, image=self.Regresar, bg='gray15',
               activebackground='gray15', bd=0) \
            .grid(columnspan=2, column=0, row=5, pady=30)

        self.frame_iris.grid_rowconfigure(6, weight=2)

        #######################  Diabetes  ####################
        self.frame_diabetes.grid_rowconfigure(0, weight=1)
        Label(self.frame_diabetes, text='Diabetes', bg='gray15', fg='gray80', font=('Verdana', 25)) \
            .grid(columnspan=2, column=0, row=2, pady=10)
        Label(self.frame_diabetes, anchor="w", text='En esta base de datos se analizan\n'
                                                'caracteríticas como el diámetro de\n'
                                                'del pépato y el sépalo como el ancho\n '
                                                'de los mismos para clasificar a cuál\n'
                                                'de las tres familias registradas\n'
                                                'pertenece la flor'
              , bg='gray15', fg='gray80', font=('Verdana', 13)) \
            .grid(columnspan=1, column=0, row=3, pady=20)
        Label(self.frame_diabetes, image=self.imagen_diabetes1, bg='gray15') \
            .grid(columnspan=1, column=1, row=3, pady=20)

        Button(self.frame_diabetes, command=self.pantalla_datos, image=self.Regresar, bg='gray15',
               activebackground='gray15', bd=0) \
            .grid(columnspan=2, column=0, row=5, pady=30)

        self.frame_diabetes.grid_rowconfigure(6, weight=2)

        #######################  Vino  ####################
        self.frame_vino.grid_rowconfigure(0, weight=1)
        Label(self.frame_vino, text='Vino', bg='gray15', fg='gray80', font=('Verdana', 25)) \
            .grid(columnspan=2, column=0, row=2, pady=10)
        Label(self.frame_vino, anchor="w", text='En esta base de datos se analizan\n'
                                                    'caracteríticas como el diámetro de\n'
                                                    'del pépato y el sépalo como el ancho\n '
                                                    'de los mismos para clasificar a cuál\n'
                                                    'de las tres familias registradas\n'
                                                    'pertenece la flor'
              , bg='gray15', fg='gray80', font=('Verdana', 13)) \
            .grid(columnspan=1, column=0, row=3, pady=0)
        Label(self.frame_vino, image=self.imagen_vino1, bg='gray15') \
            .grid(columnspan=1, column=1, row=3, pady=0)

        Button(self.frame_vino, command=self.pantalla_datos, image=self.Regresar, bg='gray15',
               activebackground='gray15', bd=0) \
            .grid(columnspan=2, column=0, row=5, pady=30)

        self.frame_vino.grid_rowconfigure(6, weight=2)

        ################ GRAFICA  ####################

        Label(self.frame_tres, text='Graficar', fg='gray80', bg='gray15',
              font=('Verdana', 25)).grid(columnspan=2, column=0, row=0, pady=10)

        Label(self.frame_tres, text='Elige la base de datos', fg='gray80', bg='gray15',
              font=('Verdana', 12)).grid(columnspan=2, column=0, row=3, pady=10)
        ttk.Combobox(self.frame_tres, textvariable=self.combobox, values=list(CSV.keys()),
                     font=('Verdana', 12)).grid(columnspan=2, column=0, row=4, pady=15, padx=5)

        Label(self.frame_tres, text='¿Que tipo de grafica quieres hacer?', fg='gray80', bg='gray15',
              font=('Verdana', 12)).grid(columnspan=2, column=0, row=7, pady=10)
        ttk.Combobox(self.frame_tres, textvariable=self.grafica_type, values=ListaGraf,
                     font=('Verdana', 12)).grid(columnspan=2, column=0, row=8, pady=15, padx=5)

        Button(self.frame_tres, command=self.graficar1, image=self.Ingresar, bg='gray15',
               activebackground='gray15', bd=0).grid(columnspan=2, column=0, row=15, pady=40, padx=4)

        Button(self.frame_graficar2, command=self.graficar2, image=self.Graficar, bg='gray15',
               activebackground='gray15', bd=0).grid(columnspan=1, column=1, row=15, pady=40, padx=5)

        Button(self.frame_graficar2, command=self.pantalla_graficar, image=self.Regresar2, bg='gray15',
               activebackground='gray15', bd=0).grid(columnspan=1, column=0, row=15, pady=40, padx=5)

        Button(self.frame_graficar3, command=self.pantalla_graficar, image=self.Regresar2, bg='gray15',
               activebackground='gray15', bd=0).grid(columnspan=2, column=0, row=15, pady=40, padx=5)

        ################ Presentacion ################

        Label(self.frame_cuatro, text='Análisis', fg='gray80', bg='gray15',
              font=('Verdana', 25)).grid(columnspan=2, column=0, row=0, pady=10)

        Label(self.frame_cuatro, text=self.text, fg='DarkGoldenrod3', bg='gray15',
              font=('Verdana', 20)).grid(columnspan=4, column=0, row=2, pady=10)

        Button(self.frame_cuatro, command=self.change, image=self.Ingresar, bg='gray15',
               activebackground='gray15', bd=0).grid(columnspan=2, column=0, row=15, pady=40, padx=4)

    def change(self):
        self.i += 1
        if self.i>2:
            self.i=0
        self.pantalla_analisis()
        return self.i

    def db(self):
        Label(self.frame_dos, text='Bases de datos', fg='gray80', bg='gray15',
              font=('Verdana', 25)).grid(columnspan=2, column=0, row=0, pady=10)

        Button(self.frame_dos, command=self.pantalla_cancer, image=self.imagen_cancer, bg='gray15',
               activebackground='gray15', bd=0) \
            .grid(columnspan=1, column=0, row=3, pady=20, padx=4)
        Button(self.frame_dos, command=self.pantalla_iris, image=self.imagen_iris, bg='gray15',
               activebackground='gray15', bd=0) \
            .grid(columnspan=1, column=1, row=3, pady=20, padx=4)
        Button(self.frame_dos, command=self.pantalla_diabetes, image=self.imagen_diabetes, bg='gray15',
               activebackground='gray15', bd=0) \
            .grid(columnspan=1, column=0, row=4, pady=50, padx=4)
        Button(self.frame_dos, command=self.pantalla_vino, image=self.imagen_vino, bg='gray15',
               activebackground='gray15', bd=0) \
            .grid(columnspan=1, column=1, row=4, pady=50, padx=4)

    def graficar1(self):
        if self.combobox.get() in list(CSV.keys()):
            archivo = self.combobox.get()
            df = pd.read_csv(CSV[archivo])

            if CSV[archivo] == "iris.csv": diccionario = Iris
            if CSV[archivo] == "data.csv": diccionario = Cancer
            if CSV[archivo] == "WineQT.csv": diccionario = Vino
            if CSV[archivo] == "diabetes.csv": diccionario = Diabetes

            grafica = self.grafica_type.get()

            self.pantalla_graficar1()

            if grafica == "Dispersion":
                Label(self.frame_graficar2, text=(self.combobox.get()), fg='DeepSkyBlue3', bg='gray15',
                      font=('Verdana', 25)).grid(columnspan=2, column=0, row=0, pady=10)

                Label(self.frame_graficar2, text='Colorificar', fg='gray80', bg='gray15',
                      font=('Verdana', 12)).grid(columnspan=2, column=0, row=2, pady=10)
                ttk.Combobox(self.frame_graficar2, textvariable=self.colorificar, values=list(diccionario.keys()),
                             font=('Verdana', 12)).grid(columnspan=2, column=0, row=3, pady=15, padx=5)

                Label(self.frame_graficar2, text='Eje x', fg='gray80', bg='gray15',
                      font=('Verdana', 12)).grid(columnspan=2, column=0, row=5, pady=10)
                ttk.Combobox(self.frame_graficar2, textvariable=self.ejex, values=list(diccionario.keys()),
                             font=('Verdana', 12)).grid(columnspan=2, column=0, row=7, pady=15, padx=5)

                Label(self.frame_graficar2, text='Eje y', fg='gray80', bg='gray15',
                      font=('Verdana', 12)).grid(columnspan=2, column=0, row=9, pady=10)
                ttk.Combobox(self.frame_graficar2, textvariable=self.ejey, values=list(diccionario.keys()),
                             font=('Verdana', 12)).grid(columnspan=2, column=0, row=10, pady=15, padx=5)

            elif grafica in ListaGraf:
                Label(self.frame_graficar2, text=(self.combobox.get()), fg='DeepSkyBlue3', bg='gray15',
                      font=('Verdana', 25)).grid(columnspan=2, column=0, row=0, pady=10)

                Label(self.frame_graficar2, text='Colorificar', fg='gray80', bg='gray15',
                      font=('Verdana', 12)).grid(columnspan=2, column=0, row=2, pady=10)
                ttk.Combobox(self.frame_graficar2, textvariable=self.colorificar, values=list(diccionario.keys()),
                             font=('Verdana', 12)).grid(columnspan=2, column=0, row=3, pady=15, padx=5)

                Label(self.frame_graficar2, text='Valor', fg='gray80', bg='gray15',
                      font=('Verdana', 12)).grid(columnspan=2, column=0, row=5, pady=10)
                ttk.Combobox(self.frame_graficar2, textvariable=self.valor, values=list(diccionario.keys()),
                             font=('Verdana', 12)).grid(columnspan=2, column=0, row=7, pady=15, padx=5)

    def graficar2(self):

        self.pantalla_graficar2()

        archivo = self.combobox.get()
        df = pd.read_csv(CSV[archivo])

        if CSV[archivo] == "iris.csv": diccionario = Iris
        if CSV[archivo] == "data.csv": diccionario = Cancer
        if CSV[archivo] == "WineQT.csv": diccionario = Vino
        if CSV[archivo] == "diabetes.csv": diccionario = Diabetes

        grafica = self.grafica_type.get()

        if grafica == "Dispersion":
            color = self.colorificar.get()
            ejex = self.ejex.get()
            ejey = self.ejey.get()
            sns.scatterplot(x=diccionario[ejex], y=diccionario[ejey], hue=diccionario[color], data=df)
            plt.savefig('plot.png')

        elif grafica == "De Barras Contadora":
            valor = self.valor.get()
            sns.countplot(x=diccionario[valor], data=df)
            plt.savefig('plot.png')

        elif grafica == "Histograma":
            valor = self.valor.get()
            fig, axes = plt.subplots(1, 1, figsize=(6, 6))
            b = round(1 + np.log2(150))
            axes.set_title("Grafica")
            axes.hist(df[diccionario[valor]], bins=b)
            plt.savefig('plot.png')

        elif grafica == "Histogramas con graficas de distribucion":
            valor = self.valor.get()
            color = self.colorificar.get()
            plot = sns.FacetGrid(df, hue=diccionario[color])
            plot.map(sns.histplot, diccionario[valor]).add_legend()
            plt.savefig('plot.png')

        self.image = Image.open("plot.png")
        self.resize_image = self.image.resize((400, 250))
        self.img = ImageTk.PhotoImage(self.resize_image)

        Label(self.frame_graficar3, text=(self.combobox.get()), bg='gray15', fg='DeepSkyBlue3',
              font=('Verdana', 30)).grid(columnspan=2, column=0, row=2, pady=15, padx=5)

        Label(self.frame_graficar3, image=self.img, bg='gray15').grid(columnspan=2, column=0, row=4, pady=15, padx=5)

        os.remove('plot.png')


if __name__ == "__main__":
    ventana = Tk()
    ventana.title('')
    ventana.minsize(height=570, width=700)
    ventana.geometry('700x570+180+80')
    ventana.maxsize(height=570, width=700)
    ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logscreanv2.png'))
    app = Ventana(ventana)
    app.mainloop()

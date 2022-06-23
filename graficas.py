# -- coding: utf-8 --
"""
Created on Mon Jun 20 20:35:58 2022

@author: ACER PC
"""

from tkinter import *
from tkinter import ttk
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
    "Calidad": "quality",
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


def main():
    window = Tk()
    window.title("Graficadora")
    window.geometry("300x500")
    lbltitulo = Label(window, text="Graficadora", font=("Times", 40))
    lbltitulo.place(x=35, y=0)
    lblcsv = Label(window, text="Elige la Base de datos", font=("Times", 10))
    lblcsv.place(x=70, y=100)
    comboboxcsv = ttk.Combobox(window, values=list(CSV.keys()))
    comboboxcsv.place(x=70, y=120)
    lblgrafica = Label(window, text="¿Que tipo de grafica quieres hacer?")
    lblgrafica.place(x=70, y=150)
    comboboxgrafica = ttk.Combobox(window, values=ListaGraf)
    comboboxgrafica.place(x=70, y=170)

    def graficar():
        if comboboxcsv.get() in list(CSV.keys()):
            archivo = comboboxcsv.get()
            df = pd.read_csv(CSV[archivo])

            if CSV[archivo] == "iris.csv": diccionario = Iris
            if CSV[archivo] == "data.csv": diccionario = Cancer
            if CSV[archivo] == "WineQT.csv": diccionario = Vino
            if CSV[archivo] == "diabetes.csv": diccionario = Diabetes

            graficadora = Tk()
            graficadora.title("Graficar")
            graficadora.geometry("500x500")
            lblgraficar = Label(graficadora, text="Graficadora", font=("Times", 40))
            lblgraficar.place(x=120, y=0)
            grafica = comboboxgrafica.get()
            if grafica == "Dispersion":
                lblcolorificar = Label(graficadora, text="Colorificar", font=("Times", 10))
                lblcolorificar.place(x=170, y=100)
                comboboxcolor = ttk.Combobox(graficadora, values=list(diccionario.keys()))
                comboboxcolor.place(x=170, y=120)
                lblejex = Label(graficadora, text="Eje X", font=("Times", 10))
                lblejex.place(x=170, y=160)
                comboboxejex = ttk.Combobox(graficadora, values=list(diccionario.keys()))
                comboboxejex.place(x=170, y=180)
                lblejey = Label(graficadora, text="Eje Y", font=("Times", 10))
                lblejey.place(x=170, y=210)
                comboboxejey = ttk.Combobox(graficadora, values=list(diccionario.keys()))
                comboboxejey.place(x=170, y=230)
            elif grafica in ListaGraf:
                lblcolorificar = Label(graficadora, text="Colorificar", font=("Times", 10))
                lblcolorificar.place(x=170, y=100)
                comboboxcolor = ttk.Combobox(graficadora, values=list(diccionario.keys()), validate="focusout")
                comboboxcolor.place(x=170, y=120)
                lblvalor = Label(graficadora, text="Valor", font=("Times", 10))
                lblvalor.place(x=170, y=160)
                combobovalor = ttk.Combobox(graficadora, values=list(diccionario.keys()))
                combobovalor.place(x=170, y=180)

            def grafico():
                if grafica == "Dispersion":
                    Color = comboboxcolor.get()
                    Ejex = comboboxejex.get()
                    Ejey = comboboxejey.get()
                    sns.scatterplot(x=diccionario[Ejex], y=diccionario[Ejey], hue=diccionario[Color], data=df)
                    plt.savefig('plot.png')

                elif grafica == "De Barras Contadora":
                    Valor = combobovalor.get()
                    sns.countplot(x=diccionario[Valor], data=df)
                    plt.savefig('plot.png')
                elif grafica == "Histograma":
                    Valor = combobovalor.get()
                    fig, axes = plt.subplots(1, 1, figsize=(6, 6))
                    b = round(1 + np.log2(150))
                    axes.set_title("Grafica")
                    axes.hist(df[diccionario[Valor]], bins=b)
                    plt.savefig('plot.png')

                elif grafica == "Histogramas con graficas de distribucion":

                    Valor = combobovalor.get()
                    Color = comboboxcolor.get()
                    plot = sns.FacetGrid(df, hue=diccionario[Color])
                    plot.map(sns.histplot, diccionario[Valor]).add_legend()
                    plt.savefig('plot.png')

                plot = Toplevel()
                plot.title('Plot')
                plot.geometry("500x350")
                image = Image.open("plot.png")
                resize_image = image.resize((500, 350))
                img = ImageTk.PhotoImage(resize_image)
                sel_img = Label(plot, image=img, bg="black")
                sel_img.image = img
                sel_img.pack()
                os.remove('plot.png')
                plot.mainloop()

            btngrafica = Button(graficadora, text="Graficar", command=grafico)
            btngrafica.place(x=210, y=270)

            graficadora.mainloop()

    btngraficar = Button(window, text="Graficar", command=graficar)
    btngraficar.place(x=90, y=250)

    def informacion():
        info = Tk()
        info.title("Informacion")
        info.geometry("300x400")
        lbltitulo = Label(info, text="Informacion", font=("Times", 40))
        lbltitulo.place(x=40, y=0)

        def que_es_analisis():
            anal = Tk()
            anal.title("¿Qué es el Analisis de Datos")
            anal.geometry("300x400")

            anal.mainloop()

        info.mainloop()

    window.mainloop()


if __name__ == "__main__":
    main()
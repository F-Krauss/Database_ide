
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

def dispersion(color,ejex,ejey,diccionario,df):
    sns.scatterplot(x=diccionario[ejex], y=diccionario[ejey], hue=diccionario[color], data=df)
    plt.savefig('plot.png')
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import os

carpeta_recursos = os.path.join(os.path.dirname(__file__), 'audiovisual')
frame = tk.Tk()
frame.title("Punto de Equilibrio")
frame.state('zoomed')
frame.resizable(False, 1)
frame.geometry("100x100")
frame.iconbitmap(os.path.join(carpeta_recursos, 'logo.ico'))

def puntoequi(preven, costouni, gasfig):
    return gasfig / (preven - costouni)

def puntoPlatita(resulta, preven):
    return resulta * preven

def opetabla(resulta):
    porcentage = resulta * 0.25
    return porcentage

def tablita(gasfig, resulta, porcentage, preven, costouni):
    cantidades = [resulta - porcentage, resulta, resulta + porcentage]
    ventas = [u * preven for u in cantidades]
    variables = [u * costouni for u in cantidades]
    margen = [ventas[i] - variables[i] for i in range(len(cantidades))]
    util = [margen[i] - gasfig for i in range(len(cantidades))]
    
    tree = ttk.Treeview(frame, columns=("Blank", "25PorMenos", "Punto", "25PorMas"), show="headings", height=6)
    tree.heading("Blank", text="")
    tree.heading("25PorMenos", text="25% menos de produccion")
    tree.heading("Punto", text="Punto de equilibrio")
    tree.heading("25PorMas", text="25% mas de produccion")
    tree.column("Blank", width=150)
    tree.column("25PorMenos", width=150)
    tree.column("Punto", width=150)
    tree.column("25PorMas", width=150)

    # Insertar datos de la tabla
    tree.insert("", "end", values=("Numero de unidades", *cantidades))
    tree.insert("", "end", values=("Ingreso por ventas", *ventas))
    tree.insert("", "end", values=("Costos variables", *variables))
    tree.insert("", "end", values=("Costos fijos", *[gasfig]*3))
    tree.insert("", "end", values=("Margen de contribucion", *margen))
    tree.insert("", "end", values=("Utilidad", *util))
    tree.place(relx = 0.5, rely = 0.1) 
    
def graficar(preven, costouni, gasfig, resulta):
    cantidadesRango = np.arange(0, resulta * 2, 1)
    
    ventasT = cantidadesRango * preven
    costosV = cantidadesRango * costouni
    costosT = costosV + gasfig
    costosF = np.ones_like(cantidadesRango) * gasfig
    
    fig, ax = plt.subplots(figsize=(8, 3.8))
    
    ax.plot(cantidadesRango, ventasT, label="Ventas Totales", color="blue")
    ax.plot(cantidadesRango, costosT, label="Costos Totales", color="red")
    ax.plot(cantidadesRango, costosV, label="Costos Variables", color="orange")
    ax.plot(cantidadesRango, costosF, label="Costos Fijos", color="green")
    ax.axvline(resulta, color="purple", linestyle="--", label=f"Punto de Equilibrio: {resulta} unidades")
    
    ax.set_xlabel("Unidades Vendidas")
    ax.set_ylabel("Quetzales")
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,.0f}".format(x)))
    ax.legend()
    
    for text in ax.texts:
        if "ie6" in text.get_text():
            text.set_visible(False)
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().place(relx = 0.1, rely = 0.4)

def calcular():
    try:
        preven = float(entrapre.get())
        costouni = float(entracostuni.get())
        gasfig = float(entragasfig.get())
    
        resulta = puntoequi(preven, costouni, gasfig)
        result.config(text= f"Para Alcanzar el punto de equilibrio deberia vender {resulta} unidades")
        
        resultPlati = puntoPlatita(resulta, preven)
        resultadoPlati.config(text= f"La empresa tendria que vender Q{resultPlati} para estar en su punto de equilibrio")
        porcentage = opetabla(resulta)
        tablita(gasfig, resulta, porcentage, preven, costouni)
        graficar(preven, costouni, gasfig, resulta)
        
    except ValueError:
        messagebox.showerror("", "El valor introducido no es valido, Introduce Por favor un Numero")
        return   
    
hola = tk.Label(frame, text="Punto de equilibrio", font=("Times New Roman", 20))
hola.place(relx=0.42, rely=0.002)

integrantes = tk.Label(frame, text="Integrantes:", font=("Times New Roman", 10))
integrantes.grid(row=1, column=0, padx=0, pady=5, sticky="w")

integrante1 = tk.Label(frame, text="José Miguel Castillo Pérez 0907-24-1862", font=("Times New Roman", 10))
integrante1.grid(row=1, column=1, padx=0, pady=5, sticky="w")

integrante2 = tk.Label(frame, text="Miguel Jose Alfaro Vásquez ", font=("Times New Roman", 10))
integrante2.grid(row=2, column=1, padx=0, pady=5, sticky="w")

hola2 = tk.Label(frame, text="", font=("Times New Roman", 20))
hola2.grid(row=2, column=0, padx=10, pady=5, sticky="w")

prevenl = tk.Label(frame, text="Precio de Venta: ", font=("Times New Roman", 10))
prevenl.grid(row=3, column=0, padx=10, pady=5, sticky="w")

entrapre = tk.Entry(frame, font=("Times New Roman", 10), width=20)
entrapre.grid(row=3, column=1, padx=10, pady=5, sticky="w")

cosunil = tk.Label(frame, text="Costo por Unidad: ", font=("Times New Roman", 10))
cosunil.grid(row=4, column=0, padx=10, pady=5, sticky="w")

entracostuni = tk.Entry(frame, font=("Times New Roman", 10), width=20)
entracostuni.grid(row=4, column=1, padx=10, pady=5, sticky="w")

gasfigl = tk.Label(frame, text="Gasto fijo: ", font=("Times New Roman", 10))
gasfigl.grid(row=5, column=0, padx=10, pady=5, sticky="w")

entragasfig = tk.Entry(frame, font=("Times New Roman", 10), width=20)
entragasfig.grid(row=5, column=1, padx=10, pady=5, sticky="w")

btncalc = tk.Button(frame, command=calcular, text="Calcular", font=("Times New Roman", 10) )
btncalc.grid(row=7, column=1, columnspan=3, pady=5, sticky="w")

result = tk.Label(frame, text="", font=("Times New Roman", 10)) #muestra los resultados de las operaciones
result.grid(row=8, column=1, padx=5, pady=5, sticky="w")

resultadoPlati = tk.Label(frame, text="", font=("Times New Roman", 10)) #muestra la cantidad de quetzales que se tienen que vender
resultadoPlati.grid(row=9, column=1, padx=5, pady=5, sticky="w")


frame.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

frame = tk.Tk()
frame.title("Punto de Equilibrio")
frame.geometry("1000x1000")

def puntoequi(preven, costouni, gasfig):
    return gasfig // (preven - costouni)

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
    tree.column("Blank", width=125)
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
    tree.grid(row=7, column=1, padx=10, pady=10) # jaja pack
    
def graficar(preven, costouni, gasfig, resulta):
    cantidades = np.arange(0, resulta * 2, 1)
    ventasT = cantidades * preven
    costosT = cantidades * costouni + gasfig
    
    fig, ax = plt.subplots(figsize=(5, 4))
    
    ax.plot(cantidades, ventasT, label="Ventas Totales", color="green")
    ax.plot(cantidades, costosT, label="Costos Totales", color="red")
    ax.axvline(resulta, color="blue", linestyle="--", label=f"Punto de Equilibrio: {resulta} unidades")
    
    ax.set_xlabel("Unidades Vendidas")
    ax.set_ylabel("Quetzales")
    ax.legend()
    ax.set_title("Gráfica del Punto de Equilibrio")
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=8, column=1, padx=10, pady=10)

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

prevenl = tk.Label(frame, text="Precio de Venta: ", font=("Times New Roman", 10))
prevenl.grid(row=1, column=0, padx=10, pady=10)

entrapre = tk.Entry(frame, font=("Times New Roman", 10), width=50)
entrapre.grid(row=1, column=1, padx=10, pady=10)

cosunil = tk.Label(frame, text="Costo por Unidad: ", font=("Times New Roman", 10))
cosunil.grid(row=2, column=0, padx=10, pady=10)

entracostuni = tk.Entry(frame, font=("Times New Roman", 10), width=50)
entracostuni.grid(row=2, column=1, padx=10, pady=10)

gasfigl = tk.Label(frame, text="Gasto fijo: ", font=("Times New Roman", 10))
gasfigl.grid(row=3, column=0, padx=10, pady=10)

entragasfig = tk.Entry(frame, font=("Times New Roman", 10), width=50)
entragasfig.grid(row=3, column=1, padx=10, pady=10)

btncalc = tk.Button(frame, command=calcular, text="Calcular", font=("Times New Roman", 10) )
btncalc.grid(row=5, column=1, columnspan=2, pady=10)

result = tk.Label(frame, text="", font=("Times New Roman", 10)) #muestra los resultados de las operaciones
result.grid(row=6, column=1, padx=10, pady=10)

resultadoPlati = tk.Label(frame, text="", font=("Times New Roman", 10)) #muestra la cantidad de quetzales que se tienen que vender
resultadoPlati.grid(row=6, column=1, padx=10, pady=10)


frame.mainloop()
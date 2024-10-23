import tkinter as tk
from tkinter import messagebox
import matplotlib as mt
from tkinter import ttk

frame = tk.Tk()
frame.title("Punto de Equilibrio")
frame.geometry("1000x500")

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
    tree.pack(padx=10, pady=50) # jaja pack

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
        
    except ValueError:
        messagebox.showerror("", "El valor introducido no es valido, Introduce Por favor un Numero")
        return   

prevenl = tk.Label(frame, text="Precio de Venta: ", font=("Times New Roman", 10))
prevenl.pack()
cosunil = tk.Label(frame, text="Costo por Unidad: ", font=("Times New Roman", 10))
cosunil.pack()
gasfigl = tk.Label(frame, text="Gasto fijo: ", font=("Times New Roman", 10))
gasfigl.pack()
entrapre = tk.Entry(frame, font=("Times New Roman", 10), width=50)
entrapre.pack()
entracostuni = tk.Entry(frame, font=("Times New Roman", 10), width=50)
entracostuni.pack()
entragasfig = tk.Entry(frame, font=("Times New Roman", 10), width=50)
entragasfig.pack()
btncalc = tk.Button(frame, command=calcular, text="Calcular", font=("Times New Roman", 10) )
btncalc.pack()
result = tk.Label(frame, text="", font=("Times New Roman", 10)) #muestra los resultados de las operaciones
result.pack()
resultadoPlati = tk.Label(frame, text="", font=("Times New Roman", 10)) #muestra la cantidad de quetzales que se tienen que vender
resultadoPlati.pack()

frame.mainloop()
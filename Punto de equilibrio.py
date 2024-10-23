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

def calcular():
    try:
        preven = float(entrapre.get())
        costouni = float(entracostuni.get())
        gasfig = float(entragasfig.get())
    
        resulta = puntoequi(preven, costouni, gasfig)
        result.config(text= f"Para Alcanzar el punto de equilibrio deberia vender {resulta} unidades")
        
        resultPlati = puntoPlatita(resulta, preven)
        resultadoPlati.config(text= f"La empresa tendria que vender Q{resultPlati} para estar en su punto de equilibrio")
        
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

tree = ttk.Treeview(frame, columns=("Blank", "25PorMenos", "Punto", "25PorMas"), show="headings", height=5)
tree.heading("Blank", text="")
tree.heading("25PorMenos", text="25% menos de produccion")
tree.heading("Punto", text="Punto de equilibrio")
tree.heading("25PorMas", text="25% mas de produccion")
tree.column("Blank", width=100)
tree.column("25PorMenos", width=250)
tree.column("Punto", width=120)
tree.column("25PorMas", width=300)

# Insertar datos en el Treeview
tree.insert("", "end", values=("Christopher Ricardo Garcia Giron", "0907-24-10087", "Líder de proyecto, Encargado de la intefaz principal"))
tree.pack(padx=10, pady=50)  # Usamos pack en lugar de grid para este caso

frame.mainloop()
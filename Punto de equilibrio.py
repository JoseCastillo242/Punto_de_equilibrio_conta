import tkinter as tk
from tkinter import messagebox
import matplotlib as mt

frame = tk.Tk()
frame.title("Punto de Equilibrio")
frame.geometry("1000x500")

def puntoequi(preven, costouni, gasfig):
    return gasfig // (preven - costouni)

def calcular():
    try:
        preven = float(entrapre.get())
        costouni = float(entracostuni.get())
        gasfig = float(entragasfig.get())
    
        resulta = puntoequi(preven, costouni, gasfig)
        result.config(text= f"Para Alcanzar el punto de equilibrio deberia vender {resulta} unidades")
    
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
frame.mainloop()
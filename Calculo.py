import tkinter as tk
from tkinter import messagebox

class RobotAspirador:
    def __init__(self, velocidad_limite=1.0, rendimiento=0.5):
        self.velocidad_limite = velocidad_limite  # en m/s
        self.rendimiento = rendimiento  # en m^2/s

    def calcular_superficie(self, largo, ancho):
        return largo * ancho  # Área de la habitación en metros cuadrados

    def estimar_tiempo_limpieza(self, area_habitacion):
        tiempo = area_habitacion / self.rendimiento
        return tiempo / self.velocidad_limite

def calcular_y_mostrar_resultados():
    try:
        largo = float(entry_largo.get())
        ancho = float(entry_ancho.get())
        
        # Calcular la superficie de la habitación
        area = mi_robot.calcular_superficie(largo, ancho)
        texto_resultado = f"Superficie de la habitación: {area:.2f} metros cuadrados\n"

        # Estimar el tiempo de limpieza
        tiempo_limpieza = mi_robot.estimar_tiempo_limpieza(area)
        texto_resultado += f"Tiempo estimado de limpieza: {tiempo_limpieza:.2f} segundos"

        messagebox.showinfo("Resultados", texto_resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos para el largo y el ancho.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Superficie y Tiempo de Limpieza")

# Crear un objeto RobotAspirador
mi_robot = RobotAspirador()

# Crear y colocar los widgets en la ventana
frame = tk.Frame(root)
frame.pack(padx=20, pady=10)

label_largo = tk.Label(frame, text="Largo de la habitación (metros):")
label_largo.grid(row=0, column=0, padx=5, pady=5, sticky="e")

entry_largo = tk.Entry(frame)
entry_largo.grid(row=0, column=1, padx=5, pady=5)

label_ancho = tk.Label(frame, text="Ancho de la habitación (metros):")
label_ancho.grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_ancho = tk.Entry(frame)
entry_ancho.grid(row=1, column=1, padx=5, pady=5)

boton_calcular = tk.Button(frame, text="Calcular", command=calcular_y_mostrar_resultados)
boton_calcular.grid(row=2, columnspan=2, padx=5, pady=10)

# Ejecutar la aplicación
root.mainloop()

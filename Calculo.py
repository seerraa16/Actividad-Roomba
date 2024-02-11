import tkinter as tk
from tkinter import messagebox

class RobotAspirador:
    def __init__(self, velocidad_limite=1.0, rendimiento=0.5):
        self.velocidad_limite = velocidad_limite  # en m/s
        self.rendimiento = rendimiento  # en m^2/s

    def calcular_superficie(self, largo, ancho):
        return largo * ancho  # Área de la habitación en metros cuadrados

    def estimar_tiempo_limpieza(self, area_habitacion, area_obstaculo):
        tiempo = (area_habitacion - area_obstaculo) / self.rendimiento
        return tiempo / self.velocidad_limite

def calcular_y_mostrar_resultados():
    try:
        largo = float(entry_largo.get())
        ancho = float(entry_ancho.get())
        largo_obstaculo = float(entry_largo_obstaculo.get())
        ancho_obstaculo = float(entry_ancho_obstaculo.get())
        
        # Calcular la superficie de la habitación
        area_habitacion = mi_robot.calcular_superficie(largo, ancho)
        area_obstaculo = mi_robot.calcular_superficie(largo_obstaculo, ancho_obstaculo)
        
        # Estimar el tiempo de limpieza
        tiempo_limpieza = mi_robot.estimar_tiempo_limpieza(area_habitacion, area_obstaculo)
        
        texto_resultado = f"Superficie de la habitación: {area_habitacion:.2f} metros cuadrados\n"
        texto_resultado += f"Tamaño del obstáculo: {area_obstaculo:.2f} metros cuadrados\n"
        texto_resultado += f"Tiempo estimado de limpieza: {tiempo_limpieza:.2f} segundos"

        messagebox.showinfo("Resultados", texto_resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos para las dimensiones.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Superficie y Tiempo de Limpieza")

# Crear un objeto RobotAspirador
mi_robot = RobotAspirador()

# Crear y colocar los widgets en la ventana
frame = tk.Frame(root)
frame.pack(padx=20, pady=10)

label_largo = tk.Label(frame, text="Largo de la habitación:")
label_largo.grid(row=0, column=0, padx=5, pady=5, sticky="e")

entry_largo = tk.Entry(frame)
entry_largo.grid(row=0, column=1, padx=5, pady=5)

label_ancho = tk.Label(frame, text="Ancho de la habitación:")
label_ancho.grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_ancho = tk.Entry(frame)
entry_ancho.grid(row=1, column=1, padx=5, pady=5)

label_largo_obstaculo = tk.Label(frame, text="Largo del obstáculo donde no se puede limpiar:")
label_largo_obstaculo.grid(row=2, column=0, padx=5, pady=5, sticky="e")

entry_largo_obstaculo = tk.Entry(frame)
entry_largo_obstaculo.grid(row=2, column=1, padx=5, pady=5)

label_ancho_obstaculo = tk.Label(frame, text="Ancho del obstáculo donde no se puede limpiar:")
label_ancho_obstaculo.grid(row=3, column=0, padx=5, pady=5, sticky="e")

entry_ancho_obstaculo = tk.Entry(frame)
entry_ancho_obstaculo.grid(row=3, column=1, padx=5, pady=5)

boton_calcular = tk.Button(frame, text="Calcular", command=calcular_y_mostrar_resultados)
boton_calcular.grid(row=4, columnspan=2, padx=5, pady=10)

# Ejecutar la aplicación
root.mainloop()


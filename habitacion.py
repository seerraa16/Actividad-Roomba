import tkinter as tk

root = tk.Tk()
root.title("Ejemplo de Frames")
root.geometry("580x710")

# Crear el primer frame de color azul claro
frame_azul = tk.Frame(root, width=580, height=710, bg="grey")
frame_azul.pack(fill='both', expand=True)

# Crear el segundo frame más pequeño de color amarillo
frame_amarillo = tk.Frame(root, width=560, height=690, bg="yellow")
frame_amarillo.place(relx=0.5, rely=0.5, anchor='center')
frame_amarillo_tamaño = tk.Label(frame_amarillo, text="560x690", bg="yellow")
root.mainloop()

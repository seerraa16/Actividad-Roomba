import tkinter as ttk

root = ttk.Tk()
root.title("Ejemplo de Frames")
root.geometry("580x710")

# Crear el primer frame de color azul claro
frame_azul = ttk.Frame(root, width=580, height=710, bg="grey")
frame_azul.pack(fill='both', expand=True)

# Crear el segundo frame más pequeño de color amarillo
frame_amarillo = ttk.Frame(root, width=560, height=690, bg="yellow")
frame_amarillo.place(relx=0.5, rely=0.5, anchor='center')
frame_amarillo_tamaño = ttk.Label(frame_azul, text="560x690", bg="black")

# crear zona 1, que esta a 30 pixeles de arriba y 30 pixeles de la izquierda
frame_zona1 = ttk.Frame(root, width=500, height=150, bg="red")
frame_zona1.place(x=30, y=30)
frame_zona1_tamaño = ttk.Label(frame_amarillo, text="500x150", bg="red")

#crear zona 2
frame_zona2 =ttk.Frame(root, width=630, height=101, bg="green")
frame_zona2.place(x=30, y=180)
frame_zona2_tamaño = ttk.Label(frame_zona1, text="630x101", bg="green")

#crear zona 3 
frame_zone3 = ttk.Frame(root, width=309, height=630, bg="blue")
frame_zone3.place(x=30, y=291)
frame_zone3_tamaño = ttk.Label(frame_zona2, text="309x630", bg="blue")

#crear zona 4
frame_zone4 = ttk.Frame(root, width=309, height=630, bg="purple")
frame_zone4.place(x=221, y=180)
frame_zone4_tamaño = ttk.Label(frame_zone3, text="309x630", bg="purple")
root.mainloop()

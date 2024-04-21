import tkinter as tk
from tkinter import messagebox
import random
from datetime import date

# Función para generar datos de alumnos
def generar_alumnos():
    no_registros = int(entry_no_registros.get())
    ap1 = int(entry_ap1.get())
    ap2 = int(entry_ap2.get())
    name = int(entry_name.get())

    if ap1 == 0 or ap2 == 0 or name == 0:
        messagebox.showerror("Error", "Por favor selecciona todas las opciones")
        return

    apellidos1 = []
    apellidos2 = []
    nombres = []

    # Definir los arreglos de apellidos y nombres según la selección del usuario
    if ap1 == 1:
        apellidos1 = apellidos_ruso
    elif ap1 == 2:
        apellidos1 = apellidos_espanol
    elif ap1 == 3:
        apellidos1 = apellidos_chino
    elif ap1 == 4:
        apellidos1 = apellidos_frances

    if ap2 == 1:
        apellidos2 = apellidos_ruso
    elif ap2 == 2:
        apellidos2 = apellidos_espanol
    elif ap2 == 3:
        apellidos2 = apellidos_chino
    elif ap2 == 4:
        apellidos2 = apellidos_frances

    if name == 1:
        nombres = nombres_rusos
    elif name == 2:
        nombres = nombres_espanol
    elif name == 3:
        nombres = nombres_chino
    elif name == 4:
        nombres = nombres_frances

    alumnos = []
    for i in range(no_registros):
        expediente = 222220000 + i
        apellido = random.choice(apellidos1)
        apellido2 = random.choice(apellidos2)
        nombre = random.choice(nombres)
        correo = f"a{expediente}@correo.com"
        fecha_nacimiento = date(1980 + random.randint(0, 39), random.randint(1, 12), random.randint(1, 28))
        alumnos.append((expediente, apellido, apellido2, nombre, correo, fecha_nacimiento))

    return alumnos

# Función para generar en pantalla
def generar_en_pantalla():
    registros_alumnos = generar_alumnos()
    texto_resultado.delete(1.0, tk.END)
    for alumno in registros_alumnos:
        texto_resultado.insert(tk.END, f"{alumno}\n")

# Función para guardar en archivo
def guardar_en_archivo():
    registros_alumnos = generar_alumnos()
    nombre_archivo = "alumnos.txt"
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        for alumno in registros_alumnos:
            archivo.write(f"{','.join(map(str, alumno))}\n")
    messagebox.showinfo("Guardado", f"Se han guardado los datos en {nombre_archivo}")

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Datos de Alumnos")
root.geometry("415x500")

# Arreglos de apellidos y nombres
apellidos_ruso = ["Смирнов", "Иванов", "Кузнецов", "Попов", "Васильев", "Петров"]
apellidos_espanol = ["García", "González", "Rodríguez", "Fernández", "López", "Martínez"]
apellidos_chino = ["李", "王", "张", "刘", "陈", "杨"]
apellidos_frances = ["Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard"]

nombres_rusos = ["Александр", "Михаил", "Иван", "Дмитрий", "Андрей", "Сергей"]
nombres_espanol = ["Sofía", "Lucía", "Martina", "María", "Paula", "Julia"]
nombres_chino = ["王", "李", "张", "刘", "陈", "杨"]
nombres_frances = ["Léa", "Manon", "Chloé", "Emma", "Inès", "Jade"]

# Campos de entrada
tk.Label(root, text="Número de Registros:").grid(row=0, column=0, padx=5, pady=5)
entry_no_registros = tk.Entry(root)
entry_no_registros.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Apellido 1:").grid(row=1, column=0, padx=5, pady=5)
entry_ap1 = tk.Entry(root)
entry_ap1.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Apellido 2:").grid(row=2, column=0, padx=5, pady=5)
entry_ap2 = tk.Entry(root)
entry_ap2.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Nombre:").grid(row=3, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=3, column=1, padx=5, pady=5)

# Botones
tk.Button(root, text="Generar en pantalla", command=generar_en_pantalla).grid(row=4, column=0, columnspan=2, padx=5, pady=5)
tk.Button(root, text="Guardar en archivo", command=guardar_en_archivo).grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Área de texto
texto_resultado = tk.Text(root, height=10, width=50)
texto_resultado.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Ajustar el tamaño de la ventana
root.resizable(False, False)

# Centrar la ventana
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")


# Crear las etiquetas con información estática
etiqueta_instrucciones = tk.Label(root, text="1: Ruso, 2: Español, 3: Chino, 4: Francés")
etiqueta_instrucciones.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# Ejecutar la ventana
root.mainloop()

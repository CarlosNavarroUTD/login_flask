import tkinter as tk
from tkinter import messagebox
from app.usuarios.models import Usuario
import hashlib

def encriptar_contraseña(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Función para mostrar el formulario de registro
def mostrar_registro():
    login_window.withdraw()
    registro_window.deiconify()

# Función para mostrar el formulario de inicio de sesión
def mostrar_login():
    registro_window.withdraw()
    login_window.deiconify()

# Función de inicio de sesión
def login():
    email = entry_email.get()
    password = entry_password.get()
    password_encriptada = encriptar_contraseña(password)

    usuario = Usuario.get_by_email(email)
    if usuario and usuario[4] == password_encriptada:  # Indice 4 es el campo password
        messagebox.showinfo("Inicio de sesión", f"Bienvenido, {usuario[1]}!")
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")

# Función de registro
def registrar():
    nombre = entry_nuevo_nombre.get()
    apellidos = entry_nuevo_apellidos.get()
    email = entry_nuevo_email.get()
    password = entry_nuevo_password.get()
    confirmar_password = entry_confirmar_password.get()

    if password != confirmar_password:
        messagebox.showerror("Error", "Las contraseñas no coinciden")
        return

    password_encriptada = encriptar_contraseña(password)
    nuevo_usuario = Usuario(nombre=nombre, apellidos=apellidos, email=email, password=password_encriptada)
    nuevo_usuario.create()
    messagebox.showinfo("Registro", "Usuario registrado con éxito")
    mostrar_login()

# Ventana de inicio de sesión
login_window = tk.Tk()
login_window.title("Inicio de Sesión")

tk.Label(login_window, text="Email").pack(pady=5)
entry_email = tk.Entry(login_window)
entry_email.pack(pady=5)

tk.Label(login_window, text="Contraseña").pack(pady=5)
entry_password = tk.Entry(login_window, show='*')
entry_password.pack(pady=5)

tk.Button(login_window, text="Iniciar Sesión", command=login).pack(pady=5)
tk.Button(login_window, text="Registrarse", command=mostrar_registro).pack(pady=5)

# Ventana de registro
registro_window = tk.Toplevel()
registro_window.title("Registrarse")
registro_window.withdraw()  # Ocultar la ventana de registro inicialmente

tk.Label(registro_window, text="Nombre").pack(pady=5)
entry_nuevo_nombre = tk.Entry(registro_window)
entry_nuevo_nombre.pack(pady=5)

tk.Label(registro_window, text="Apellidos").pack(pady=5)
entry_nuevo_apellidos = tk.Entry(registro_window)
entry_nuevo_apellidos.pack(pady=5)

tk.Label(registro_window, text="Email").pack(pady=5)
entry_nuevo_email = tk.Entry(registro_window)
entry_nuevo_email.pack(pady=5)

tk.Label(registro_window, text="Contraseña").pack(pady=5)
entry_nuevo_password = tk.Entry(registro_window, show='*')
entry_nuevo_password.pack(pady=5)

tk.Label(registro_window, text="Confirmar Contraseña").pack(pady=5)
entry_confirmar_password = tk.Entry(registro_window, show='*')
entry_confirmar_password.pack(pady=5)

tk.Button(registro_window, text="Registrar", command=registrar).pack(pady=5)
tk.Button(registro_window, text="Volver", command=mostrar_login).pack(pady=5)

# Ejecutar el bucle principal de Tkinter
login_window.mainloop()

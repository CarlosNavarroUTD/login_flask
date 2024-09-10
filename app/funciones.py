import os
import hashlib
from datetime import datetime
from flask import flash

def flash_errors(form):
    """Función para mostrar errores de formularios Flask-WTF"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"Error en el campo {getattr(form, field).label.text}: {error}", 'error')



def hash_password(password):
    """Encripta una contraseña utilizando SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def obtener_fecha_actual():
    """Devuelve la fecha actual en formato YYYY-MM-DD."""
    return datetime.now().strftime("%d-%m-%Y")

def fecha_int():
    fecha_str = obtener_fecha_actual()
    fecha_int = int(fecha_str.replace("-", ""))
    return fecha_int
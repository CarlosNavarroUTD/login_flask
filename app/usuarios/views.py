from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from .models import Usuario
from .forms import LoginForm, RegisterForm

from . import usuarios  # Importa el blueprint usuarios

@usuarios.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        contrasena = form.password.data
        usuario = Usuario.iniciar_sesion(email, contrasena)
        if usuario:
            login_user(usuario)
            return redirect(url_for('index'))
        else:
            flash('Correo electrónico o contraseña incorrectos', 'error')
    return render_template('usuarios/login.html', form=form)

@usuarios.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegisterForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellidos = form.apellidos.data
        email = form.email.data
        contrasena = form.password.data
        usuario = Usuario.registrarse(nombre, apellidos, email, contrasena)
        if usuario:
            login_user(usuario)
            return redirect(url_for('index'))
        else:
            flash('Error al registrar usuario', 'error')
    return render_template('usuarios/register.html', form=form)

@usuarios.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
from flask import Blueprint, render_template, redirect, url_for, flash, request
from .models import Nota
from .forms import CreateNotaForm
from flask_login import login_required, current_user

from . import notas  # Importa el blueprint notas

@notas.route('/')
@login_required
def index():
    try:
        form = CreateNotaForm()
        notas_usuario = Nota.get_by_usuario_id(current_user.id)
        return render_template('notas/notas.html', form=form, notas=notas_usuario)
    except Exception as e:
        flash(f"Error en la página de inicio: {str(e)}", 'error')
        return redirect(url_for('notas.index'))

@notas.route('/create', methods=['POST'])
@login_required
def create():
    try:
        form = CreateNotaForm()
        if form.validate_on_submit():
            nueva_nota = Nota(
                usuario_id=current_user.id,
                titulo=form.titulo.data,
                descripcion=form.descripcion.data
            )
            nueva_nota.create()
            flash('Nota creada exitosamente', 'success')
            return redirect(url_for('notas.index'))
        else:
            flash("Error en la creación de la nota", 'error')
            return render_template('notas/notas.html', form=form)
    except Exception as e:
        flash(f"Error al crear la nota: {str(e)}", 'error')
        return redirect(url_for('notas.index'))

@notas.route('/edit/<int:nota_id>', methods=['GET', 'POST'])
@login_required
def edit(nota_id):
    try:
        nota = Nota(id=nota_id)
        nota.read()
        if nota.usuario_id != current_user.id:
            flash('No tienes permiso para editar esta nota', 'error')
            return redirect(url_for('notas.index'))
        
        form = CreateNotaForm(obj=nota)
        if form.validate_on_submit():
            nota.titulo = form.titulo.data
            nota.descripcion = form.descripcion.data
            nota.update()
            flash('Nota actualizada exitosamente', 'success')
            return redirect(url_for('notas.index'))
        else:
            flash("Error en la edición de la nota", 'error')
            return render_template('notas/edit.html', form=form, nota=nota)
    except Exception as e:
        flash(f"Error al editar la nota: {str(e)}", 'error')
        return redirect(url_for('notas.index'))

@notas.route('/delete/<int:nota_id>', methods=['POST'])
@login_required
def delete(nota_id):
    try:
        nota = Nota(id=nota_id)
        nota.read()
        if nota.usuario_id != current_user.id:
            flash('No tienes permiso para eliminar esta nota', 'error')
        else:
            nota.delete()
            flash('Nota eliminada exitosamente', 'success')
        return redirect(url_for('notas.index'))
    except Exception as e:
        flash(f"Error al eliminar la nota: {str(e)}", 'error')
        return redirect(url_for('notas.index'))
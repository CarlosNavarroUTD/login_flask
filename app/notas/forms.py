from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class CreateNotaForm(FlaskForm):
    usuario_id = IntegerField('Usuario ID', validators=[DataRequired()])
    titulo = StringField('Título', validators=[DataRequired(), Length(min=5, max=50)])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Guardar')
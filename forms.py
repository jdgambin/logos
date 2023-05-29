"""Para manejar los formularios web de la aplicación."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired

class ArgInitial(FlaskForm):
    """Clase para representar el formulario web 'Metadatos del argumento'."""
    vars = StringField('Variables proposicionales', validators=[DataRequired()])
    nprems = StringField('Número total de premisas', validators=[DataRequired()])
    submit = SubmitField('Continuar')

class ArgDerivation(FlaskForm):
    """Clase para representar el formulario web 'Verificar inferencia'."""
    prop = StringField('Conclusión', validators=[DataRequired()])
    refs = StringField('Referencias', validators=[DataRequired()])
    reginf = StringField('Regla de inferencia')
    submit = SubmitField('Verificar')

class PremiseEntry(FlaskForm):
    """Clase para representar el campo de texto 'Premisa #'."""
    prop = StringField('', validators=[DataRequired()])

class PremisesForm(FlaskForm):
    """Clase para representar el formulario web 'Premisas del argumento'."""
    props = FieldList(FormField(PremiseEntry), min_entries=1)
    submit = SubmitField('Continuar')

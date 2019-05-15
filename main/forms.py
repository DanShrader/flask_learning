from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.widgets.html5 import NumberInput
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from main.models import Another


class DataEntry(FlaskForm):
    grouping = IntegerField('Grouping',widget=NumberInput(), validators=[DataRequired()])
    title = QuerySelectField(
        'Title',
        query_factory=lambda: Another.query,
        allow_blank=False
    )
    submit = SubmitField('Add Record')


class DataEntryUpdate(DataEntry):
    submit = SubmitField('Update Record')
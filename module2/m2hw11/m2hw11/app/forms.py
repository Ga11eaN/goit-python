from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    contact_name = StringField("Contact name", validators=[DataRequired()])
    phone = StringField("Phone")
    mail = StringField("E-mail")
    address = StringField("Address")
    birthday = StringField("Birthday")
    submit = SubmitField("Create")
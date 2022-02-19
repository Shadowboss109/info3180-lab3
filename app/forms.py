from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, EmailField
from wtforms.validators import DataRequired,Email

class ContactForm(FlaskForm):
    class Meta:
        csrf = True
        
    name = StringField('Name', validators=[DataRequired()])

    email = EmailField('E-mail', validators=[
                       Email(),
                       DataRequired()
                       ])

    subject = StringField('Subject', validators=[
                          DataRequired()])

    message=TextAreaField('Message', validators=[DataRequired()])
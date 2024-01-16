from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email, NumberRange


class NewCustomerForm(FlaskForm):
    id = IntegerField('Customer ID', validators=[DataRequired(), NumberRange(1, 9999, message="Not a valid ID")])
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email(message="Not a valid Email")])
    phone = IntegerField('Phone Number',
                         validators=[DataRequired(), NumberRange(1000000000, 9999999999, message="Not a valid phone "
                                                                                                 "number")])
    address = StringField('Address', validators=[DataRequired(), Length(1, 30, message="Character length should be "
                                                                                       "between 1 and 30")])
    submit = SubmitField('Add Customer')

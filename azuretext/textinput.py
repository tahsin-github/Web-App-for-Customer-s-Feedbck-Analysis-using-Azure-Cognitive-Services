from flask_wtf import FlaskForm
from wtforms import  SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError


class TextComment(FlaskForm):
    comment = TextAreaField('Comment', validators = [DataRequired(), Length(min = 2, max = 5000)])

    submit = SubmitField('Analyze Now.')


    
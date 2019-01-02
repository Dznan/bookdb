from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class SearchForm(FlaskForm):
    book_name = StringField('Book Name',
                            validators=[
                                DataRequired(message='It can\' be empty!'),
                                Length(1, 64)
                            ])
    submit = SubmitField('Search')
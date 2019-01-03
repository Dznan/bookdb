from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class SearchForm(FlaskForm):
    book_name = StringField('Book Name',
                            validators=[
                                DataRequired(message='It can\' be empty!'),
                                Length(1, 64)
                            ],
                            render_kw={'placeholder': 'Enter Book Name...'}
                            )
    submit = SubmitField('Search')


class LoginForm(FlaskForm):
    username = StringField('Username',
                            validators=[
                                DataRequired(message='Username can\'t be empty!'),
                                Length(1, 64)
                            ],
                            render_kw={'placeholder': 'Username'}
                            )
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(message='Password can\'t be empty!'),
                                 Length(1, 64)
                             ],
                             render_kw={'placeholder': 'Password'}
                             )
    login = SubmitField('Login')

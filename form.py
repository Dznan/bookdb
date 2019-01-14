from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
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

class ReviewForm(FlaskForm):
    review_content = TextAreaField('Review Content',
                            validators=[
                                DataRequired(message='It can\' be empty!'),
                                Length(1, 1000)
                            ],
                            render_kw={'placeholder': 'Enter Your Review of the Book...'}
                            )
    submit = SubmitField('Submit')

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

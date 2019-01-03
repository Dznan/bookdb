from .form import SearchForm
from .db import BookDatabase

from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'xSWEdn&v03uj0@'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/s', methods=['GET', 'POST'])
def search_front():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('search', book_name=form.book_name.data))
    return render_template('search.html', form=form)


@app.route('/search?book_name=<book_name>')
def search(book_name):
    db = BookDatabase()
    book_list = db.search_with_book_name(book_name)
    form = SearchForm()
    return render_template('search.html', form=form, book_list=book_list)


@app.route('/review')
def reviews():
    db = BookDatabase()
    review_list = db.grab_review()
    return render_template('reviews.html', review_list=review_list)



if __name__ == '__main__':
    app.run(debug=True)

import mysql.connector


class BookDatabase:
    def __init__(self):
        self.config = {
            'host': 'aliyun.duerx.host',
            'user': 'remote',
            'password': '123456',
            'db': 'book'
        }

        self.con = mysql.connector.connect(**self.config)
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()

    def search_with_book_name(self, book_name):
        query = '''
        SELECT books.book_id, title, author, author_name
        FROM books, author
        WHERE books.author = author_id AND title like '%{}%';
        '''.format(book_name)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_book_list(self,book_range):
        query = '''
        SELECT books.book_id, title, author, author_name
        FROM books, author
        WHERE books.author = author_id 
        ORDER BY books.book_id desc
        LIMIT {},{}
        '''.format(book_range,book_range+20)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_book_list_by_author_id(self, author_id):
        query = '''
        SELECT book_id, title, author, summary
        FROM books
        WHERE author = {};
        '''.format(author_id)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_book_list_by_publisher_id(self, publisher_id):
        query = '''
        SELECT book_id, title, publisher, summary
        FROM books
        WHERE publisher = {};
        '''.format(publisher_id)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_book_detail(self, book_id):
        query = '''
        SELECT title,subtitle,author,image,summary,publisher, pages, binding, rating, isbn10, isbn13, series, serie_name, price, pubdate, alt, author.author_name, publisher_name, rating.average 
        FROM books, serie, author, publisher, rating
        WHERE books.book_id = '{}' and books.series = serie.serie_id and books.author = author.author_id and books.publisher = publisher.publisher_id and rating = rating.rating_id;
        '''.format(book_id)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result


    def get_serie_list(self,serie_range):
        query = '''
        SELECT serie_id, serie_name, description, volumes
        FROM serie 
        ORDER BY serie.serie_id desc
        LIMIT {},{}
        '''.format(serie_range,serie_range+20)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_serie_detail(self, serie_id):
        query = '''
        SELECT books.title, books.book_id, serie.serie_name, author.author_id, author.author_name, serie.volumes
        FROM serie, books, author 
        where serie.serie_id = '{}' and serie.serie_id=books.series and books.author=author.author_id;
        '''.format(serie_id)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_author_list(self,author_range):
        query = '''
        SELECT author_id, author_name, author_introduction
        FROM author 
        ORDER BY author_id desc
        LIMIT {},{}
        '''.format(author_range,author_range+10)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_author_detail(self, author_id):
        query = '''
        SELECT *
        FROM author
        where author_id = '{}';
        '''.format(author_id)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_publisher_list(self,publisher_range):
        query = '''
        SELECT publisher_id, publisher_name, publisher_introduction
        FROM publisher 
        ORDER BY publisher_id desc
        LIMIT {},{}
        '''.format(publisher_range,publisher_range+20)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_publisher_detail(self, publisher_id):
        query = '''
        SELECT *
        FROM publisher
        where publisher_id = '{}';
        '''.format(publisher_id)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_reviews_by_book_id(self,book_id):
        query = '''
        SELECT user.user_name, reviews.time, content, review_likes_count.likes_num
        FROM user, reviews, review_likes_count
        WHERE reviews.book_id = '{}' and reviews.review_id = review_likes_count.reviews and reviews.reviewer_id = user.user_id
        ORDER BY reviews.time desc
        '''.format(book_id)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_reviews(self):
        query = '''
        SELECT title, content, review_likes_count.likes_num, books.book_id
        FROM books, reviews, review_likes_count
        WHERE reviews.book_id = books.book_id and reviews.review_id = review_likes_count.reviews
        ORDER BY reviews.time desc
        LIMIT 0,20;  
        '''

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_username_by_id(self, id):
        query = '''
        SELECT user_name
        FROM user
        WHERE user_id = \'{}\'
        '''.format(id)

        self.cur.execute(query)
        username,  = self.cur.fetchone()

        return username

    def get_password_by_id(self, id):
        query = '''
        SELECT password
        FROM user
        WHERE user_id = \'{}\'
        '''.format(id)

        self.cur.execute(query)
        password,  = self.cur.fetchone()

        return password

    def validate_login(self, username, password):
        query = '''
        SELECT password
        FROM user
        WHERE user_name = \'{}\'
        '''.format(username)

        self.cur.execute(query)
        result = self.cur.fetchone()

        return result[0] == password

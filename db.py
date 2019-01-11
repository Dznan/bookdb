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
        SELECT title, author_name, books.book_id
        FROM books, author
        WHERE books.author = author_id AND title like '%{}%';
        '''.format(book_name)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_book_list(self,book_range):
        query = '''
        SELECT title, author_name, books.book_id
        FROM books, author
        WHERE books.author = author_id 
        ORDER BY books.book_id desc
        LIMIT {},{}
        '''.format(book_range,book_range+20)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_book_detail(self, book_id):
        query = '''
        SELECT title,subtitle,author,image,summary,publisher, pages, binding, rating, isbn10, isbn13, series, price, pubdate, alt
        FROM books
        WHERE books.book_id = '{}';
        '''.format(book_id)

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

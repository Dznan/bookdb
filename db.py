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
        SELECT books.book_id, title, author, author_name, book_likes_count.likes_num
        FROM books, author, book_likes_count
        WHERE books.author = author_id AND title like '%{}%' AND books.book_id = book_likes_count.book_id
        '''.format(book_name)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_book_list(self,book_range):
        query = '''
        SELECT books.book_id, title, author, author_name, book_likes_count.likes_num
        FROM books, author, book_likes_count
        WHERE books.author = author_id and books.book_id = book_likes_count.book_id
        ORDER BY book_likes_count.likes_num desc
        LIMIT {},{}
        '''.format(book_range,book_range+20)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_book_list_by_author_id(self, author_id):
        query = '''
        SELECT books.book_id, title, author, summary, book_likes_count.likes_num
        FROM books, book_likes_count
        WHERE author = {} and books.book_id = book_likes_count.book_id;
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

    def get_book_list_by_like_user_id(self, user_id):
        query = '''
        SELECT books.book_id, books.title, author, author_name, book_likes_count.likes_num
        FROM book_likes, books, author, book_likes_count
        WHERE book_likes.liker_id = {} and book_likes.book_id = books.book_id and books.author = author.author_id and books.book_id = book_likes_count.book_id
        '''.format(user_id)

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
        SELECT user.user_name, reviews.time, content, review_likes_count.likes_num, user.user_id, reviews.review_id
        FROM user, reviews, review_likes_count
        WHERE reviews.book_id = '{}' and reviews.review_id = review_likes_count.reviews and reviews.reviewer_id = user.user_id
        ORDER BY reviews.time desc
        '''.format(book_id)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_reviews_by_user_id(self,user_id):
        query = '''
        SELECT books.title, reviews.time, content, review_likes_count.likes_num, books.book_id
        FROM books, reviews, review_likes_count
        WHERE reviews.reviewer_id = '{}' and books.book_id = reviews.book_id and  reviews.review_id = review_likes_count.reviews
        ORDER BY reviews.time desc
        '''.format(user_id)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def insert_reivews(self, user_id, book_id, content):
        query = '''
        INSERT INTO reviews (reviewer_id, book_id, content)
        VALUES ({}, '{}', '{}');
        '''.format(user_id, book_id, content)

        self.cur.execute(query)
        self.con.commit()
        # result = self.cur.fetchall()
        # return result

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
        
        if result == None:
            return "No Such Username"
        elif result[0] != password:
            return "Wrong Password"
        return result[0] == password

    def get_user_info_by_username(self, username):
        query = '''
        SELECT user_id, user_name, password
        FROM user
        WHERE user_name = \'{}\'
        '''.format(username)

        self.cur.execute(query)
        result = self.cur.fetchone()

        return result

    def get_user_info_by_id(self, id):
        query = '''
        SELECT user_id, user_name, password
        FROM user
        WHERE user_id = \'{}\'
        '''.format(id)

        self.cur.execute(query)
        result = self.cur.fetchone()

        return result

    def delete_review(self, review_id):
        query = '''
        DELETE FROM reviews
        WHERE review_id = {};
        '''.format(review_id)

        self.cur.execute(query)
        self.con.commit()
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
        SELECT title, author_name
        FROM books, author
        WHERE books.author = author_id AND title like '%{}%';
        '''.format(book_name)

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def grab_review(self):
        query = '''
        SELECT title, content, review_likes_count.likes_num
        FROM books, reviews, review_likes_count
        WHERE reviews.book_id = books.book_id and reviews.review_id = review_likes_count.reviews
        ORDER BY reviews.time desc
        LIMIT 0,20;  
        '''

        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def validate_login(self, username, password):
        query = '''
        SELECT password
        FROM user
        WHERE user_name = \'{}\'
        '''.format(username)

        self.cur.execute(query)
        result = self.cur.fetchone()

        return result[0] == password

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

        print(query)

        self.cur.execute(query)
        result = self.cur.fetchall()
        print(result)
        return result

'''
Module interacting with database.
Using MySQL.
'''

import pymysql


host = '192.168.114.128'
port = 3306
user = 'dev'
password = 'dev0123'
db = 'devdb'
charset = 'utf8'

like_column = ['liked_time', 'liker', 'object_type', 'liked_object']
user_column = ['id', 'username', 'nickname', 'gender', 'comment', 'register_time']
book_column = ['marc_no', 'book_name', 'author', 'publisher', 'ISBN', 'call_number']
comment_column = ['id', 'commentor', 'object_type', 'comment_object', 'comment_time', 'content']


def Connect():
    conn = pymysql.connect(
                               host = host,
                               port = port,
                               user = user,
                               password = password,
                               db = db,
                               charset = charset
                          )
    return conn

def DatabaseInit():
    conn = Connect()
    cur = conn.cursor()
    cmd_table_user = '''
                     CREATE TABLE user (
                                           id MEDIUMINT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                                           username CHAR(12),
                                           nickname CHAR(20),
                                           gender CHAR(2),
                                           comments MEDIUMINT DEFAULT 0,
                                           register_time DATETIME DEFAULT NOW()
                                       ) ENGINE=InnoDB DEFAULT CHARSET=UTF8
                     '''
    cmd_table_book = '''
                     CREATE TABLE book (
                                           marc_no INT ZEROFILL PRIMARY KEY AUTO_INCREMENT NOT NULL,
                                           bookname VARCHAR(50),
                                           author VARCHAR(50),
                                           publisher VARCHAR(50),
                                           ISBN CHAR(17),
                                           call_number VARCHAR(30)
                                       ) ENGINE=InnoDB DEFAULT CHARSET=UTF8
                     '''
    cmd_table_comment = '''
                        CREATE TABLE comment (
                                                 id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                                                 commentor MEDIUMINT,
                                                 object_type CHAR(5),
                                                 comment_object INT,
                                                 comment_time DATETIME DEFAULT NOW(),
                                                 content VARCHAR(500)
                                             ) ENGINE=InnoDB DEFAULT CHARSET=UTF8
                        '''
    cmd_table_likes = '''
                     CREATE TABLE likes (
                                           liked_time DATETIME DEFAULT NOW(),
                                           liker MEDIUMINT,
                                           object_type CHAR(5),
                                           liked_object INT
                                        ) ENGINE=InnoDB DEFAULT CHARSET=UTF8
                     '''
    cur.execute(cmd_table_user)
    cur.execute(cmd_table_book)
    cur.execute(cmd_table_comment)
    cur.execute(cmd_table_likes)
    conn.commit()
    conn.close()
    return

'''
This is area for Book Information System.
'''

def AddNewBook(info = {}):
    conn = Connect()
    cur = conn.cursor()
    cmd = 'INSERT INTO book (marc_no,bookname,author,publisher,ISBN,call_number) values (%s,%s,%s,%s,%s,%s)'
    cur.execute(cmd, (info['marc_no'], info['bookname'], info['author'], info['publisher'], info['ISBN'], info['call_number']))
    conn.commit()
    conn.close()
    return

def GetBookInfo(bookname = ''):
    conn = Connect()
    cur = conn.cursor()
    cmd = 'SELECT marc_no,bookname,author,publisher,ISBN,call_number FROM book WHERE bookname=%s'
    cur.execute(cmd, (bookname, ))
    res = cur.fetchall()
    conn.commit()
    conn.close()
    return res

def ModifyUserInfo(info = {}, bookname = ''):
    conn = Connect()
    cur = conn.cursor()
    cmd = 'UPDATE book SET'
    for i in info:
        if i in book_column:
            cmd = cmd + i + '=' + str(info[i]) + ','
    cmd = cmd[:-1] + ' WHERE bookname=%s'
    cur.execute(cmd, (bookname, ))
    conn.commit()
    conn.close()
    return

'''
This is area for User's Comment System.
'''

def AddComment():
    pass

def AddLike():
    pass

def AddReply():
    pass

def GetCommentByBook():
    pass

def GetCommentByUser():
    pass

def RemoveLike():
    pass

'''
This is area for User's Information System.
'''

def ContactUser():
    pass

def GetUserInfo():
    pass

def LoginUser():
    pass

def ModifyfUserInfo():
    pass

def RegisterUser():
    pass
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
                                           realname CHAR(10),
                                           gender CHAR(2),
                                           school CHAR(20),
                                           comments MEDIUMINT DEFAULT 0,
                                           register_time TIME DEFAULT NOW()
                                       ) ENGINE=InnoDB DEFAULT CHARSET=UTF8
                     '''
    cmd_table_book = '''
                     CREATE TABLE book (
                                           marc_no CHAR(10),
                                           bookname VARCHAR(100),
                                           author VARCHAR(60),
                                           publisher VARCHAR(40),
                                           pub_time CHAR(8),
                                           ISBN CHAR(17),
                                           call_number VARCHAR(30)
                                       ) ENGINE=InnoDB DEFAULT CHARSET=UTF8
                     '''
    cmd_table_comment = '''
                        CREATE TABLE comment (
                                                 id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                                                 username CHAR(12),
                                                 comment_time TIME DEFAULT NOW(),
                                                 replies MEDIUMINT DEFAULT 0,
                                                 likes INT DEFAULT 0, 
                                                 content VARCHAR(500)
                                             ) ENGINE=InnoDB DEFAULT CHARSET=UTF8
                        '''
    cmd_table_reply = '''
                      CREATE TABLE reply (
                                             id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                                             username CHAR(12),
                                             reply_time TIME DEFAULT NOW(),
                                             reply_to CHAR(12),
                                             comment_id INT,
                                             content VARCHAR(200)
                                         ) ENGINE=InnoDB DEFAULT CHARSET=UTF8
                      '''
    cur.execute(cmd_table_user)
    cur.execute(cmd_table_book)
    cur.execute(cmd_table_comment)
    cur.execute(cmd_table_reply)
    conn.commit()
    conn.close()
    return

def GetComment():
    pass

def GetReply():
    pass

def UserRegister():
    pass

def UserLogin():
    pass

def UserComment():
    pass

def UserReply():
    pass
import mysql.connector
from qiushibaike import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD,host=MYSQL_HOSTS,database=MYSQL_DB)
cur = cnx.cursor(buffered=True)

class Sql:
    @classmethod
    def insert_item(cls,id, name,content,agreed_number, page_number):
        sql = 'INSERT INTO article (`id`,`name`,`content`,`agreed_number`,`page_number`) VALUES (%(id)s, %(name)s, %(content)s, %(agreed_number)s, %(page_number)s)'
        value = {
            'id':id,
            'name':name,
            'content':content,
            'agreed_number':agreed_number,
            'page_number': page_number
        }
        cur.execute(sql,value)
        cnx.commit()
    #查找id,如果存在返回1，否则0
    @classmethod
    def select_id(cls, id):
        sql = 'SELECT EXISTS(SELECT 1 FROM article WHERE id=%(id)s)'
        value = {
            'id':id
        }
        cur.execute(sql,value)
        return cur.fetchall()[0]


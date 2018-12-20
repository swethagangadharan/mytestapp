import pymysql
import sqlparse
import json


class Users():
    def __init__(self):
        self.connection = pymysql.connect(host="localhost", user="root", passwd="",
                                          db="learn_python", charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    def checkUserLogin(self, username, password):
        sql = "select * from {} where `name`='{}' and `password`='{}'".format("users", username, password)
        cur = self.connection.cursor()
        # print sql
        cur.execute(sql)
        result = cur.fetchall()
        print result, "result"
        return result

    def getUsers(self):
        sql = "select * from users"
        cur = self.connection.cursor()
        cur.execute( sql )
        result = cur.fetchall()
        return result

    def getUser(self, id):
        sql = "select * from users where id = {}.".format(id)
        cur = self.connection.cursor()
        cur.execute( sql )
        result = cur.fetchone()
        return result

    def updateUser(self, data):
        sql = "update users set `name`='{}', `password` = '{}' where `id`={}".format(data['name'], data['password'], data['id'])
        print sql, " sql"
        cur = self.connection.cursor()
        cur.execute( sql )
        self.connection.commit()

    def update(self, name, id):
		sql = "update users set `name`='{}' where `id`={}".format(name, id)
		print sql
		cur = self.connection.cursor()
		cur.execute( sql )
		self.connection.commit()
    
    def insert(self,data):
        sql="insert into users (`name`,`password`) values ('{}','{}')".format(data['name'],data['password'])
        print sql
        cur=self.connection.cursor()
        cur.execute(sql)
        self.connection.commit()
    
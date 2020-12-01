from flask_restful import Resource,reqparse
import pymysql
from flask import jsonify

parser = reqparse.RequestParser()
parser.add_argument("name")
parser.add_argument("gender")
parser.add_argument("birth")
parser.add_argument("note")
class User(Resource):
    def init_db(self):
        db = pymysql.connect("localhost","root","123456","api")
        cursor = db.cursor(pymysql.cursors.DictCursor)
        return db,cursor
    def get(self,id):
        db,cursor = self.init_db()
        sql = """SELECT * FROM api.users WHERE id ={}""".format(id)
        cursor.execute(sql)
        db.commit()
        user = cursor.fetchone()
        db.close

        return jsonify(user)
    def delete(self,userid):
        db,cursor = self.init_db()
        sql = "UPDATE api.users SET deleted = 1 WHERE id ={}".format(userid)
        response = {}
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            response['meg'] = 'Success'
        except:
            response['msg'] = 'Failed'
        db.close()
        return jsonify(response)
class Users(Resource):
    def init_db(self):
        db = pymysql.connect("localhost","root","123456","api")
        cursor = db.cursor(pymysql.cursors.DictCursor)
        return db,cursor
    def get(self):
        db,cursor = self.init_db()
        sql = """SELECT * FROM api.users """
        cursor.execute(sql)
        db.commit()
        users = cursor.fetchall()
        db.close

        return jsonify(users)
    def post(self):
        db, cursor = self.init_db()
        arg = parser.parse_args()
        user = {
            'name': arg['name'],
            'gender': arg['gender'],
            'birth': arg['birth'],
            'note': arg['note'],
        }
        sql = """
            INSERT INTO `api`.`users` (`name`, `gender`, `birth`, `note`) 
            VALUES ('{}', '{}', '{}', '{}');
        """.format(user['name'],user['gender'],user['birth'],user['note'])
        response = {}
        try:
                cursor.execute(sql)
                response['meg'] = 'Success'
        except:
                response['msg'] = 'Failed'
        db.commit()
        db.close()
        return jsonify(response)
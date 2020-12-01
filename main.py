from flask import Flask
from flask_restful import Api
from resources.user import Users,User

app = Flask(__name__)
api = Api(app)

api.add_resource(Users,'/users')
api.add_resource(User,'/user/<userid>')

@app.route("/")
def hello():
    return "Hello World"

@app.route("/test")
def test():
    return "test"

@app.route("/heyhey/<userid>")
def heyhey(userid):
    return "hey hey{}".format(userid)

if __name__ == "__main__":
    app.debug=True
    app.run(debug=True, host="127.0.0.1",port=5031)
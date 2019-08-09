#-*-coding:utf-8-*-
from flask import Flask
from flask_script  import  Manager#命令行启动该APP
# from oneBluePrint.bluePrint2 import simple_blueprint2
# from oneBluePrint.bluePrint1 import simple_blueprint1
from bluePrinttwo import simple_blueprint2
from bluePrintone import simple_blueprint1
app = Flask(__name__)
app.register_blueprint(simple_blueprint2)
app.register_blueprint(simple_blueprint1)
manage=Manager(app)
if __name__ == '__main__':
    manage.run()


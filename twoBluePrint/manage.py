#-*-coding:utf-8-*-
from flask import Flask
from twoBluePrint.bluePrint2 import simple_blueprint2
from twoBluePrint.bluePrint1 import simple_blueprint1
if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(simple_blueprint2)
    app.register_blueprint(simple_blueprint1)
    app.run()

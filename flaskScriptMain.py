#-*-coding:utf-8-*-
#蓝图命令行启动，只能在命令行启动，不能在视图启动
from  flask import Flask
from flask_script  import Manager
app=Flask(__name__)
@app.route("/")
def  index():
    return "Hello world"
manage=Manager(app)#对app进行命令行序列化
@manage.command#command命令command
def  hello(name="createsuperuser"):
    #是命令行可以传递的参数，在命令行以--name来传递
    username=input("name:")
    password = input("name:")
    return "玩玩玩！"
if __name__ == '__main__':
    manage.run()#启动flask,manage,manage启动app


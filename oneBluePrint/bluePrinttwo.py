#-*-coding:utf-8-*-
"""
蓝图的官方案例，
注册多蓝图实例，
使用app的加载蓝图
"""

from flask import Blueprint,Flask
simple_blueprint2=Blueprint("simple_page2",__name__)#创建蓝图
#bluePrint的路由和视图
@simple_blueprint2.route("/index2/")
def  index():
    return "hello  world two"
#启动项目
# if __name__ == '__main__':
#     app=Flask(__name__)
#     app.register_blueprint(simple_blueprint)#注册蓝图
#     app.run()

# 导入flask
from flask import Flask

# 创建flask应用对象
app = Flask(__name__)

# 路由 + 视图函数
@app.route('/')
def hello_world():
    return 'Hello World!'

# 添加一个路由和视图函数,两边都要加/，否则报错
@app.route('/index/')
def index():
    return 'Welcome to Index Page!'

if __name__=='__main__':
    # debug开启调试模式，开启后修改python代码会自动重启
    app.run(debug=True)
from datetime import datetime

from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return 'Flask home'


@app.route('/index/')
def index():
    # 返回字符串：支持html标签
    # return '<b>Flask Index<b>'

    # 　模板渲染
    return render_template('index.html', name='法外狂徒张三')

    # jsonify:序列化
    # return jsonify({'name':'张三','age':18})


# 过滤器
def datetime_format(value, format='%Y年-%m月-%d日 %H:%M:%S'):
    # strftime:将value格式化为指定的格式字符串
    return value.strftime(format)


# 将datetime_format函数注册为模块过滤器，命名为dformat
app.add_template_filter(datetime_format, 'dformat')


@app.route('/filter/')
def filter():
    time = datetime.now()
    return render_template("filter.html", time=time)


# 模块访问对象属性
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


@app.route('/user/')
def user():
    person = User(username='尹之妍', email='123@qq.com')
    return render_template("filter.html", person=person)


# if语句
@app.route('/control/<int:age>')
def control(age):
    return render_template("control.html", age=age)


# for循环
@app.route('/book/')
def book():
    books = [{'name': '三国演义', 'author': '罗贯中'}, {'name': '红楼梦', 'author': '曹雪芹'}]
    return render_template("control.html", books=books)


if __name__ == '__main__':
    # debug:开启调试模式，开启后修改python代码会自动重启
    # port:默认端口为5000
    # host:默认主机名为127.0.0.1，指定0.0.0.0代表本机所有ip
    # app.run(debug=True,port=5000,host='0.0.0.0')
    app.run(debug=True)

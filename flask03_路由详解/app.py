from flask import Flask, send_from_directory, jsonify

app = Flask(__name__)

# 1.静态路由
@app.route('/')
def index():
    return 'Welcome to Index Page!'

# 2.路由参数:在URL中动态传递参数
@app.route('/book/list/<currentPage>/')
def book_list(currentPage):
    return f'这是第{currentPage}页的图书列表!'

"""
3.路由规则:使用类型转换器指定URL参数的类型
    1.字符串(默认):匹配任意字符串
    2.<int:value>:匹配整数值
    3.<float:value>:匹配浮点数值
    4.<path:value>:匹配任意字符，包括 /
"""
# 默认字符串
@app.route('/user/name/<name>/')
def string_type(name):
    return f'姓名:{name}'

# int型
@app.route('/user/age/<int:age>/')
def int_type(age):
    return f'年龄:{age}'

# float型
@app.route('/user/money/<float:money>')
def float_type(money):
    return f'余额:{money}'

# path:从本机下载文件
# send_from_directory:flask的一个函数，用于安全地从指定目录发送文件到客户端，主要用于文件下载
@app.route('/files/<path:filename>')
def down_file(filename):
    return send_from_directory('C:/Users/Administrator/Desktop',filename)

# 4.请求方法:指定HTTP方法
@app.route('/submit/',methods=['GET'])
def submit():
    return 'Form submitted!'

"""
5.路由函数返回
    1.字符串:返回文本响应
    2.HTML:返回html页面
    3.JSON:返回json数据
    4.Response:自定义响应
"""
# 文本类型的响应
@app.route('/text/')
def text_response():
    return "这是一个文本类型的响应!"

# html格式的响应
@app.route('/html/')
def html_response():
    return '<h3>这是一个html的响应</h3>'

# json格式的响应
# json中，特殊字符会被表示为Unicode转义序列
@app.route('/json/')
def json_response():
    data = {'name':'尹之妍','age':18}
    return jsonify(data)
if __name__=='__main__':
    app.run(debug=True)
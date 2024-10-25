from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Flask home'

@app.route('/index/')
def index():
    # 返回字符串：支持html标签
    # return '<b>Flask Index<b>'

    #　模板渲染
    return render_template('index.html',name='法外狂徒张三')

    # jsonify:序列化
    # return jsonify({'name':'张三','age':18})

if __name__=='__main__':
    # debug:开启调试模式，开启后修改python代码会自动重启
    # port:默认端口为5000
    # host:默认主机名为127.0.0.1，指定0.0.0.0代表本机所有ip
    # app.run(debug=True,port=5000,host='0.0.0.0')
    app.run(debug=True)
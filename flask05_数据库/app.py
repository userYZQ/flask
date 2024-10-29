from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# 配置数据库连接信息
HOSTNAME = '127.0.0.1'
PORT = 3306
USERNAME = 'root'
PASSWORD = '123456'
DATABASE = 'flask_database'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"


# 创建db对象
db = SQLAlchemy(app)

# 测试连接
with app.app_context():
    with db.engine.connect() as conn:
        response = conn.execute(text("select 1"))
        print(response.fetchone())

if __name__ == '__main__':
    app.run(debug=True)

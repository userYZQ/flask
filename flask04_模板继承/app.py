from flask import Flask, render_template

app = Flask(__name__)

@app.route('/child1/')
def child1():
    return render_template("child1.html")

@app.route('/child2/')
def child2():
    return render_template("child2.html")

@app.route('/static/')
def static_demo():
    return render_template("static.html")
if __name__=='__main__':
    app.run(debug=True)
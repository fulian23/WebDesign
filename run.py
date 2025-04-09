from flask import Flask, render_template

from app import routes

from app.api import search
app = Flask(__name__)

app.register_blueprint(routes.test)
app.register_blueprint(search.search)

@app.route('/')
def hello_world():
    data = {'name': 'John', 'age': 25, "list":['a','b','c']}
    return render_template('base.html',data=data)

@app.route('/test')
def test():
    data={} #这里填需要的测试数据
    return render_template('test.html',data=data)


if __name__ == '__main__':
    app.run()


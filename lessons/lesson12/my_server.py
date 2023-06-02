import json

from flask import Flask, request, render_template

app = Flask(__name__)


#
#
# @app.route('/')
# def hello_world():
#     return '<b>Hello<\b>, World!'
#
#
# @app.route('/user')
# def hello_user():
#     return 'Hello, User!'
#
#
# @app.route('/user/<name>')
# def hello_user_name(name):
#     return f'Hello, {name}!'
#
# @app.route('/gohome')
# def hello_user_go_home():
#     return redirect(url_for("hello_user"))
#
# @app.route("/check_method", methods=['GET', 'POST',])
# def check_method():
#     if request.method == 'POST':
#         return "You are using POST"
#     else:
#         return "You are probably using GET"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('name.html', my_name=name)


def valid_login(name, password):
    return name == password


def log_the_user_in(name):
    return f" Hello, you are an authorized user {name} "


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return render_template('login.html', msg=log_the_user_in(request.form['username']))
        error = 'Invalid username/password'
        return render_template('login.html', error=error)
    else:
        return render_template('login.html')


user = {"name": "Liubomyr",
        "age": 36}


@app.route('/user', methods=['POST', 'GET'])
def get_user_json():
    if request.method == 'GET':
        return json.dumps(user)
    elif request.method == 'POST':
        return str(user)


if __name__ == '__main__':
    app.run(debug=True)

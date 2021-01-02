from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'I did it! You can read more about this app -> ' + \
           'https://github.com/MariaMozgunova/flask-app'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

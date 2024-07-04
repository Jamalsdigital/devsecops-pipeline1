from flask import flask # type: ignore
app = flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, DevSecOps!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
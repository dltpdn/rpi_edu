from flask import Flask


app = Flask(__name__)

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route('/')
def root():
    return "<h1>this is main page</h1>"


@app.route('/aaa.html')
def abc():
    return "<h1>this is abc.html</h1>"



app.run(host='0.0.0.0', port=8888)
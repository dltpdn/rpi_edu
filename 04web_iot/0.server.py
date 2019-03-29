import flask

app = flask.Flask(__name__)
app.env = "debug"

@app.route('/')
def index():
    return "Hello!"

app.run(host="192.178.0.2")
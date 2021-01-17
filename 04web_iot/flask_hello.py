from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <h1>Hello flask!</h1>
    <a href="/next">Go Next</a>
    '''

@app.route("/next")
def next():
    return '''
    <h1>Next Page</h1>
    <a href="/">Go Home</a>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
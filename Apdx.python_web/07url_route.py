from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    return  '<h1> This is root page</h1><a href="/next">Go next</a>'

@app.route('/next')
def next():
    return  '<h1> This is Next page</h1><a href="/">Go Root</a>'


app.run()

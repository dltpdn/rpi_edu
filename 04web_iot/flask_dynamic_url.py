from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return app.send_static_file('dynamic_url.html')

@app.route("/user/<name>/<int:id>")
def user(name, id):
    return f'''
    <h1>User</h1>
    <p>name:{name}, id:{id}</p>
    <a href="/">Back</a>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
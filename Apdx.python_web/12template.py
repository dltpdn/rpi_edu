from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/template')
@app.route('/template/<name>')
def template_test(name=None):
    gender = request.args.get('gender')
    drinks = ['cofee', 'milk', 'tea', 'beer']
    return render_template('test.html',name=name, gender=gender, drinks=drinks)

app.run()

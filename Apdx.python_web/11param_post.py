from flask import Flask, request, redirect

app = Flask(__name__)



@app.route('/')
def root():
   return  redirect('/static/form.html')
    
    
@app.route('/post_param', methods=['POST'])
def post_param():
#    id = request.form['id']
    id = request.values['id']
    pwd = request.form['pwd']
    return 'ID: %s, PWD:%s' %(id, pwd)


app.run()
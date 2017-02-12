from flask import Flask, request

app = Flask('my')

@app.route('/get_param', methods=['GET'])
def get_param():
    #id= request.args.get('id')
    id = request.values['id']
    pwd = request.args.get('pwd')
    return  'id: %s , pwd : %s' %(id, pwd)

@app.route('/')
def root():
    return '<a href="/get_param?id=abc&pwd=1234">get_param</a>'

app.run()
from flask import Flask

app = Flask(__name__)

@app.route('/user/<id>', methods=['GET'])
def show_user(id):
    print id
    if id == "abc":
        return 'User id is %s, name is %s' %(id, 'Lee')
    elif id == "xyz":
        return 'User id is %s, name is %s' %(id, 'Kim')
    else:
        return 'No User id : %s' %id
    
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post id : %d' %post_id

app.run()    
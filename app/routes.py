from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Stygian Gray'}
    posts = [
        {
            'author': {'username': 'Kool Keith'},
            'body': 'I\'m traveling at the speed of thought'
        },
        {
            'author': {'username': 'Tony Stark'},
            'body': 'I am Iron Man'
        }
    ]
    
    return render_template('index.html', title='The Home of', user=user, posts=posts)
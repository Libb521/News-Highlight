from flask import render_template
from app import app

#views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "For The Latest and Newest News Articles"
    return render_template('index.html',title = title)

@app.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    title = f'You are viewing {news_id}'
    return render_template('news.html',title = title)
from flask import render_template
from app import app
from .fetch import get_sources,get_articles

#views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    sources = get_sources('category')
    print(sources)
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    title = 'For The Latest and Newest News Articles'

    return render_template('index.html', title = title,sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources=entertainment_sources)
    
@app.route('/sources/<id>')
def news(id):

    '''
    View news page function that returns the news details page and its data
    '''
    articles = get_articles(id)
    title = f'{id}'
    return render_template('articles.html',title = title,articles = articles)
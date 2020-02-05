from flask import render_template
from app import app
from .fetch import get_sources

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

    # search_source = request.args.get('source_query')

    # if search_source:
    #     return redirect(url_for('search',source_name=search_source))
    # else:
    return render_template('index.html', title = title,sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources=entertainment_sources)
    

@app.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    title = f'You are viewing {news_id}'
    return render_template('news.html',title = title)
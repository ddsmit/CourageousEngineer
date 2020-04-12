import flask
from flask import render_template
from chrissmit import services

blueprint = flask.Blueprint('navigation_views', __name__, template_folder='templates')

@blueprint.route('/articles/<article>')
def article(article):
    article_data = services.article.get_article_data(article)
    return render_template(
        template_name_or_list='articles/article.html',
        story=article_data
        )
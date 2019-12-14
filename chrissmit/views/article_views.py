import flask
from chrissmit.infrastructure.view_modifiers import response
import chrissmit.services.article_service as article_service

blueprint = flask.Blueprint('navigation_views', __name__, template_folder='templates')

@blueprint.route('/articles/<article>')
@response(template_file='articles/article.html')
def article(article):
    article_data = article_service.get_article_data(article)
    return dict(article=article_data)
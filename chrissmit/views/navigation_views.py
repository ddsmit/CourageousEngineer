import flask
from chrissmit.infrastructure.view_modifiers import response
import chrissmit.services.article_service as article_service

blueprint = flask.Blueprint('navigation', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='navigation/index.html')
def index():
    last_four = article_service.get_last_four_articles()
    return dict(articles=last_four)


@blueprint.route('/about')
@response(template_file='navigation/about.html')
def about():
    return dict()


@blueprint.route('/articles')
@response(template_file='navigation/articles.html')
def articles():
    articles = article_service.get_all_articles()
    return dict(articles=articles)

@blueprint.route('/contact')
@response(template_file='navigation/contact.html')
def contact():
    return dict()

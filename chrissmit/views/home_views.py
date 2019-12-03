import flask
from chrissmit.infrastructure.view_modifiers import response
import chrissmit.services.article_service as article_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    last_four = article_service.get_last_four_articles()
    return dict(articles=last_four)


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return dict()

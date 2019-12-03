import flask
from chrissmit.infrastructure.view_modifiers import response
import chrissmit.services.article_service as article_service

blueprint = flask.Blueprint('home_views', __name__, template_folder='templates')

@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return dict()
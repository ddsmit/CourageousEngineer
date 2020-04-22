import flask
from flask import render_template
from chrissmit.services import article, profile
from flask_login import current_user

blueprint = flask.Blueprint('navigation_views', __name__, template_folder='templates')


@blueprint.route('/articles/<article_id>')
def read_article(article_id):
    current_article = article.get(article_id)
    current_edit = article.get_edit(current_article.current_edit_id)
    current_author = profile.get(id=current_article.author_id)
    return render_template(
        template_name_or_list='articles/read.html',
        article=current_article,
        edit = current_edit,
        author = current_author,
        release=False,
        suggest_edit=current_user.is_authenticated,
        go_to_latest = False,
    )

@blueprint.route('/review/edit/<edit_id>')
def view(edit_id):
    current_edit = article.get_edit(edit_id)
    current_article = article.get(current_edit.article_id)
    current_author = profile.get(id=current_article.author_id)
    can_release = profile.all_access() and current_user.id != current_article.author_id and current_edit.is_ready_for_release 
    return render_template(
        template_name_or_list='articles/read.html',
        article=current_article,
        edit = current_edit,
        author = current_author,
        release=can_release,
        suggest_edit=current_user.is_authenticated,
        go_to_latest = False,
    )

        
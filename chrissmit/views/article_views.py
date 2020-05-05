import flask
from flask import render_template
from chrissmit.services import article, profile
from flask_login import current_user, login_required

blueprint = flask.Blueprint('navigation_views', __name__, template_folder='templates')


@blueprint.route('/articles/<article_id>')
def read_article(article_id):
    recent_articles = article.get_last(4)
    current_article = article.get_article(article_id)
    current_edit = article.get_edit(current_article.current_edit_id)
    tags = article.get_edit_tags(current_edit.id)
    return render_template(
        template_name_or_list='articles/read.html',
        article=current_article,
        edit = current_edit,
        release=False,
        suggest_edit=current_user.is_authenticated,
        go_to_latest = False,
        recent_articles=recent_articles,
        tags=tags,
    )

@blueprint.route('/review/edit/<edit_id>')
@login_required
def view(edit_id):
    recent_articles = article.get_last(4)
    current_edit = article.get_edit(edit_id)
    current_article = article.get_article(current_edit.article_id)
    tags = article.get_edit_tags(current_edit.id)
    can_release = profile.all_access() and current_user.id != current_article.author_id and current_edit.is_ready_for_release 
    return render_template(
        template_name_or_list='articles/read.html',
        edit = current_edit,
        release=can_release,
        suggest_edit=current_user.is_authenticated,
        go_to_latest = False,
        recent_articles=recent_articles,
        tags=tags,
    )

@blueprint.route('/articles/<tag>')
def by_tag(tag):
    pass

        
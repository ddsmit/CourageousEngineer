import flask
from flask import render_template
from chrissmit.services import article, profile
from flask_login import current_user, login_required

blueprint = flask.Blueprint('navigation_views', __name__, template_folder='templates')


@blueprint.route('/articles/<article_id>')
def read_article(article_id):
    recent_articles = article.get_last(4)
    current_article = article.get_full_article(article_id)
    # current_edit = article.get_edit(current_article.current_edit_id)
    tags = article.get_edit_tags(current_article.current_edit_id)
    return render_template(
        template_name_or_list='articles/read.html',
        content=current_article,
        # edit = current_edit,
        release=False,
        suggest_edit=current_user.is_authenticated,
        go_to_latest = False,
        recent_articles=recent_articles,
        tags=tags,
        display_posted = article.is_display_posted(current_article),
    )

@blueprint.route('/review/edit/<edit_id>')
@login_required
def view(edit_id):
    recent_articles = article.get_last(4)
    current_edit = article.get_full_edit(edit_id)
    # current_article = article.get_article(current_edit.article_id)
    tags = article.get_edit_tags(current_edit.id)
    can_release = profile.all_access() and current_user.id != current_edit.author_id and current_edit.is_ready_for_release 
    return render_template(
        template_name_or_list='articles/read.html',
        content = current_edit,
        # article = current_article,
        release=can_release,
        suggest_edit=current_user.is_authenticated,
        go_to_latest = False,
        recent_articles=recent_articles,
        tags=tags,
        display_posted = article.is_display_posted(current_edit),
    )

@blueprint.route('/articles/tag/<tag>')
def article_by_tag(tag):
    recent_articles = article.get_last(4)
    articles = article.get_by_tag(tag)
    tags = article.get_tags()
    return render_template(
        template_name_or_list='navigation/articles.html',
        recent_articles=recent_articles, 
        articles=articles,
        tags=tags,
        current_tags=tag,
    )

@blueprint.route('/articles')
def all_articles():
    recent_articles = article.get_last(4)
    articles = article.get_all_released()
    tags = article.get_tags()
    return render_template(
        template_name_or_list='navigation/articles.html',
        recent_articles=recent_articles, 
        articles=articles,
        tags=tags,
        current_tags=[],
    )

        
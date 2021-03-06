import flask
from flask import render_template, flash, redirect, url_for
from chrissmit.services import article, profile, navigation, image
from flask_login import current_user, login_required

blueprint = flask.Blueprint('navigation_views', __name__, template_folder='templates')


@blueprint.route('/articles/<article_id>')
def read_article(article_id):
    current_article = article.get_full_article(article_id)

    if not current_article:
        flash('Article does not exist, please check your url. If  you navigated to the URL from our site, please help us out by reporting the error on the "Contact" page.','warning')
        return redirect(url_for('navigation_views.all_articles'))
    
    if not current_article.is_released:
        flash(f'{current_article.title} has not been released to the public yet, or it has been archived.', 'warning')
        return redirect(url_for('navigation_views.all_articles'))

    tags = article.get_edit_tags(current_article.current_edit_id)
    author = profile.get(id=current_article.author_id)
    return render_template(
        template_name_or_list='articles/read.html',
        website_title=current_article.title,
        website_description=current_article.preview,
        website_image=image.get_preview(current_article.image_file),
        website_publish=current_article.posted,
        website_author_twitter=author.twitter_handle,
        content=current_article,
        release=False,
        suggest_edit=current_user.is_authenticated,
        go_to_latest=False,
        nav_data=navigation.data(), 
        tags=tags,
        display_posted=article.is_display_posted(current_article),
        additional_script='/static/js/article.js',
    )

@blueprint.route('/review/edit/<edit_id>')
@login_required
def view(edit_id):
    current_edit = article.get_full_edit(edit_id)
    tags = article.get_edit_tags(current_edit.id)
    can_release = profile.all_access() and current_user.id != current_edit.author_id and current_edit.is_ready_for_release 
    return render_template(
        template_name_or_list='articles/read.html',
        website_title=current_edit.title,
        content=current_edit,
        release=can_release,
        suggest_edit=current_user.is_authenticated,
        go_to_latest=False,
        nav_data=navigation.data(), 
        tags=tags,
        display_posted = article.is_display_posted(current_edit),
        additional_script='/static/js/article.js',
    )

@blueprint.route('/articles/tag/<tag>')
def article_by_tag(tag):
    articles = article.get_by_tag(tag)
    tags = article.get_current_used_tags()
    return render_template(
        template_name_or_list='navigation/articles.html',
        website_title = article.get_tag_desc(tag),
        website_description = f'Articles with tag: {article.get_tag_desc(tag)}',
        nav_data=navigation.data(), 
        articles=articles,
        tags=tags,
        current_tags=[int(tag)],
    )

@blueprint.route('/articles')
def all_articles():
    articles = article.get_all_released()
    tags = article.get_current_used_tags()
    return render_template(
        template_name_or_list='navigation/articles.html',
        website_title='Read some amazing stories.',
        website_description="Browse all of the articles we've written so far.",
        nav_data=navigation.data(), 
        articles=articles,
        tags=tags,
        current_tags=[],
    )

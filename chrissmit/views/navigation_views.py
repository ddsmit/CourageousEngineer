import flask
from flask import render_template, url_for, redirect
from chrissmit.infrastructure.view_modifiers import response
import chrissmit.services.article_service as article_service
import chrissmit.services.author_service as author_service
from chrissmit.services.db_models import User, Post, Update
from chrissmit.forms.content import UpdatesForm
from chrissmit import db
from flask_login import current_user

blueprint = flask.Blueprint('navigation', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET','POST'])
def index():
    updates_form = UpdatesForm()
    updates = Update.query.all()
    last_four = article_service.get_last_four_articles()
    if updates_form.validate_on_submit():
        new_update = Update(
            title=updates_form.title.data,
            user_id=current_user.username,
            content=updates_form.content.data,
        )
        db.session.add(new_update)
        db.session.commit()
        return redirect(url_for('navigation.index'))

    return render_template(
        template_name_or_list='navigation/index.html',
        recent_articles=last_four, 
        update_form = updates_form, 
        updates=updates,
        )


@blueprint.route('/about')
@response(template_file='navigation/about.html')
def about():
    last_four = article_service.get_last_four_articles()
    authors = User.query.all()
    print(authors)
    return dict(recent_articles=last_four, authors=authors)


@blueprint.route('/articles')
@response(template_file='navigation/articles.html')
def articles():
    articles = article_service.get_all_articles()
    last_four = article_service.get_last_four_articles()
    return dict(articles=articles, recent_articles=last_four)

@blueprint.route('/contact')
@response(template_file='navigation/contact.html')
def contact():
    last_four = article_service.get_last_four_articles()
    return dict(recent_articles=last_four)

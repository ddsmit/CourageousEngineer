import flask
from flask import render_template, url_for, redirect, flash
from chrissmit.services import profile, article, update, messages
from chrissmit.forms.content import UpdatesForm, ContactForm
from chrissmit import db
from flask_login import current_user

blueprint = flask.Blueprint('navigation', __name__, template_folder='templates')

@blueprint.route('/', methods=['GET','POST'])
def index():
    updates_form = UpdatesForm()
    recent_updates = update.get_last(5)
    recent_articles = article.get_last(4)
    if updates_form.validate_on_submit() and current_user.is_authenticated:
        update.create(updates_form)
        return redirect(url_for('navigation.index'))
    return render_template(
        template_name_or_list='navigation/index.html',
        recent_articles=recent_articles, 
        update_form = updates_form, 
        updates=recent_updates,
    )


@blueprint.route('/about')
def about():
    recent_articles = article.get_last(4)
    authors = profile.get_all()
    return render_template(
        template_name_or_list='navigation/about.html',
        recent_articles=recent_articles, 
        authors=authors,
    )

@blueprint.route('/articles')
def articles():
    articles = article.get_all_released()
    recent_articles = article.get_last(4)
    return render_template(
        template_name_or_list='navigation/articles.html',
        recent_articles=recent_articles, 
        articles=articles,
    )

@blueprint.route('/contact', methods=['GET','POST'])
def contact():
    recent_articles = article.get_last(4)
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        messages.save(contact_form)
        flash('Thank you for contacting us! We love the feedback!', 'success')
        return redirect(url_for('navigation.index'))
    return render_template(
        template_name_or_list='navigation/contact.html',
        recent_articles=recent_articles, 
        contact_form=contact_form,
    )

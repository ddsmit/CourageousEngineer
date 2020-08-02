import flask
from flask import render_template, url_for, redirect, flash
from chrissmit.services import profile, article, update, messages, navigation, image
from chrissmit.forms.content import UpdatesForm, ContactForm
from chrissmit import db
from flask_login import current_user

blueprint = flask.Blueprint('navigation', __name__, template_folder='templates')

@blueprint.route('/', methods=['GET','POST'])
def index():
    return render_template(
        template_name_or_list='navigation/index.html',
        website_title='Welcome to Courageous Engineer!',
        nav_data=navigation.data(), 
    )


@blueprint.route('/about/<id>')
def about(id):
    current_profile = profile.get(id=id)
    return render_template(
        template_name_or_list='navigation/about.html',
        website_title=f'Meet {current_profile.full_name}!',
        website_description=f'Learn more about {current_profile.full_name}',
        website_image=image.get_preview(current_profile.image_file),
        nav_data=navigation.data(), 
        author=current_profile,
    )

@blueprint.route('/contact', methods=['GET','POST'])
def contact():
    contact_form = ContactForm()
    contact_form.reason.choices = messages.get_reasons()
    if contact_form.validate_on_submit():
        messages.save(contact_form)
        flash('Thank you for contacting us! We love the feedback!', 'success')
        return redirect(url_for('navigation.index'))
    return render_template(
        template_name_or_list='navigation/contact.html',
        website_title='We love to hear from you!',
        nav_data=navigation.data(), 
        contact_form=contact_form,
    )

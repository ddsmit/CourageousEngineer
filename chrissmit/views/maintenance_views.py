from flask import Blueprint, render_template, url_for, redirect, flash, request
from chrissmit.services.db_models import User, Post, Update
from chrissmit.forms.content import UpdateProfile, UpdatesForm
from chrissmit import db
from chrissmit.services import profile, article, update
from flask_login import current_user, login_required

blueprint = Blueprint('maintenance', __name__, template_folder='templates')

# TODO won't update the profile on submit
# TODO need to add validation for duplicate emails, user names, etc.
# TODO need to update the routes to only be accessabile with a login
@blueprint.route('/update/profile',methods=['GET','POST'])
def update_profile():
    profile_form = UpdateProfile()
    if profile_form.validate_on_submit() and current_user.is_authenticated:
        profile.update(profile_form)
        flash('Profile updated','success')
        return redirect(url_for('maintenance.update_profile'))
    elif request.method == 'GET':
        profile_form = profile.update_form_data(profile_form)
    return render_template(
        template_name_or_list=f'maintenance/profile.html', 
        profile_form=profile_form,
        )

@blueprint.route('/delete/update/<update_id>')
def delete_update(update_id):
    update = Update.query.get(update_id)
    db.session.delete(update)
    db.session.commit()
    return redirect(url_for('navigation.index'))

@blueprint.route('/update/update/<update_id>', methods=['GET','POST'])
def update_update(update_id):
    current_update = update.get(int(update_id))
    update_form = UpdatesForm()
    print(current_update)
    if update_form.validate_on_submit():
        update.update(update_form, current_update)
        return redirect(url_for('navigation.index'))
    elif request.method == 'GET':
        update_form = update.update_form_data(update_form, current_update)
    
    return render_template('maintenance/update.html', update_form=update_form)



@blueprint.route('/update/articles')
def update_articles():
    profile_form = UpdateProfile()
    profile_form.email.data = 'current_user.email'
    print(current_user)
    return render_template(
        template_name_or_list=f'maintenance/profile.html', 
        profile_form=profile_form,
        )


@blueprint.route('/read/messages')
def read_messages():
    profile_form = UpdateProfile()
    profile_form.email.data = current_user.full_name
    return render_template(
        template_name_or_list=f'maintenance/profile.html', 
        profile_form=profile_form,
        )


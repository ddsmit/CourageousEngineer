from flask import Blueprint, render_template, url_for, redirect
from chrissmit.services.db_models import User, Post, Update
from chrissmit.forms.content import UpdateProfile
from chrissmit import db
from flask_login import current_user, login_required

blueprint = Blueprint('maintenance', __name__, template_folder='templates')

# TODO won't update the profile on submit
# TODO need to add validation for duplicate emails, user names, etc.
@blueprint.route('/update/profile',methods=['GET','POST'])
def update_profile():
    profile_form = UpdateProfile()
    profile_form.full_name.data = current_user.full_name
    profile_form.user_name.data = current_user.username
    profile_form.email.data = current_user.email
    profile_form.content.data = current_user.content
    if profile_form.validate_on_submit() and current_user.is_authenticated:
        current_user.full_name=profile_form.full_name.data
        current_user.username=profile_form.user_name.data
        current_user.email=profile_form.email.data
        current_user.content=profile_form.content.data
        db.session.commit()
        return redirect(url_for('maintenance.update_profile'))
    return render_template(
        template_name_or_list=f'maintenance/profile.html', 
        profile_form=profile_form,
        )


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


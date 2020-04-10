from flask import Blueprint, render_template, url_for, redirect
from chrissmit.services.db_models import User, Post, Update
from chrissmit.forms.content import ProfileForm
from chrissmit import db
from flask_login import current_user, login_required

blueprint = Blueprint('maintenance', __name__, template_folder='templates')

@blueprint.route('/update/profile')
def update_profile():
    profile_form = ProfileForm()
    return render_template(
        template_name_or_list=f'maintenance/area.html', 
        profile_form=profile_form,
        )


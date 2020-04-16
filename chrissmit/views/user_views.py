from flask import flash, redirect, url_for, Blueprint, render_template, request
from flask_login import login_user, logout_user, current_user
from chrissmit.services.db_models import User
from chrissmit.forms.user import LogInForm, RegistrationFrom
from chrissmit.services import profile


blueprint = Blueprint('user', __name__, template_folder='templates')

@blueprint.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('navigation.index'))
    form = LogInForm()
    if form.validate_on_submit():
        user = profile.get(email=form.email.data)
        if user and profile.is_password_correct(user.password,form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f'Logged in as {user.full_name}','success')
            return redirect(next_page) if next_page else redirect(url_for('navigation.index'))
        else:
            flash(f'Something went wrong, please check the email and password.', 'danger')
    print(current_user.full_name)
    return render_template(template_name_or_list='user/login.html', form=form, additional_css='/static/css/forms.css')

@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('navigation.index'))



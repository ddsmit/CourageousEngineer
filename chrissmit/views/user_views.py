from flask import flash, redirect, url_for, Blueprint, render_template, request
from flask_login import login_user, logout_user, current_user
from chrissmit.infrastructure.view_modifiers import response
from chrissmit.services.db_models import User
from chrissmit.forms.user import LogInForm, RegistrationFrom
from chrissmit import bcrypt

blueprint = Blueprint('user', __name__, template_folder='templates')


# @blueprint.route('/registration', methods=['GET','POST'])
# # @response(template_file='user/registration.html')
# def registration():
#     form = RegistrationFrom()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('navigation.index'))
#     return render_template(
#         template_name_or_list='user/registration.html',
#         form=form,
#         additional_css='/static/css/forms.css'
#     )


@blueprint.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('navigation.index'))
    form = LogInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Logged in as {user.username}','success')
            return redirect(url_for('navigation.index'))
        else:
            flash(f'Something went wrong, please check the email and password.', 'danger')
    return render_template(template_name_or_list='user/login.html', form=form, additional_css='/static/css/forms.css')

@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('navigation.index'))



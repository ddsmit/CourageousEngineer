from flask import flash, redirect, url_for, Blueprint, render_template, request
from flask_login import login_user, logout_user, current_user
from chrissmit.services.db_models import User
from chrissmit.forms.user import LogInForm, RequestResetForm, ResetPasswordForm
from chrissmit.services import profile, article, navigation

blueprint = Blueprint('user', __name__, template_folder='templates')

@blueprint.route('/login', methods=['GET','POST'])
def login():
    form = LogInForm()
    if current_user.is_authenticated:
        return redirect(url_for('navigation.index'))
    if form.validate_on_submit():
        user = profile.get(email=form.email.data)
        if user and profile.is_password_correct(user.password,form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f'Logged in as {user.full_name}','success')
            return redirect(next_page) if next_page else redirect(url_for('navigation.index'))
        else:
            flash(f'Something went wrong, please check the email and password.', 'danger')
    return render_template(
        template_name_or_list='user/login.html', 
        website_title='Log in to your account',
        form=form, 
        additional_css='/static/css/forms.css',
        nav_data=navigation.data(), 
    )

@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('navigation.index'))

@blueprint.route('/resetpassword', methods=['GET','POST'])
def request_reset():
    form =RequestResetForm()
    if form.validate_on_submit():
        user = profile.get(email=form.email.data)
        profile.update_password_email(user)
        flash('Email has been sent with instructions on changing your password.', 'success')
        return redirect(url_for('user.logout'))
    if current_user.is_authenticated:
        form.email.data = current_user.email
    return render_template(
        template_name_or_list='user/requestresetpassword.html',
        website_title='Reset you password',
        form=form,
        additional_css='/static/css/forms.css',
        nav_data=navigation.data(),
    )

@blueprint.route('/resetpassword/<token>', methods=['GET','POST'])
def reset_password(token):
    form =ResetPasswordForm()
    verified_user = profile.verify_reset_token(token)
    if not verified_user:
        flash('Request has expired or invalid url used.', 'warning')
        return redirect(url_for('navigation.index'))
    if form.validate_on_submit():
        profile.update_password(user=verified_user, form=form,)
        return redirect(url_for('navigation.index'))
    return render_template(
        template_name_or_list='user/resetpassword.html',
        website_title='Reset you password',
        form=form,
        user=verified_user,
        additional_css='/static/css/forms.css',
        nav_data=navigation.data(),
    )


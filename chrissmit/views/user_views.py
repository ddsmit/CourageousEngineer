from flask import flash, redirect, url_for, Blueprint, render_template

from chrissmit.infrastructure.view_modifiers import response
from chrissmit.forms.user import LogInForm, RegistrationFrom

blueprint = Blueprint('user', __name__, template_folder='templates')


@blueprint.route('/registration', methods=['GET','POST'])
# @response(template_file='user/registration.html')
def registration():
    form = RegistrationFrom()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('navigation.index'))
    return render_template(
        template_name_or_list='user/registration.html',
        form=form,
        additional_css='/static/css/forms.css'
    )


@blueprint.route('/login', methods=['GET','POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        flash(f'Invalid Email or Password. Please check spelling and try again','warning')
    return render_template(template_name_or_list='user/login.html', form=form, additional_css='/static/css/forms.css')
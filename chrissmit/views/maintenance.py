from flask import flash, redirect, url_for, Blueprint, render_template, request
from chrissmit.services import author_service, article_service

from chrissmit.forms.user import LogInForm, RegistrationFrom

blueprint = Blueprint('maintenance', __name__, template_folder='templates')

@blueprint.route('/updatesite', methods=['GET','POST'])
def user_main():
    return render_template(template_name_or_list='maintenance/main.html')

@blueprint.route('/updatesite/<area>')
def article(area):
    if area == 'authors':
        function = author_service.get_all_authors
    elif area == "articles":
        function = article_service.get_all_articles
    available_records = function()
    return render_template(template_name_or_list=f'maintenance/area.html', available_records=available_records)


from chrissmit.services.db_models import Update
from chrissmit import bcrypt, db
from flask_login import current_user

def get_all(desc=True):
    if desc:
        return Update.query.order_by(Update.posted.desc()).all()
    return Update.query.all()

def get_last(number=4, desc=True):
    if desc:
        return Update.query.order_by(Update.posted.desc()).limit(number).all()
    return Update.query.limit(number).all()

def get(id):
    return Update.query.filter_by(id=id).first()

def update(form, update):
    update.title=form.title.data
    update.content=form.content.data
    db.session.commit()

def update_form_data(form, update):
    form.title.data = update.title
    form.content.data = update.content
    return form


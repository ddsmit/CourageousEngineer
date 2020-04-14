from chrissmit.services.db_models import Article
from flask_login import current_user

def get_all(desc=True):
    if desc:
        return Article.query.order_by(Article.posted.desc()).all()
    return Article.query.all()


def get_all_released(desc=True):
    if desc:
        return Article.query.filter_by(is_released=True).order_by(Article.posted.desc()).all()
    return Article.query.filter_by(is_released=True).all()

def get_all_ready_for_review(desc=True):
    if desc:
        return Article.query.filter_by(is_ready_for_review=True, is_realease=False).order_by(Article.posted.desc()).all()
    return Article.query.filter_by(is_ready_for_review=True, is_realease=False).all()

def get_last(number=4, desc=True):
    if desc:
        return Article.query.filter_by(is_released=True).order_by(Article.posted.desc()).limit(number).all()
    return Article.query.filter_by(is_released=True).limit(number).all()

def get(id):
    return Article.query.filter_by(id=id).first()



def update(form, article):
    article.title=form.title.data
    article.content=form.content.data
    db.session.commit()

def update_form_data(form, update):
    form.title.data = article.title
    form.content.data = article.content
    return form
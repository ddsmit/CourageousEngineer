from chrissmit.services.db_models import Article, ArticleEdits
from chrissmit import db, bcrypt
from flask_login import current_user
from datetime import datetime

def new_edit(current_edit, current_article):
    return True

def create(form):
    new_article = Article(
        is_released = False,
        author_id = current_user.id,
    )
    db.session.add(new_article)
    db.session.commit()
    new_edit = ArticleEdits(
        article_id = new_article.id,
        is_edited = True,
        is_ready_for_release = False,
        user_id = current_user.id,
        title = form.title.data,
        preview = form.preview.data,
        content = form.content.data,
    )
    db.session.add(new_edit)
    db.session.commit()
    return new_edit

def freeze_edit(edit):
    edit.is_edited = False
    edit.is_ready_for_release = False
    db.session.commit()

def edit_is_ready_for_release(edit):
    edit.is_edited = False
    edit.is_ready_for_release = True
    db.session.commit()

def create_edit_existing(previous_edit):
    new_edit = ArticleEdits(
        article_id = previous_edit.article_id,
        is_edited = True,
        is_ready_for_release = False,
        user_id = current_user.id,
        title = previous_edit.title,
        preview = previous_edit.preview,
        content = previous_edit.content,
    )
    db.session.add(new_edit)
    db.session.commit()
    return new_edit

def get_edit(id):
    return ArticleEdits.query.filter_by(id=id).first()

def ready_for_review(edit):
    edit.is_ready_for_release = True
    edit.is_edited = False
    db.session.commit()

def release(edit):
    article = get(edit.article_id)
    article.posted = datetime.utcnow()
    article.current_edit_id = edit.id
    article.is_released = True
    db.session.commit()

def get_all_ready_for_review():
    pass


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
    article.preview=form.preview.data
    article.content=form.content.data
    db.session.commit()

def update_form_data(form, edit):
    form.title.data = edit.title
    form.content.data = edit.content
    form.preview.data = edit.preview
    return form
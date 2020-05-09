from chrissmit.services.db_models import Article, ArticleEdits, User, Tags, EditTags
from chrissmit import db, bcrypt
from flask_login import current_user
from datetime import datetime

def create(form, image_file = None):
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
        image_file = image_file,
    )
    db.session.add(new_edit)
    db.session.commit()
    create_edit_tags(edit_id=new_edit.id, form=form)
    return new_edit

def create_edit_tags(edit_id, form):
    for tag in form.tags.data:
        new_record = EditTags(
            edit_id = edit_id,
            tag_id = int(tag),
        )
        db.session.add(new_record)
    db.session.commit()

def create_edit_tags_existing(previous_edit, new_edit):
    existing_tags = EditTags.query.filter_by(edit_id = previous_edit.id).all()
    for tag in existing_tags:
        print('tag-',tag.id,'edit', new_edit.id)
        new_record = EditTags(
            edit_id = new_edit.id,
            tag_id = int(tag.tag_id)
        )
        db.session.add(new_record)
    db.session.commit()


def get_edit(id):
    return ArticleEdits.query.filter_by(id=int(id)).first()

def get_full_edit(id):
    full_edit = full_edit_data()
    return full_edit.filter(ArticleEdits.id==id).first()

def get_open_edits(desc=False, test=False):
    return get_full_edits(filter_criteria = ArticleEdits.is_edited == True)

def get_open_to_review(desc=False):
    return get_full_edits(filter_criteria = ArticleEdits.is_ready_for_release == True)

def get_full_edits(filter_criteria, desc=False):
    full_edit = full_edit_data()
    if desc:
        return full_edit.filter(filter_criteria).order_by(ArticleEdits.edited.desc()).all()
    return full_edit.filter(filter_criteria).all()

def get_article(id):
    return Article.query.filter_by(id=int(id)).first()

def get_full_article(id):
    full_article = full_article_data()
    return full_article.filter(Article.id==int(id)).first()

def get_all_released(desc=True):
    return get_full_articles(filter_criteria = Article.is_released==True)

def get_all_archived():
    return get_full_articles(
        filter_criteria = 
        Article.is_released==False and
        ArticleEdits.is_edited == False and
        ArticleEdits.is_ready_for_release==False
    )

def get_full_articles(filter_criteria, desc=True):
    full_article = full_article_data()
    if desc:
        return full_article.filter(filter_criteria).order_by(Article.posted.desc()).all()
    return full_article.filter(filter_criteria).all()

def get_last(number=4, desc=True):
    full_article = full_article_data()
    if desc:
        return full_article.filter(Article.is_released==True).order_by(Article.posted.desc()).limit(number).all()
    return full_article.filter(Article.is_released==True).limit(number).all()

def get_tags():
    all_tags = Tags.query.all()
    return [
        (str(tag.id), tag.desc) 
        for tag in all_tags
    ]

def get_edit_tags(edit_id):
    print(edit_id)
    return db.session.query(
        EditTags.tag_id, Tags.desc
    ).join(
        Tags,
        Tags.id == EditTags.tag_id
    ).filter(
        EditTags.edit_id == edit_id
    ).all()

def get_by_tag(tag):
    edit_id_by_tag = db.session.query(
        EditTags.edit_id
    ).filter(
        EditTags.tag_id == tag
    )
    return get_full_articles(
        filter_criteria = ArticleEdits.id.in_(edit_id_by_tag)
    )


def update_edit(form, edit):
    edit.title=form.title.data
    edit.preview=form.preview.data
    edit.content=form.content.data
    db.session.commit()
    delete_tags(edit.id)
    create_edit_tags(edit.id, form)


def update_form_data(form, edit):
    form.title.data = edit.title
    form.content.data = edit.content
    form.preview.data = edit.preview
    return form

def archive(article_id):
    article_to_archive = get_article(article_id)
    article_to_archive.is_released = False
    for edit in article_to_archive.all_edits:
        edit.is_edited = False
        edit.is_ready_for_release = False
    db.session.commit()

def unarchive(article_id):
    article_to_unarchive = get_article(article_id)
    last_edit = get_edit(article_to_unarchive.current_edit_id)
    new_edit = create_edit_existing(last_edit)
    article_to_unarchive.current_edit_id = new_edit.id
    db.session.commit()

def ready_for_review(edit):
    edit.is_ready_for_release = True
    edit.is_edited = False
    db.session.commit()

def release(edit):
    article = get_article(edit.article_id)
    article.posted = datetime.utcnow()
    article.current_edit_id = edit.id
    article.is_released = True
    db.session.commit()

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
        image_file = previous_edit.image_file,
    )
    db.session.add(new_edit)
    db.session.commit()
    create_edit_tags_existing(previous_edit,new_edit)
    return new_edit

def delete_tags(edit_id):
    tags = EditTags.query.filter_by(edit_id=edit_id).delete()
    db.session.commit()

def full_edit_data():
    fields = full_data_fields()
    return fields.join(
        Article, 
        ArticleEdits.article_id == Article.id,
    ).join(
        User, 
        ArticleEdits.user_id == User.id
    )

def full_article_data():
    fields = full_data_fields()
    return fields.join(
        ArticleEdits, 
        Article.current_edit_id == ArticleEdits.id,
    ).join(
        User, 
        Article.author_id == User.id
    )

def full_data_fields():
    return db.session.query(
        ArticleEdits.id,
        ArticleEdits.article_id,
        Article.posted,
        Article.edited,
        Article.is_released,
        Article.author_id,
        Article.current_edit_id,
        ArticleEdits.title, 
        ArticleEdits.preview, 
        ArticleEdits.content,
        ArticleEdits.image_file,
        ArticleEdits.user_id,
        ArticleEdits.is_edited,
        ArticleEdits.is_ready_for_release,
        ArticleEdits.edited,
        Article.author_id,
        User.full_name,
    )

def add_commas(tags):
    ids = [tag.tag_id for tag in tags]
    descs = [tag.desc for tag in tags]
    descs = ',-'.join(descs)
    descs = descs.split('-')
    return [
        {
            'tag_id':tag[0],
            'desc':tag[1],
        }
        for tag in zip(ids,descs)
    ]

def is_display_posted(content):
    if not content.posted:
        return content.posted
    return content.posted > content.edited
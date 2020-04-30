from flask import Blueprint, render_template, url_for, redirect, flash, request
from chrissmit.forms.content import UpdateProfile, UpdatesForm, ArticleForm
from chrissmit import db
from chrissmit.services import profile, article, update, image, messages
from flask_login import current_user, login_required

blueprint = Blueprint('maintenance', __name__, template_folder='templates')

@blueprint.route('/articles/maintain')
@login_required
def maintain_articles():
    recent_articles = article.get_last(4)
    open_edits = article.get_open_edits()
    open_to_review = article.get_open_to_review()
    released = article.get_all_released()
    archived_articles = article.get_all_archived()
    archived_edits = None
    return render_template(
        template_name_or_list=f'maintenance/articles.html', 
        recent_articles=recent_articles,
        open_edits = open_edits,
        open_to_review = open_to_review,
        released = released,
        archived_edits = archived_edits,
        archived_articles = archived_articles,
    )


@blueprint.route('/update/profile',methods=['GET','POST'])
@login_required
def update_profile():
    recent_articles = article.get_last(4)
    profile_form = UpdateProfile()
    if profile_form.validate_on_submit() and current_user.is_authenticated:
        if profile_form.image_file.data:
            image.delete(current_user.image_file, 'authors')
            current_user.image_file = image.save(profile_form.image_file.data, 'authors')
        profile.update(profile_form)
        flash('Profile updated','success')
        return redirect(url_for('maintenance.update_profile'))
    elif request.method == 'GET':
        profile_form = profile.update_form_data(profile_form)
    return render_template(
        template_name_or_list=f'maintenance/profile.html', 
        profile_form=profile_form,
        recent_articles=recent_articles
    )

@blueprint.route('/delete/update/<update_id>')
@login_required
def delete_update(update_id):
    update.delete(update_id)
    return redirect(url_for('navigation.index'))

@blueprint.route('/update/update/<update_id>', methods=['GET','POST'])
@login_required
def update_update(update_id):
    recent_articles = article.get_last(4)
    current_update = update.get(int(update_id))
    update_form = UpdatesForm()
    if update_form.validate_on_submit():
        update.update(update_form, current_update)
        return redirect(url_for('navigation.index'))
    elif request.method == 'GET':
        update_form = update.update_form_data(update_form, current_update)
    return render_template(
        template_name_or_list='maintenance/update.html', 
        update_form=update_form,
        recent_articles=recent_articles,
    )

@blueprint.route('/create/article', methods=['GET','POST'])
@login_required
def create_article():
    recent_articles = article.get_last(4)
    article_form = ArticleForm()
    if article_form.validate_on_submit():
        if article_form.image_file.data:
            image_file = image.save(article_form.image_file.data, 'articles')
        else:
            image_file = None
        edit = article.create(article_form, image_file)
        if  article_form.save.data:
            return redirect(url_for('maintenance.update_article', edit_id = edit.id))
        elif article_form.step_forward.data:
            article.ready_for_review(edit)
            flash('Article has been released for review.', 'success')
            return redirect(url_for('navigation_views.view', edit_id = edit.id))
    return render_template(
        template_name_or_list=f'articles/update.html', 
        article_form=article_form,
        current_article=None,
        status_message = 'Create a New Article',
        step_forward = True,
        recent_articles=recent_articles,
    )

@blueprint.route('/update/edit/<edit_id>', methods=['GET','POST'])
@login_required
def update_article(edit_id):    
    recent_articles = article.get_last(4)
    #TODO Update the get edit to look for the latest open
    current_edit = article.get_edit(id = edit_id)
    current_article = article.get_article(id=current_edit.article_id)
    article_form = ArticleForm()
    can_step_forward = current_article.author_id == current_user.id
    can_edit = current_edit.is_edited
    is_current_user = current_user.id == current_edit.user_id
    if not is_current_user and can_edit:
        article.freeze_edit(current_edit)
        current_edit = article.create_edit_existing(current_edit)
        return redirect(url_for('maintenance.update_article', edit_id=current_edit.id))
    if not can_edit:
        return redirect(url_for('navigation_views.view', edit_id = current_edit.id))
    if article_form.validate_on_submit():
        if article_form.image_file.data:
            image.delete(current_edit.image_file,'articles')
            current_edit.image_file = image.save(article_form.image_file.data, 'articles')
        if article_form.step_forward.data:
            article.update(article_form,current_edit)
            article.edit_is_ready_for_release(current_edit)
            flash('Article has been released for review','success')
            return redirect(url_for('maintenance.maintain_articles', edit_id = current_edit.id))
        elif article_form.save.data:
            article.update(article_form,current_edit)
            flash('Changes have been saved.','success')
            return redirect(url_for('maintenance.update_article', edit_id = current_edit.id))
    elif request.method == 'GET':
        article_form = article.update_form_data(article_form, current_edit)
    
    return render_template(
        template_name_or_list=f'articles/update.html', 
        article_form=article_form,
        current_article=None,
        status_message='Edit Article',
        step_forward = can_step_forward,
        recent_articles=recent_articles,
        image_file = current_edit.image_file,
    )

@blueprint.route('/archive/article/<article_id>')
@login_required
def archive_article(article_id):
    article.archive(article_id)
    flash('Archived article', 'success')
    return redirect(url_for('maintenance.maintain_articles'))

@blueprint.route('/unarchive/article/<article_id>')
@login_required
def unarchive_article(article_id):
    article.unarchive(article_id)
    flash('Article has been opened back for editing','success')
    return redirect(url_for('maintenance.maintain_articles'))

@blueprint.route('/suggestedit/<current_edit_id>')
@login_required
def suggest_edit(current_edit_id):
    current_edit = article.get_edit(current_edit_id)
    article.freeze_edit(current_edit)
    current_edit = article.create_edit_existing(current_edit)
    return redirect(url_for('maintenance.update_article', edit_id=current_edit.id))

@blueprint.route('/release/<current_edit_id>')
@login_required
def release_edit(current_edit_id):
    if not profile.all_access():
        flash('You are not authorized to release articles')
        return redirect(url_for('maintenance.maintain_articles', edit_id=current_edit_id))
    current_edit = article.get_edit(current_edit_id)
    article.freeze_edit(current_edit)
    article.release(current_edit)
    return redirect(url_for('navigation_views.view', edit_id=current_edit.id))

@blueprint.route('/read/messages')
@login_required
def read_messages():
    recent_articles = article.get_last(4)
    read_messages = messages.get_read()
    unread_messages = messages.get_unread()
    return render_template(
        template_name_or_list=f'maintenance/messages.html', 
        recent_articles=recent_articles,
        read_messages=read_messages,
        unread_messages=unread_messages,
    )


from flask import Blueprint, render_template, url_for, redirect, flash, request
from chrissmit.forms.content import UpdateProfile, UpdatesForm, ArticleForm
from chrissmit import db
from chrissmit.services import profile, article, update
from flask_login import current_user, login_required

blueprint = Blueprint('maintenance', __name__, template_folder='templates')

@blueprint.route('/update/profile',methods=['GET','POST'])
@login_required
def update_profile():
    profile_form = UpdateProfile()
    if profile_form.validate_on_submit() and current_user.is_authenticated:
        profile.delete_current_picture()
        profile.save_picture(profile_form.image_file.data)
        profile.update(profile_form)
        flash('Profile updated','success')
        return redirect(url_for('maintenance.update_profile'))
    elif request.method == 'GET':
        profile_form = profile.update_form_data(profile_form)
    return render_template(
        template_name_or_list=f'maintenance/profile.html', 
        profile_form=profile_form,
    )

@blueprint.route('/delete/update/<update_id>')
@login_required
def delete_update(update_id):
    update.delete(update_id)
    return redirect(url_for('navigation.index'))

@blueprint.route('/update/update/<update_id>', methods=['GET','POST'])
@login_required
def update_update(update_id):
    current_update = update.get(int(update_id))
    update_form = UpdatesForm()
    print(current_update)
    if update_form.validate_on_submit():
        update.update(update_form, current_update)
        return redirect(url_for('navigation.index'))
    elif request.method == 'GET':
        update_form = update.update_form_data(update_form, current_update)
    return render_template('maintenance/update.html', update_form=update_form)

@blueprint.route('/create/article', methods=['GET','POST'])
@login_required
def create_article():
    article_form = ArticleForm()
    if article_form.validate_on_submit():
        edit = article.create(article_form)
        if  article_form.save.data:
            return redirect(
                url_for('maintenance.update_article', edit_id = edit.id)
            )
        elif article_form.step_forward.data:
            article.ready_for_review(edit)
            flash('Article has been released.', 'success')
    return render_template(
        template_name_or_list=f'maintenance/article.html', 
        article_form=article_form,
        current_article=None,
        status_message = 'Create a New Article',
    )

@blueprint.route('/update/articles/<edit_id>', methods=['GET','POST'])
@login_required
def update_article(edit_id):
    article_form = ArticleForm()
    #TODO Update the get edit to look for the latest open
    current_edit = article.get_edit(id = edit_id)
    current_article = article.get(id=current_edit.article_id)
    
    #If you step an article forward, you will change the status 
    if article_form.validate_on_submit() and article_form.step_forward.data:
        article.edit_is_ready_for_release(current_edit, article_form)
        flash('Article has been released for review','success')
        #TODO Add different redirect
        return redirect(url_for('navigation.index'))

    #If you access a closed article, you will create a new edit
    elif current_article.is_released or current_edit.is_ready_for_release:
        article.freeze_edit(current_edit)
        current_edit = article.create_edit_existing(current_edit)
        return redirect(url_for('maintenance.update_article', edit_id=current_edit.id))
    
    #Populate the form for the appropriate article  
    elif request.method == 'GET':
        article_form = article.update_form_data(article_form, current_edit)
    
    return render_template(
        template_name_or_list=f'maintenance/article.html', 
        article_form=article_form,
        current_article=None,
        status_message='Edit article.',
        step_forward_action = 'next_action',
        step_forward = True
    )


@blueprint.route('/read/messages')
@login_required
def read_messages():
    profile_form = UpdateProfile()
    profile_form.email.data = current_user.full_name
    return render_template(
        template_name_or_list=f'maintenance/profile.html', 
        profile_form=profile_form,
        )


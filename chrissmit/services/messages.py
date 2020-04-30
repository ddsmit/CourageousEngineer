from chrissmit.services.db_models import Messages, Read, Reasons
from chrissmit import db
from flask_login import current_user

def save(form):
    new_message = Messages(
        name = form.name.data,
        email = form.email.data,
        reason = form.reason.data,
        content = form.content.data,
    )
    db.session.add(new_message)
    db.session.commit()

def mark_read(message_id):
    new_read = Read(
        message_id = message_id,
        user_id = current_user.id,
    )
    db.session.add(new_read)
    db.session.commit()

def get_read():
    return Messages.query.filter(
        Messages.id == Read.message_id,
    ).all()

def get_unread():
    return Messages.query.filter(
        Messages.id != Read.message_id,
    ).all()

def get_reasons():
    reasons = Reasons.query.all() 
    return [
        (str(reason.id), reason.desc)
        for reason in reasons
    ]

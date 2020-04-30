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
    message_read = Read.query.filter(
        Read.message_id == int(message_id),
        Read.user_id == current_user.id,
    ).first()

    if not message_read:
        new_read = Read(
            message_id = message_id,
            user_id = current_user.id,
        )
        db.session.add(new_read)
        db.session.commit()
        return False
    else:
        return True

def get_message(message_id):
    full_message = full_message_data()
    return full_message.filter(
        Messages.id == int(message_id)
    ).first()

def get_read():
    full_message = full_message_data()
    user_read = user_read_data()
    return full_message.filter(
        Messages.id.in_(user_read),
    ).all()

def get_unread():
    full_message = full_message_data()
    user_read = user_read_data()
    return full_message.filter(
        ~Messages.id.in_(user_read),
    ).all()

def get_reasons():
    reasons = Reasons.query.all() 
    return [
        (str(reason.id), reason.desc)
        for reason in reasons
    ]

def user_read_data():
    return db.session.query(
        Read.message_id
        ).filter(
        Read.user_id == current_user.id
    )

def full_message_data():
    return db.session.query(
        Messages.id,
        Messages.name,
        Messages.email,
        Messages.content,
        Reasons.desc, 
    ).join(
        Reasons,
        Reasons.id == Messages.reason,
    )
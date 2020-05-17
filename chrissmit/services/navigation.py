from chrissmit.services import profile, article, update, messages

def data():
    return {
        'articles':article.get_last(4),
        'authors':profile.get_all(),
    }
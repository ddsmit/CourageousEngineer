articles = [
    {
        'title': 'Building a Legacy',
        'author': 'The Hubby',
        'page': 'building',
        'preview': 'It starts as a gift...',
        'content': """
        On Christmas, 2019, this site will be handed over to Chris Smit as a Christmas gift from me, "The Hubby". 
        I wanted to build this site to provide a platform for my wife to share her experiences as a strong, kind, beautiful
        black woman in Engineering. She has so many stories to tell, and I am so excited for her to share them with the world!
        """,
        'posted': '12/6/2019',
        'edited': None,
    },
    {
        'title':'Accentuating Accents',
        'author': 'Christine Smit',
        'page':'accentuatingaccents',
        'preview':'The subtle racism you face.',
        'content':'words words words',
        'posted':'today',
        'edited':'today',
    },
]
def get_last_four_articles():
    return articles[-4:]

def get_article_data(page):
    for article in articles:
        if page == article['page']:
            return article
    return {}

def get_all_articles():
    return articles
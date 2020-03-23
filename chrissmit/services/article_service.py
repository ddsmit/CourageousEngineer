articles = [
    {
        'title': 'Building a Legacy',
        'author': 'hubby',
        'page': 'building',
        'preview': 'It starts as a gift...',
        'content': """
        On Christmas, 2019, this site will be handed over to Chris Smit as a Christmas gift from me, the hubby. 
        I wanted to build this site to provide a platform for my wife to share her experiences as a strong, kind, beautiful
        black woman in Engineering. She has so many stories to tell, and I am so excited for her to share them with the world.
        The site is still in its very early stages, but expect major changes in the first month of 2020. See you next year!
        """,
        'posted': '12/6/2019',
        'edited': None,
        'image':'static/img/stories/gift-svgrepo-com.xml',
    },
    {
        'title': 'Actenuating Accents',
        'author': 'Yolanda Smit',
        'page': 'accents',
        'preview': "It's hard to listen when all you do is hear...",
        'content': """
        On Christmas, 2019, this site will be handed over to Chris Smit as a Christmas gift from me, the hubby. 
        I wanted to build this site to provide a platform for my wife to share her experiences as a strong, kind, beautiful
        black woman in Engineering. She has so many stories to tell, and I am so excited for her to share them with the world.
        The site is still in its very early stages, but expect major changes in the first month of 2020. See you next year!
        """,
        'posted': '12/6/2019',
        'edited': None,
        'image':'static/img/stories/aa.xml'
    },
    {
        'title': 'Building a Legacy',
        'author': 'hubby',
        'page': 'building',
        'preview': 'It starts as a gift...',
        'content': """
    On Christmas, 2019, this site will be handed over to Chris Smit as a Christmas gift from me, the hubby. 
    I wanted to build this site to provide a platform for my wife to share her experiences as a strong, kind, beautiful
    black woman in Engineering. She has so many stories to tell, and I am so excited for her to share them with the world.
    The site is still in its very early stages, but expect major changes in the first month of 2020. See you next year!
    """,
        'posted': '12/6/2019',
        'edited': None,
        'image': 'static/img/stories/gift-svgrepo-com.xml',
    },
    {
        'title': 'Actenuating Accents',
        'author': 'Yolanda Smit',
        'page': 'accents',
        'preview': "It's hard to listen when all you do is hear...",
        'content': """
    On Christmas, 2019, this site will be handed over to Chris Smit as a Christmas gift from me, the hubby. 
    I wanted to build this site to provide a platform for my wife to share her experiences as a strong, kind, beautiful
    black woman in Engineering. She has so many stories to tell, and I am so excited for her to share them with the world.
    The site is still in its very early stages, but expect major changes in the first month of 2020. See you next year!
    """,
        'posted': '12/6/2019',
        'edited': None,
        'image': 'static/img/stories/aa.xml'
    },
    {
        'title': 'Building a Legacy',
        'author': 'hubby',
        'page': 'building',
        'preview': 'It starts as a gift...',
        'content': """
    On Christmas, 2019, this site will be handed over to Chris Smit as a Christmas gift from me, the hubby. 
    I wanted to build this site to provide a platform for my wife to share her experiences as a strong, kind, beautiful
    black woman in Engineering. She has so many stories to tell, and I am so excited for her to share them with the world.
    The site is still in its very early stages, but expect major changes in the first month of 2020. See you next year!
    """,
        'posted': '12/6/2019',
        'edited': None,
        'image': 'static/img/stories/gift-svgrepo-com.xml',
    },
    {
        'title': 'Actenuating Accents',
        'author': 'Yolanda Smit',
        'page': 'accents',
        'preview': "It's hard to listen when all you do is hear...",
        'content': """
    On Christmas, 2019, this site will be handed over to Chris Smit as a Christmas gift from me, the hubby. 
    I wanted to build this site to provide a platform for my wife to share her experiences as a strong, kind, beautiful
    black woman in Engineering. She has so many stories to tell, and I am so excited for her to share them with the world.
    The site is still in its very early stages, but expect major changes in the first month of 2020. See you next year!
    """,
        'posted': '12/6/2019',
        'edited': None,
        'image': 'static/img/stories/aa.xml'
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
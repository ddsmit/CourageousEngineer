authors = [
    {
        'name': 'Yolanda Smit',
        'alias': 'Chris Smit',
        'twitter_handle': '@yoyosmit',
        'image': 'static/img/yoyo.xml',
        'content': """
        This area is under construction. I could say a lot about Chris Smit, but I think it would be best to let the lady herself
        be the one to lay it out for you.
        This area is under construction. I could say a lot about Chris Smit, but I think it would be best to let the lady herself
        be the one to lay it out for you.
        This area is under construction. I could say a lot about Chris Smit, but I think it would be best to let the lady herself
        be the one to lay it out for you.
        This area is under construction. I could say a lot about Chris Smit, but I think it would be best to let the lady herself
        be the one to lay it out for you.
        This area is under construction. I could say a lot about Chris Smit, but I think it would be best to let the lady herself
        be the one to lay it out for you.
        This area is under construction. I could say a lot about Chris Smit, but I think it would be best to let the lady herself
        be the one to lay it out for you.
        This area is under construction. I could say a lot about Chris Smit, but I think it would be best to let the lady herself
        be the one to lay it out for you.
        """,
        'joined': '12/6/2019',
        'edited': None,
    },
    {
        'name': 'David Smit',
        'twitter_handle': '@davidouglasmit',
        'image': 'static/img/dave.xml',
        'content': """
        I am a mechanical engineer by trade and education, but I love all types of engineering and problem solving.
        I started learning Python to be more effective with my analysis at work, and I fell in love with the language. 
        Now I'm trying to get a handle on various front and back-end technologies for the web as well as various 
        computer science concepts. 
        """,
        'joined': '12/6/2019',
        'edited': None,
    },
]

def get_author_data(page):
    for author in authors:
        if page == author['page']:
            return author
    return {}

def get_all_authors():
    return authors

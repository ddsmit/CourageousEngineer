

def get_last_four_articles():
    return None

def get_article_data(page):
    for article in articles:
        if page == article['page']:
            return article
    return {}

def get_all_articles():
    return articles
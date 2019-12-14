def register(app):
    from chrissmit.views import user_views
    from chrissmit.views import article_views
    from chrissmit.views import navigation_views
    app.register_blueprint(navigation_views.blueprint)
    app.register_blueprint(article_views.blueprint)
    app.register_blueprint(user_views.blueprint)
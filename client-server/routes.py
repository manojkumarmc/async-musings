from views import index, index_param

def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/{name}', index_param)


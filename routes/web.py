from masonite.routes import Route
from masonite.authentication import Auth

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.get('/create', 'PostController@create_post'),
    Route.post('/create', 'PostController@save_post'),
    Route.get('/read/@id', 'PostController@read_post'),
    Route.get('/post/@id/update', 'PostController@update_post'),
    Route.post('/post/@id/update', 'PostController@save_update'),
    Route.get('/post/@id/delete', 'PostController@delete_post'),
    ]
ROUTES += Auth.routes()
"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller
from app.models.Post import Post

class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        posts = Post.all()
        return view.render("welcome", {"posts": posts})

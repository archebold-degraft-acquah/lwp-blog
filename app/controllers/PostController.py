from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from app.models.Post import Post
from masonite.authentication import Auth
from masonite.response import Response
from masonite.sessions import Session


class PostController(Controller):
    def create_post(self, response: Response, auth: Auth, view: View):
        if auth.user():
            return view.render("create")
        else:
            return response.redirect('/login')

    def save_post(self, response: Response, request: Request, view: View):
        Post.create(
        title = request.input('title'),
        body = request.input('body'),
        author_id = request.user().id
        )
        return response.redirect('/').with_success("Your Post has been published successfully")

    def read_post(self, request: Request, view: View):
        post = Post.find(request.param('id'))
        return view.render('read', {'post': post, "num_reads": num_reads})

    def update_post(self, response: Response, request: Request, view: View):
        post = Post.find(request.param('id'))
        return view.render('update', {'post': post})


    def save_update(self, auth: Auth, request: Request, response: Response, view: View):
        post = Post.find(request.param('id'))
        post.title = request.input('title')
        post.body = request.input('body')
        if auth.user() == post.author:
            post.save()
            return response.redirect('/').with_success("Post updated successfully")
        else:
            return response.status(403, "You are not the author of this post. You can't update it!")


    def delete_post(self, auth: Auth, response: Response, request: Request, view: View):
        post = Post.find(request.param('id'))
        post.delete()
        return response.redirect('/').with_success("Your Post has been deleted successfully")


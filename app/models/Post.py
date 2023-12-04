""" Post Model """
from masoniteorm.relationships import belongs_to
from masoniteorm.models import Model


class Post(Model):
    """Post Model"""
    __table__ = 'posts'
    __fillable__ = ['title', 'author_id', 'body']
    @belongs_to('author_id', 'id')
    def author(self):
        from app.models.User import User
        return User



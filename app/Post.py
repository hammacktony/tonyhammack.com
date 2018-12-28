''' A Post Database Model '''
from orator.orm import belongs_to, scope

from app.User import User
from config.database import Model


class Post(Model):
    
    __connection__ = 'connection_2'

    __fillable__ = ['title',
                    'author_id',
                    'body',
                    'category',
                    'slug',
                    'image',
                    'is_live']

    @belongs_to('author_id', 'id')
    def author(self):
        return User

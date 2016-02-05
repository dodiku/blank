from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]

class Post(models.Model):
    user = models.ForeignKey(User)
    i_am = models.CharField(max_length=50)
    i_want = models.CharField(max_length=50)
    i_need = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    chats = models.IntegerField(default=0)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return self.i_need

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username

from django.db import models
from apps.login.models import User

class Message(models.Model):
    message = models.CharField(max_length = 1200)
    users = models.ForeignKey(User, related_name="messages")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment = models.CharField(max_length = 1200)
    messages = models.ForeignKey(Message, related_name="comments")
    users = models.ForeignKey(User, related_name="comments")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
    user = models.ForeignKey(User, related_name="likes")
    message = models.ForeignKey(Message, related_name="likes", null = True)
    comment = models.ForeignKey(Comment, related_name="likes", null = True)
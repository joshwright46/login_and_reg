from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.wall),
    url(r'^post_msg$', views.post_msg),
    url(r'^post_cmt$', views.post_cmt),
    url(r'^(?P<message_id>\d+)/delete_message$', views.delete_message),
    url(r'^(?P<comment_id>\d+)/delete_comment$', views. delete_comment),
    url(r'^(?P<message_id>\d+)/like_message$', views.like_message),
    url(r'^(?P<comment_id>\d+)/like_comment', views.like_comment)
]
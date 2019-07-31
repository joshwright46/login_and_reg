from django.shortcuts import render, redirect
from apps.login.models import User
from .models import Message
from .models import Comment
from .models import Like
import datetime

def wall(request):
    user = User.objects.get(id = request.session['current_user_id'])
    all_messages = Message.objects.all()
    all_comments = Comment.objects.all()
    all_likes = Like.objects.all()
    # now = datetime.datetime.now()

    context = {
        'user':user,
        'all_messages': all_messages,
        'all_comments': all_comments,
        'all_likes' : all_likes

        # 'now': now
    }
    return render(request, 'wall.html', context)

def post_msg(request):
    user = User.objects.get(id = request.session['current_user_id'])
    Message.objects.create(message = request.POST['message'], users = user )
    return redirect('/wall')

def post_cmt(request):
    user = User.objects.get(id = request.session['current_user_id'])
    print ('*' * 50)
    print(user)
    
    message = Message.objects.get(id = request.POST['msg_id'])
    print ('*' * 50)
    print(message)

    Comment.objects.create(comment = request.POST['comment'], messages = message, users = user)
    return redirect('/wall')

def delete_message(request, message_id):
    delete_message = Message.objects.get(id = message_id)
    delete_message.delete()
    return redirect('/wall')

def delete_comment(request, comment_id):
    delete_comment = Comment.objects.get(id = comment_id)
    delete_comment.delete()
    return redirect('/wall')

def like_message(request, message_id):
    user = User.objects.get(id = request.session['current_user_id'])
    message = Message.objects.get(id = message_id)
    Like.objects.create(user = user, message = message)
    return redirect('/wall')

def like_comment(request, comment_id):
    user = User.objects.get(id = request.session['current_user_id'])
    comment = Comment.objects.get(id = comment_id)
    Like.objects.create(user = user, comment = comment)
    return redirect('/wall')




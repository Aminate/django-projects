from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.decorators import api_view  #это - функции, чтобы отвечала на запросы
from rest_framework.response import Response   # это - чтобы получать ответ на запрос
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404  # это - для того чтоб вытыщить обьект, а если нет то ошибка 404 
#нихуя не понялa

from .models import Like
from post.models import Post, User
from .models import Comment
from .serializers import CommentSerializer


@api_view(['POST'])
def toggle_like(request, id): # id -post
    user = request.user
    if not user.is_authenticated:
        return Response(status=401)
    # user_id = request.data.get('user')
    # if not user_id:   #user_id = None
    #     return Response({"user":["this field is required"]}, status=400)
    # user = get_object_or_404(User, id=user_id)
    post = get_object_or_404(Post, id=id)
    if Like.objects.filter(user=user, post=post).exists():  
         #exists-проверяет сущ ли запись, (если лайк есть то удаляем его)
        Like.objects.filter(user=user, post=post).delete()
    else:
        # если нет, то создаем
        Like.objects.create(user=user, post=post)
    return Response(status=201)



# @api_view(['POST'])
# def toggle_comment(request, id):
#     user_id = request.data.get('user')
#     if not user_id:   #user_id = None
#         return Response({"user":["this field is required"]}, status=400)
#     user = get_object_or_404(User, id=user_id)
#     post = get_object_or_404(Post, id=id)
#     Comment.objects.create(user=user, post=post)
#     return Response(status=201)

    
@api_view(['POST'])
def toggle_comment(request, id):
    print(request.data)
    user_id = request.data.get('user')
    text = request.data.get('text')
    post = get_object_or_404(Post, id=id)
    user = get_object_or_404(User, id=user_id)
    serializer = CommentSerializer(post, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    Comment.objects.create(user=user, post=post, text=text)
    return Response(serializer.data, status=201)



class CreateCommentAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class UpdateCommentAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class DeleteCommentAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


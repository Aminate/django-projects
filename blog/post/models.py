from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
#работа с базой данных тут:
User = get_user_model()



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)     #CharField-тип данных(строка)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)       #когда создавалась



from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# [Django] 관계를 표현하는 모델 필드, ForeignKey,OneToOneField,ManyToManyField
# https://ssungkang.tistory.com/entry/Django-%EA%B4%80%EA%B3%84%EB%A5%BC-%ED%91%9C%ED%98%84%ED%95%98%EB%8A%94-%EB%AA%A8%EB%8D%B8-%ED%95%84%EB%93%9C-ForeignKeyOneToOneFieldManyToManyField
# https://velog.io/@bungouk6829/Django-%EB%AA%A8%EB%8D%B8%EC%9D%98-%ED%95%84%EB%93%9C-%EA%B4%80%EA%B3%84%ED%98%95-%ED%95%84%EB%93%9C
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/',null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)
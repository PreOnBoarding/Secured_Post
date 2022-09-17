from django.db import models

# Create your models here.

class Post(models.Model):
    """
    게시글에 해당하는 모델
    """
    title = models.CharField("제목", max_length=20)
    content = models.TextField("내용", max_length=200)
    password = models.CharField("비밀번호", max_length=200)
    created_date = models.DateTimeField("게시글 등록 일자", auto_now_add=True)
    update_date = models.DateTimeField("게시글 수정 일자", auto_now=True)

    def __str__(self):
        return self.title


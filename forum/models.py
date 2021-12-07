from django.db import models
from account.models import User


class Thread(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='작성자')
    nickname = models.CharField(default="", max_length=16, verbose_name='닉네임')
    password = models.CharField(default="", max_length=16, verbose_name='비밀번호')
    title = models.CharField(default="", max_length=60, verbose_name='제목')
    contents = models.TextField(default="", verbose_name='내용')
    tags = models.TextField(default="", verbose_name='태그')
    is_sticky_thread = models.BooleanField(default=False, verbose_name='주게시물 여부')
    view_count = models.IntegerField(default=0, verbose_name='노출 수')
    #like_count = models.IntegerField(default=0, verbose_name='좋아요')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='수정일')

    def __str__(self):
        return f'{self.author} / {self.title} / {self.is_sticky_thread} / {self.tags} / {self.contents}'


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, verbose_name='본게시물')
    nickname = models.CharField(default="", max_length=16, verbose_name='닉네임') 
    password = models.CharField(default="", max_length=16, verbose_name='비밀번호')
    message = models.TextField(default="", max_length=300, verbose_name='댓글')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='수정일')

    def __str__(self):
        return f'{self.author.id} / {self.thread.id} / {self.message}'


class TagDictionary(models.Model):
    tag = models.CharField(max_length=100, verbose_name='태그')
    synonyms = models.TextField(default="", verbose_name='비슷한 태그')
    associated_words = models.TextField(default="", verbose_name='연관 태그')
    hit_count = models.IntegerField(default=0, verbose_name='클릭 횟수')
    search_count = models.IntegerField(default=0, verbose_name='검색 횟수')
    register_count = models.IntegerField(default=1, verbose_name='등록 횟수')
    def __str__(self):
        return f'{self.tag} / {self.hit_count} / {self.search_count}'


class TagThreadMap(models.Model):
    tag = models.ForeignKey(TagDictionary, on_delete=models.CASCADE, verbose_name='태그')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, verbose_name='게시물')


class LikeMap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='좋아요를 누른 사람')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, verbose_name='좋아요를 받은 게시물')
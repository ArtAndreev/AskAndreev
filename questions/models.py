from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse, get_object_or_404

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    rating = models.IntegerField(default=0)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name()


class Tag(models.Model):
    label = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.label


class Question(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)


class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField(default=False)


class Like(models.Model):
    type = models.IntegerField(default=0)


class QuestionLike(Like):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class AnswerLike(Like):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

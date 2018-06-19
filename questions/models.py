from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse, get_object_or_404

# Create your models here.


class QuestionManager(models.Manager):
    def get_hot(self):
        return self.order_by('-rating')

    def get_last(self):
        return self.order_by('-pub_date')

    def get_by_tag(self, tag):
        return self.filter(tags__label__iexact=tag).order_by('-pub_date')


class AnswerManager(models.Manager):
    def get_answers(self, question_id):
        return self.filter(question__id__exact=question_id).order_by('-rating',
                                                                     '-pub_date')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='user_profile')
    rating = models.IntegerField(default=0)
    avatar = models.ImageField(blank=True)
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

    objects = QuestionManager()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField(default=False)

    objects = AnswerManager()


class Like(models.Model):
    type = models.IntegerField(default=0)


class QuestionLike(Like):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('question', 'user')


class AnswerLike(Like):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('answer', 'user')

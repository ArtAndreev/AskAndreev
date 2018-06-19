from django.core.management.base import BaseCommand
from questions.models import Question, Tag, Answer, UserProfile, User


class Command(BaseCommand):
    help = 'Fills the database with testing data.'

    def execute(*args, **options):
        for i in range(5):
            user = User.objects.create(username='User{0}'.format(i), password='abacaba')
            UserProfile.objects.create(user=user)

        for i in range(7):
            Tag.objects.create(label='Tag{0}'.format(i))

        for i in range(50):
            print('id={0}'.format(i % 5))
            author = UserProfile.objects.get(user__username__exact='User{0}'.format(i % 5))
            new_question = Question.objects.create(
                title='Question title {0}.'.format(i),
                text='Question text {0}.'.format(i),
                rating=(i - 25),
                author=author
            )
            tag1 = Tag.objects.get(label__exact='Tag{0}'.format(i % 7))
            tag2 = Tag.objects.get(label__exact='Tag{0}'.format((i + 3) % 7))
            tag3 = Tag.objects.get(label__exact='Tag{0}'.format((i + 5) % 7))
            new_question.tags.add(tag1, tag2, tag3)

        for i in range(20):
            author = UserProfile.objects.get(user__username__exact='User{0}'.format((25 - i) % 5))
            question = Question.objects.get(title__exact='Question title {0}.'.format(49 - i))
            Answer.objects.create(text='Good answer {0}'.format(i),
                                  author=author,
                                  rating=i % 10 - 5,
                                  is_correct=bool(i % 5 % 2),
                                  question=question
                                  )



from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.questions_list, name='questions_list'),
    url(r'^hot/', views.hot_list, name='hot_list'),
    url(r'^question/(?P<question_id>[0-9]+)', views.question, name='question'),
    url(r'^ask/', views.ask_question, name='ask_question'),
    url(r'^tag/(?P<tag_name>\w+)', views.tag_list, name='tag_list'),
    url(r'^login/', views.user_login, name='user_login'),
    url(r'^settings/', views.user_settings, name='user_settings'),
    url(r'^signup/', views.user_signup, name='user_signup'),
]

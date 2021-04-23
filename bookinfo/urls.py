from rest_framework.routers import DefaultRouter
from bookinfo.views import BookViewSet

router = DefaultRouter()

router.register(r'book', BookViewSet, basename='book')




class Student:
    def __init__(self, name):
        self.Name = name
s1 = Student(name='abc')
s2 = Student(name='pqr')
s3 = Student(name='xyz')


from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
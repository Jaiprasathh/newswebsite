from django.urls import path
from news import views


urlpatterns=[
    path("", views.main, name="main"),
    path('category/<cname>/', views.post_by_category, name='post_by_category'),
    path('article/<slug>/', views.single_article, name="single_article"),
    path('register/', views.register, name='register')
]
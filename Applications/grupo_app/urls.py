from django.urls import path, include
from . import views
urlpatterns = [
    path('rxheader/', views.RxHeader.as_view()),
    path('rxheader2/', views.RxHeader2.as_view()),
]

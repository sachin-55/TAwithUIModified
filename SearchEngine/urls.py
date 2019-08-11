from django.urls import path

from . import views

urlpatterns = [
    path('result/',views.searchView,name='search'),
    path('feedback/',views.feedbackView,name='feedback'),

]
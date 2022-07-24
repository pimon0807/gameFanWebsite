from . import views
from django.urls import path


app_name = 'gameFanWebsite'
urlpatterns = [
    path('', views.indexView, name="index"),
    path('rules/', views.rulesView, name="rules"),
    path('notables/<int:notableIndex>/', views.notablesDetail, name="notablesDetail.html"),
    path('notables/', views.notablesList, name="notablesList"),
    path('externalLinks/', views.externalLinks, name="externalLinks"),
]
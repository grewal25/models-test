from django.urls import path

from . import views
app_name='likes'
urlpatterns=[
    path('', views.home, name='home'),
    path('<int:person_id>/', views.detail, name='likes-detail'),



]

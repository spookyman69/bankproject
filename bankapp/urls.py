from django.urls import path
from bankapp import views

app_name = 'bank'
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('application', views.application, name='application'),
    path('logout',views.logout, name='logout')
]

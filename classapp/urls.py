from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('logout', views.logout_user, name='logout_user'),
    path('login', views.login_user, name='login_user'),
    path('register', views.register, name='register'),
    path('meeting', views.meeting, name='meeting'),
    path('joinroom', views.joinroom, name='joinroom'),
    path('post', views.allpost, name='allpost'),
    path('post/<int:pk>', views.postview, name='postview'),
    path('comment', views.comment, name='comment'),
      
]

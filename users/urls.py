from django.contrib.auth import views
from django.urls import path
from .views import profile, RegisterDoneView, RegisterUserView

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('register', RegisterUserView.as_view(),
         name='register'),
    path('register/done/', RegisterDoneView.as_view(),
         name='register_done')
]
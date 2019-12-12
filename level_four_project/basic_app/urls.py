from django.urls import path
from . import views

#TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('index/', views.index, name = "index"),
    path('other/', views.other, name = 'other'),
    path('relative/', views.relative, name = "relative"),
    path('register/', views.register, name = "register"),
    path('user_login/', views.user_login, name = "user_login")
]
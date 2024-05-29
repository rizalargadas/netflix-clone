from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name="index"),
    path('success/', views.success, name="success"),
    path('signup/', views.signup, name="signup"),
    # path('signin/', views.signin, name="signin"),
]

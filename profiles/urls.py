from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('choose_profile/', views.choose_profile, name="choose_profile"),
    path('manage_profiles/', views.manage_profiles, name="manage_profiles"),
    path('add_profile/', views.add_profile, name="add_profile"),
    path('edit_profile/<int:pk>/', views.edit_profile, name="edit_profile"),
    path('delete_profile/<int:pk>/', views.delete_profile, name="delete_profile"),
    path('profile_lock/<int:pk>/', views.profile_lock, name="profile_lock"),
    path('check_profile_lock/<int:pk>/',
         views.check_profile_lock, name="check_profile_lock"),
]

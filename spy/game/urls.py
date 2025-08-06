from django.urls import path, include
from . import views

app_name = 'game'
urlpatterns = [
    path("", views.setup_view, name='setup'),
    path("names/", views.names_view, name='names'),
    path("roles/", views.role_reveal_view, name='role_reveal'),
    path("timer/", views.timer_view, name='timer'),
    path('game-over/', views.game_over_view, name='game_over'),
    path('restart/', views.restart_game_view, name='restart_game'),
]

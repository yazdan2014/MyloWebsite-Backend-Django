
from django.urls import path

from . import views

urlpatterns = [
    path('commands/', views.commands),
    path('commands/<int:id>', views.commandsid),

    path('articles/', views.articles),

    path("dashboard/", views.dashboard_view)
]

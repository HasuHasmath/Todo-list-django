# Correct import statement to import views from the todo app
from todo import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', views.index, name="todo"),
    path('del/', views.remove, name="del"),  # Adjusted URL pattern
    path('admin/', admin.site.urls),
]

"""
URL configuration for homework_07 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import main.views as main

urlpatterns = [
    path('main/videos/list/', main.get_videos_list),
    # path('main/videos/<int:video_id>/', main.get_video_details),
    path('main/videos/add/', main.create_new_video),
    # path('videos//<int:video_id>/confirm-delete/', main.confirm_delete_video),
    path('main/', main.index),
    path('admin/', admin.site.urls),
]

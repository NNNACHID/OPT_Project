"""
URL configuration for MainApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include


urlpatterns = [
    # path("", users_views.index, name="home"),
    # path("registration/", users_views.add_user, name="registration"),
    # path("delete_user/<int:user_pk>/", users_views.delete_user, name="delete_user"),
    # path("get_users/<int:category_pk>/", users_views.get_users, name="users"),
    path("users/", include("Users.urls")),
    path("admin/", admin.site.urls),
]

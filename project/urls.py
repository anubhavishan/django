"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views
from django.contrib.auth.views import LoginView
from tweet.views import home 
from tweet import views



urlpatterns = [
    path('tweet/', views.tweet_list, name='tweet_list'),
    path('', views.create_tweet, name='create_tweet'),
    path('', home, name='home'), 
    path('admin/', admin.site.urls),
    path('tweet/', include('tweet.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







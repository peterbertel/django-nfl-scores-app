"""bertel_capstone_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from nfl_scores import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.ScoresView.as_view(), name="scores"),
    url(r'^standings/$', views.standings, name="standings"),
    url(r'^get_games/$', views.get_games, name="get_games"),
    url(r'^load_all_games/$', views.load_all_games, name="load_all_games"),
    url(r'^load_sportradar_data/$', views.load_sportradar_data, name="load_sportradar_data"),
]

"""
URL configuration for AMRSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf import settings

import adcrawls.views
import miscpages.views
import songrequests.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("adcrawls/<int:id>/content.txt", adcrawls.views.getcrawlcontent, name="getcrawlcontent"),
    path("adcrawls/<int:id>.json", adcrawls.views.detailjson, name="detailjson"),
    path("", miscpages.views.home, name="home"),
    path(".well-known/gpc.json", miscpages.views.gpc, name="gpc"),
    path("about/", miscpages.views.about, name="about"),
    path("request-song/", songrequests.views.request_song, name="request_song"),
]

admin.site.site_header = f'{settings.APP_NAME} Administration'
admin.site.site_title = f'{settings.APP_NAME} Administration'
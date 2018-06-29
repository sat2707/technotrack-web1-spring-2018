"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
import users.urls
import reports.urls
from users.views import login_form, logout_view

from reports.views import all_categories

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login_form),
    url(r'^logout/$', logout_view),
    url(r'^users/', include(users.urls, namespace='users')),
    url(r'^reports/', include(reports.urls, namespace='reports')),
    # url(r'^', include(application.mainpage, namespace='main'))
    url(r'^$', all_categories, name='main')
]



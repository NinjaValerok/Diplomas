"""diplomas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')f
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from input_matrix_web import views as inmatweb
from load_matrix import views as load
from diplomas.views import *
from forms.forms import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'set_sizes$', inmatweb.set_sizes),
    url(r'^set_matrix$', inmatweb.set_matrix),
    url(r'^load$', load.upload_file),
    url(r'^files/data.xls$', load.download_file),
    url(r'^data$', load.download_file),
    url(r'^$', start_view),
    url(r'accounts/login', LoginFormView.as_view()),
    url(r'accounts/logout', LogoutView.as_view()),
    url(r'accounts/register/', RegisterFormView.as_view()),
    url(r'^accounts/profile/$', profile),
    url(r'^download_PCA_file_by_id/(\d+)/$', download_PCA_file_by_id),
    url(r'^delete_file_by_id/(\d+)/$', delete_file_by_id),
]


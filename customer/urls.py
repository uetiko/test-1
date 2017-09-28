"""customer URL Configuration

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
from django.contrib.auth import views as auth_views
from users.views import HomeView
from users.views import DataView
from users.views import HomeLoginView
from users.views import DataAddView, DataUpdateView, DataDeleteView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^view/$', HomeLoginView.as_view(), name='login_home'),
    url(r'^costomer/data/$', DataView.as_view(), name='data_view'),
    url(r'^costomer/data/add/$', DataAddView.as_view(), name='add_client'),
    url(
        r'^costomer/data/update/(?P<clientid>\d+)/$',
        DataUpdateView.as_view(),
        name='update_client'
    ),
    url(
        r'^costomer/data/delete/(?P<clientid>\d+)/$',
        DataDeleteView.as_view(),
        name='delete_client'
    ),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {
        'template_name': 'logged_out.html',
        'next_page': '/'
    }, name='logout'),
    url(r'^admin/', admin.site.urls),
]

"""zinzi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from members import views
from reservations.views import reserve, reservation_complete
from restaurants import views as restaurant_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^restaurant/$', restaurant_view.restaurant_list, name='restaurant-list'),
    url(r'^restaurant/(?P<pk>\d+)/$', restaurant_view.restaurant_detail, name='restaurant-detail'),
    url(r'^reservation/(?P<info_pk>\d+)/$', reserve, name='reserve'),
    url(r'^reservation_complete/(?P<pk>\d+)$', reservation_complete),
]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)

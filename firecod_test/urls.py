"""firecod_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from shops import views
from shops import api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('city/', views.CityViewSet.as_view()),
    path('city/<int:city_id>/street/', views.StreetViewSet.as_view()),
    path('shop/', views.ShopViewSet.as_view({'post': 'create', 'get': 'list'})),
]
admin.site.index_title = "Test1"
admin.site.site_header = "Test2"
admin.site.site_title = "Test3"

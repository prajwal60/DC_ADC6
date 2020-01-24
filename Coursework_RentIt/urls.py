"""Coursework_RentIt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage, name="homepage"),
    path('login_form/',views.login_form),
    path('buyerregistration_form/',views.registration_form_of_buyer),
    path('again_to_login/',views.login_form),
    path('ownerregistration_form/',views.registration_form_of_owner),
    path('photoupload_form/',views.uploadphoto),
    path('Photo_upload_result/', views.uploadphoto),
    # path('searchdata/', views.homepage),
    path('update_form/<int:pk>/', views.update_form),
    path('update_form/update/<int:pk>/', views.update),
    path('delete/<int:pk>/', views.delete),
    path('search/', views.search),
    # path('seephoto/' ,views.seephoto ),
    # path('seephoto/<int:pk>/' ,views.seephoto ),
    # path('/<string:x.file.url>')




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

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
from django.urls import path
from app.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),

    #App
    path('', login_page, name="login_page"),  # Assuming login is the default page
    path('login/', login_page, name="login_page"),
    path('signup/', signup_page, name="signup_page"),
    path('user-records/<int:user_id>/', user_records, name='user_records_with_id'),
    path("delete_record/<int:record_id>/", delete_record, name="delete_record"),
    path("logout/", logout_page, name="logout_page")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




urlpatterns += staticfiles_urlpatterns()

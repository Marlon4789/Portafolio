"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from portafolio import views as portafolio
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('portafolio/', portafolio.portafolio, name='portafolio'),
    # api coffee store
    path('api_coffee_store/', include('api_coffee_store.urls')),
    # blog
    path('create_post/', views.model_form_view, name='create_post'),
    path('detail/<int:quillpost_id>/', views.quillpost_detail, name="detail"),
    path('show_all_posts/', views.show_all_post, name='show_all_posts'),
]

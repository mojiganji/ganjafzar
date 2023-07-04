
from django.contrib import admin
from django.urls import path, include
from ganjafzar import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('programming' , views.programming),
    path('artificial-intelligence' , views.artificial),
    path('data-maining' , views.data),
    path('machine-learning' , views.machine),
]



from django.contrib import admin
from django.urls import path, include
from ganjafzar import views
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings
#from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('programming' , views.programming),
    path('neural-network' , views.neural),
    path('data-maining' , views.data),
    path('machine-learning' , views.machine),
    path('accounts/' , include('accounts.urls')),
]


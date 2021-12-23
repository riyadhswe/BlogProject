from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('AppLogin.urls')),
    path('blog/', include('AppBlog.urls')),
    path('', views.Index, name='index')
]

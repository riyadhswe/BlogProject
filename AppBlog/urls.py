from django.urls import path
from . import views
app_name = "AppBlog"
urlpatterns = [
    path('',views.bloglist,name = 'bloglist')

]

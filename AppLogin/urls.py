from django.urls import path
from AppLogin import views
app_name = "AppLogin"

urlpatterns = [
    path('signup/',views.singup,name='sign_up')

]

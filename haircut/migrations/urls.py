from django.urls import path
from . import views 


app_name='hearcut'

urlpatterns=[
    path("", views.home_page, name='home_page'), 
] 


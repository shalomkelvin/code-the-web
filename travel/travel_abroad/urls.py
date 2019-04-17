from django.conf.urls import url
from travel_abroad import views

# template URLs

app_name = 'travel_abroad'

urlpatterns =[
     url(r'^register/$', views.register, name ='register'),
     url(r'^user_login/$', views.user_login, name='user_login'),
]

from django.urls import path

from 두산베어스 import views

app_name = '두산베어스'

urlpatterns = [
    path('/철원', views.show_철원, name='철원'),
    path('/의지', views.show_의지, name='의지'),
    path('/수빈', views.show_수빈, name='수빈')
]

from django.urls import include,path
from . import views






urlpatterns = [
    #path('',views.index, name='index')
    path('',views.ten_days,name='ten')
]


from django.urls import include,path
from . import views






urlpatterns = [
    #path('',views.index, name='index'),
    path('task/<str:task_id>/', views.TaskView.as_view(), name='task')
 
]

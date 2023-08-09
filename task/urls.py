from django.urls import path
from .views import TaskCreateApiView,TaskDeleteApiView,TaskDetailApiView,TaskUpdateApiView,TaskListApiView

urlpatterns=[

    path('all/',TaskListApiView.as_view()),
    path('get/<int:id>/',TaskDetailApiView.as_view()),
    path("delete/<int:id>/",TaskDetailApiView.as_view()),
    path('update/<int:id>/',TaskUpdateApiView.as_view()),
    path('create/',TaskCreateApiView.as_view())

]
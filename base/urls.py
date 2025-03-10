from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate,TaskUpdate, TaskDelete, CusomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',TaskList.as_view(), name="tasks"),
    path('register/',RegisterPage.as_view(), name="register", ),
    path('login/',CusomLoginView.as_view(), name="login", ),
    path('logout/',LogoutView.as_view(next_page = 'login'), name="logout", ),
    path('task/<int:pk>' , TaskDetail.as_view(), name = 'task'),
    path('create/' , TaskCreate.as_view(), name = 'task-create'),
    path('update/<int:pk>' , TaskUpdate.as_view(), name = 'task-update'),
    path('delete/<int:pk>' , TaskDelete.as_view(), name = 'task-delete'),


]
from django.urls import path

from . import views

app_name = 'weupdates'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:week>', views.index, name='index_with_week'),
    path('login', views.LoginView, name='view_login'),
    path('<int:choice_id>', views.add, name='add'),
    path('<int:activity_id>', views.remove, name= 'remove'),
    path('login_in', views.login_action, name='log_in'),
    path('logout', views.logout_view, name='logout'),
]
from django.urls import path
from api import views


urlpatterns = [
    path('client', views.ClientView.as_view()),
    path('client/<int:id>', views.ClientView.as_view()),
    path('client/get-all-clients', views.get_all_clients),
]

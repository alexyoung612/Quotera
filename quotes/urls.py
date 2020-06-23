from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:quote_id>/', views.detail, name='detail'),
    path('<int:quote_id>/email_draft/', views.email_draft, name='email draft'),
]
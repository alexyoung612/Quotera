from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.QuoteListView.as_view(), name='list'),
    path('create/', views.QuoteCreateView.as_view(), name='create'),
    path('<int:quote_id>/', views.QuoteUpdateView.as_view(), name='detail'),
    path('<int:quote_id>/email_preview/', views.email_preview, name='email_preview'),
]
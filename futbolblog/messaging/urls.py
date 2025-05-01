from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('send/', views.send_message, name='send_message'),
    path('edit/<int:message_id>/', views.edit_message, name='edit_message'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
]

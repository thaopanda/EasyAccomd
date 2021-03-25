from django.contrib import admin
from django.urls import path
from Notification import views

urlpatterns = [
    path('List/', views.NotificationList.as_view()),
    path('readNoti/<int:pk>', views.ReadNotificationView.as_view()),
]

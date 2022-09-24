from django.urls import path
from . import views
urlpatterns = [    
    path('meetingRoomDetail/', views.meetingRoomDetail, name='meetingRoomDetail'),
    path('meetingRoom/new/', views.meetingRoom, name='meetingRoom'),
    path('meetingRoomDelete/<int:pk>/delete/', views.meetingRoomDelete, name='meetingRoomDelete'),
]
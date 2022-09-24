from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
# Create your views here.
@api_view(['GET'])
def meetingRoomDetail(request):
    if request.method == 'GET':
        meetingRooms = models.meetingRoom.objects.all()
        serializer = serializers.MeetingRoomSerializer(meetingRooms, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
def meetingRoom(request):
    if request.method == 'POST':
        serializer = serializers.MeetingRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
@api_view(['DELETE'])
def meetingRoomDelete(request,pk):
    if request.method == 'DELETE':
       meeting = models.meetingRoom.objects.get(pk=pk)
       meeting.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
       
     


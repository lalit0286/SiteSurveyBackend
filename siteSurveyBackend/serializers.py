from . import models
from rest_framework import serializers
 
class MeetingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.meetingRoom
        fields = '__all__'
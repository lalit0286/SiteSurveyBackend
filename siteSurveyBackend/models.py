from distutils.command.upload import upload
from django.db import models

# Create your models here.
class meetingRoom(models.Model):
    id = models.AutoField(primary_key=True)
    siteName=models.CharField(max_length=30);
    floorNo=models.IntegerField
    MrNameAndNo=models.CharField(max_length=100);
    furnitureImg=models.ImageField(upload_to='furniture_images/',blank=True,null=True)
    ceilingImg=models.ImageField(upload_to='ceiling_images/',blank=True,null=True)
    ceilingMatTyp=models.CharField(max_length=50);
    CeilingHeight=models.CharField(max_length=50);
    distanceFromAdjancent=models.CharField(max_length=50);
    
    def __str__(self):
        return self.siteName
from distutils.command.upload import upload
from django.db import models

# Create your models here.
class meetingRoom(models.Model):
    id = models.AutoField(primary_key=True)
    siteName=models.CharField(max_length=30,default="");
    floorNo=models.IntegerField(default=0)
    MrNameAndNo=models.CharField(max_length=100,default='');
    furnitureImg=models.ImageField(upload_to='furniture_images/',default='')
    ceilingImg=models.ImageField(upload_to='ceiling_images/',default='')
    ceilingMatTyp=models.CharField(max_length=50,default='');
    CeilingHeight=models.CharField(max_length=50,default='');
    roomDim=models.CharField(max_length=50,default='');
    lenofPenLight=models.CharField(max_length=50,default='',blank=True,null=True);
    radius=models.CharField(max_length=50,blank=True,null=True);
    hangDist=models.CharField(max_length=50,default='',blank=True,null=True);
    distanceFromAdjancent=models.CharField(max_length=50,default='');
    comments=models.CharField(max_length=500,default='');
    
    def __str__(self):
        return self.siteName
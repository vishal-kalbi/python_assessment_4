from django.db import models

# Create your models here.
class SocietyMembers(models.Model):
    first_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100,unique=True)
    House_no=models.CharField(max_length=100)
    block_no=models.CharField(max_length=100)
    no_of_members=models.CharField(max_length=100)
    picture_of_owner=models.FileField(upload_to='profile.jpg',default='sad.jpg')


class SocietySecretory(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    picture=models.FileField(upload_to='secretory.jpg',default='sad.jpg')


class Watchmen(models.Model):
    watchmen_name=models.CharField(max_length=100)  
    contact_no=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    watchman_picture=models.FileField(upload_to='watchman.jpg',default='sad.jpg')

class Visitor(models.Model):
    v_name=models.CharField(max_length=100) 
    v_contact=models.CharField(max_length=100) 
    member=models.ForeignKey(SocietyMembers,on_delete=models.CASCADE)  

class Events(models.Model):
    event_name=models.CharField(max_length=100)
    event_des=models.CharField(max_length=200)
    event_date=models.CharField(max_length=100)

class Notice(models.Model):
    notice_title=models.CharField(max_length=100)    
    notice_des=models.CharField(max_length=100)    
    notice_date=models.CharField(max_length=100) 



  
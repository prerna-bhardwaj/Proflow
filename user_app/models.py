from django.db import models
from django.contrib.auth.models import User
from django.db.models import base
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case

# Create your models here.

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others')
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    postfolio = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=500, null=True)
    phone = models.CharField(max_length=30, null=True)
    gender = models.CharField(max_length=100, null=True)
    about_me = models.CharField(max_length=1000, null=True)
    college = models.JSONField(default=dict)
    internships = models.JSONField(default=dict)
    company = models.JSONField(default=dict)
    dob = models.DateField(null=True)
    communities = models.JSONField(default=list)
    following_cnt = models.IntegerField(default=0)              # Number of people you are following
    followers_cnt = models.IntegerField(default=0)              # Number of people following you
    following = models.JSONField(default=list)                  # List of people you are following
    followers = models.JSONField(default=list)                  # List of people following you

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'User Profile'

    def __str__(self) -> str:
        return self.user
    
    def to_dict(self):
        return {
            'id' : self.id,
            'user' : self.user,
            'github' : self.github,
            'linkedin' : self.linkedin,
            'portfolio' : self.portfolio,
            'address' : self.address,
            'phone' : self.phone,
            'gender' : self.gender,
            'about_me' : self.about_me,
            'college' : self.college,
            'internships' : self.internships,
            'company' : self.company,
            'dob' : self.dob,
            'communities' : self.communities,
            'following_cnt' : self.following_cnt,
            'followers_cnt' : self.followers_cnt,
            'following' : self.following,
            'followers' : self.followers,
        }


NOTIFICATION_TYPE = (
    ('FOLLOWING', 'FOLLOWING'),
    ('COMMENT', 'COMMENT'),
    ('TAG', 'TAG'),
    ('PROFILE VIEW', 'PROFILW VIEW'),
    ('PROJECT VIEW', 'PROJECT VIEW')
)

STATUS_CHOICES = (
    ('ASSIGNED', 'ASSIGNED'),
    ('VIEWED', 'VIEWED')
)

class Notifications(models.Model):
    username = models.OneToOneField(UserProfile, on_delete=CASCADE)
    creation_date = models.DateField()
    creation_time = models.TimeField()
    type = models.CharField(max_length=100, choices=NOTIFICATION_TYPE, null=True)
    description = models.CharField(max_length=1000, null=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, null=True)
    creator = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self) -> str:
        return self.description
    
    def to_dict(self):
        return {
            'username' : self.username,
            'creation_date' : self.creation_date,
            'creation_time' : self.creation_time,
            'type' : self.type,
            'description' : self.description,
            'status' : self.status,
            'creator' : self.creator,
        }

CATEGORY_CHOICES = (
    ('INTERVIEW', 'INTERVIEW'),
    ('PROJECT', 'PROJECT')
)

class Cart(models.Model):
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True)
    itemId = models.CharField(max_length=30, null=True)         # can be id of project or interview experience
    username = models.CharField(max_length=100, null=True)
    added_date = models.DateField()

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'

    def __str__(self) -> str:
        return self.itemId
    
    def to_dict(self):
        return {
            'category' : self.category,
            'itemId' : self.itemId,
            'username' : self.username,
            'added_date' : self.added_date,
        } 

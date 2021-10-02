from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)
    added_on = models.DateField(auto_now_add=True)
    added_by = models.CharField(max_length=100, null=True)
    suggested_by = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self) -> str:
        return self.name
    
    def to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'added_on' : self.added_on,
            'added_by' : self.added_by,
            'suggested_by' : self.suggested_by,
        }


class Community(models.Model):
    name = models.CharField(max_length=100, null=True)
    display_name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    follower_cnt = models.IntegerField(default=0)
    project_cnt = models.IntegerField(default=0)
    tags = models.JSONField(default=dict)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = _('Community')
        verbose_name_plural = _('Communities')

    def __str__(self) -> str:
        return self.name
    
    def to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'display_name' : self.display_name,
            'description' : self.description,
            'follower_cnt' : self.follower_cnt,
            'project_cnt' : self.project_cnt,
            'tags': self.tags
        }


TYPE_CHOICES = (
    (_('Individual'), _('Individual')),
    (_('Group'), _('Group')),
    (_('Internship'), _('Internship')),
    (_('Hackathon'), _('Hackathon')),
    (_('Company'), _('Company'))
)

VIEW_STATUS_CHOICES = (
    (_('Public'), _('Public')),
    (_('Private'), _('Private'))
)

class Project(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    display_name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    your_role = models.CharField(max_length=1000, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    ongoing = models.BooleanField(default=False, null=True)
    cover_image = models.ImageField(upload_to='project/coverImages/', max_length='1000', null=True)
    view_status = models.CharField(max_length=100, choices=VIEW_STATUS_CHOICES, null=True)
    code_link = models.URLField(null=True)                   # Github / Drive
    website = models.URLField(null=True)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, null=True)
    tags = models.JSONField(default=list)
    members = models.JSONField(default=list)
    # Auto generated fields
    views_cnt = models.IntegerField(default=0)
    likes_cnt = models.IntegerField(default=0)
    uploaded_date = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self) -> str:
        return self.name
    
    def to_dict(self):
        return {
            'id' : self.id,
            'username' : self.username,
            'name' : self.name,
            'display_name' : self.display_name,
            'description' : self.description,
            'your_role' : self.your_role,
            'start_date' : self.start_date,
            'end_date' : self.end_date,
            'ongoing' : self.ongoing,
            'cover_image' : self.cover_image,
            'view_status' : self.view_status,
            'code_link' : self.code_link,
            'website' : self.website,
            'type' : self.type,
            'tags' : self.tags,
            'members' : self.members,
            'views_cnt' : self.views_cnt,
            'likes_cnt' : self.likes_cnt,
            'uploaded_date' : self.uploaded_date,
            'last_updated' : self.last_updated,
        }


class ProjectDescription(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    heading = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=200, blank=True, null=True)
    body = models.JSONField(default=dict)
    footer = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = _('Project Description')
        verbose_name_plural = _('Project Descriptions')

    def __str__(self) -> str:
        return self.heading
    
    def to_dict(self):
        return {
            'project' : self.project,
            'heading' : self.heading,
            'sub_heading' : self.sub_heading,
            'body' : self.body,
            'footer' : self.footer,
        }


class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    header_image = models.ImageField(upload_to="projects/images", null=True)
    header_desc = models.ImageField(upload_to="projects/images", null=True)
    image1 = models.ImageField(upload_to="projects/images", null=True)
    desc1 = models.CharField(max_length=200, blank=True, null=True)
    image2 = models.ImageField(upload_to="projects/images", null=True)
    desc2 = models.CharField(max_length=200, blank=True, null=True)
    image3 = models.ImageField(upload_to="projects/images", null=True)
    desc3 = models.CharField(max_length=200, blank=True, null=True)
    image4 = models.ImageField(upload_to="projects/images", null=True)
    desc4 = models.CharField(max_length=200, blank=True, null=True)
    image5 = models.ImageField(upload_to="projects/images", null=True)
    desc5 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = _('Project Image')
        verbose_name_plural = _('Project Images')

    def __str__(self) -> str:
        return self.heading
    
    def to_dict(self):
        return {
            'project' : self.project,
            'header_image' : self.header_image.url,
            'header_desc' : self.header_desc,
        }
# Generated by Django 3.2.6 on 2021-09-30 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('display_name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('follower_cnt', models.IntegerField(default=0)),
                ('project_cnt', models.IntegerField(default=0)),
                ('tags', models.JSONField(default=dict)),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Community',
                'verbose_name_plural': 'Communities',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('display_name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('your_role', models.CharField(max_length=1000, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('ongoing', models.BooleanField(default=False, null=True)),
                ('cover_image', models.ImageField(max_length='1000', null=True, upload_to='project/coverImages/')),
                ('view_status', models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=100, null=True)),
                ('code_link', models.URLField(null=True)),
                ('website', models.URLField(null=True)),
                ('type', models.CharField(choices=[('Individual', 'Individual'), ('Group', 'Group'), ('Internship', 'Internship'), ('Hackathon', 'Hackathon'), ('Company', 'Company')], max_length=100, null=True)),
                ('tags', models.JSONField(default=list)),
                ('members', models.JSONField(default=list)),
                ('views_cnt', models.IntegerField(default=0)),
                ('likes_cnt', models.IntegerField(default=0)),
                ('uploaded_date', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('added_on', models.DateField(auto_now_add=True)),
                ('added_by', models.CharField(max_length=100, null=True)),
                ('suggested_by', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_image', models.ImageField(null=True, upload_to='projects/images')),
                ('header_desc', models.ImageField(null=True, upload_to='projects/images')),
                ('image1', models.ImageField(null=True, upload_to='projects/images')),
                ('desc1', models.CharField(blank=True, max_length=200, null=True)),
                ('image2', models.ImageField(null=True, upload_to='projects/images')),
                ('desc2', models.CharField(blank=True, max_length=200, null=True)),
                ('image3', models.ImageField(null=True, upload_to='projects/images')),
                ('desc3', models.CharField(blank=True, max_length=200, null=True)),
                ('image4', models.ImageField(null=True, upload_to='projects/images')),
                ('desc4', models.CharField(blank=True, max_length=200, null=True)),
                ('image5', models.ImageField(null=True, upload_to='projects/images')),
                ('desc5', models.CharField(blank=True, max_length=200, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj_app.project')),
            ],
            options={
                'verbose_name': 'Project Description',
                'verbose_name_plural': 'Project Descriptions',
            },
        ),
        migrations.CreateModel(
            name='ProjectDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('sub_heading', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.JSONField(default=dict)),
                ('footer', models.CharField(blank=True, max_length=200, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj_app.project')),
            ],
            options={
                'verbose_name': 'Project Description',
                'verbose_name_plural': 'Project Descriptions',
            },
        ),
    ]

# Generated by Django 3.2.6 on 2021-10-02 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_app', '0002_alter_notifications_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='username',
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='username',
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notifications',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]

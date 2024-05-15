# Generated by Django 5.0.2 on 2024-03-31 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_customuserprofile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuserprofile',
            name='campaigns',
        ),
        migrations.AlterField(
            model_name='customuserprofile',
            name='banner',
            field=models.ImageField(blank=True, default='static/images/default_banner.jpg', null=True, upload_to='static/banners/'),
        ),
        migrations.AlterField(
            model_name='customuserprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='static/images/profile_picture.jpg', null=True, upload_to='static/profile_pictures/'),
        ),
    ]
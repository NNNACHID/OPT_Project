# Generated by Django 5.0.2 on 2024-03-17 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_remove_customuserprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuserprofile',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=255, unique=True),
        ),
    ]

# Generated by Django 5.0.2 on 2024-04-03 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_remove_customuserprofile_social_links_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuserprofile',
            name='short_description',
            field=models.TextField(blank=True, help_text='Enter a short description', null=True, verbose_name='Short description'),
        ),
        migrations.AlterField(
            model_name='customuserprofile',
            name='main_description',
            field=models.TextField(blank=True, help_text='Enter a description', null=True, verbose_name='Description'),
        ),
    ]

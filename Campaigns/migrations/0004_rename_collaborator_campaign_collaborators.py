# Generated by Django 5.0.2 on 2024-04-03 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Campaigns', '0003_remove_campaign_collaborater_campaign_collaborator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='collaborator',
            new_name='collaborators',
        ),
    ]

# Generated by Django 4.0.3 on 2023-04-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_link_id_alter_link_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-11-21 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_roles_remove_profile_following_alter_profile_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='role',
            field=models.CharField(blank=True, choices=[('Founder', 'Founder'), ('Admin', 'Admin'), ('Trainer', 'Trainer'), ('Subscriber', 'Subscriber'), ('Normal Member', 'Normal Member')], max_length=150, null=True),
        ),
    ]

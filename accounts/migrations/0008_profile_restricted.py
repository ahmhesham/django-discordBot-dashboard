# Generated by Django 4.2.2 on 2023-12-30 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_accountsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='restricted',
            field=models.BooleanField(default=False),
        ),
    ]

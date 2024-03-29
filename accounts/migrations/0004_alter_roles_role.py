# Generated by Django 4.2.2 on 2023-12-01 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_roles_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='role',
            field=models.CharField(blank=True, choices=[('Founder', 'Founder'), ('Admin', 'Admin'), ('Trainer', 'Trainer'), ('Subscriber', 'Subscriber'), ('Unactive Subscriber', 'Unactive Subscriber'), ('Normal Member', 'Normal Member')], max_length=150, null=True),
        ),
    ]

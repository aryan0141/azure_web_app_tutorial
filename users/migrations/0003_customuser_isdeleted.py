# Generated by Django 4.0.1 on 2022-01-17 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_resume_delete_extendeduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='isDeleted',
            field=models.BooleanField(default=False, verbose_name='User Deleted'),
        ),
    ]
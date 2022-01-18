# Generated by Django 4.0.1 on 2022-01-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_resume_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='isDeleted',
            field=models.BooleanField(default=False, verbose_name='Soft User Deletion'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='is_latest',
            field=models.BooleanField(default=True),
        ),
    ]

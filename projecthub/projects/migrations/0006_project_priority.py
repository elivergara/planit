# Generated by Django 5.2.3 on 2025-06-24 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_is_pinned'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default='M', max_length=1),
        ),
    ]

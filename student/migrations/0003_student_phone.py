# Generated by Django 5.0.6 on 2024-06-20 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_action_remove_student_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.PositiveIntegerField(blank=True, max_length=20, null=True),
        ),
    ]

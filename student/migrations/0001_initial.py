# Generated by Django 5.0.6 on 2024-06-20 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(blank=True, max_length=200, null=True)),
                ('last', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('phone', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('hobby', models.CharField(max_length=200)),
                ('action', models.CharField(choices=[('EDIT', 'Edit'), ('DELETE', 'Delete')], max_length=6)),
            ],
        ),
    ]

# Generated by Django 5.0 on 2024-01-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
    ]

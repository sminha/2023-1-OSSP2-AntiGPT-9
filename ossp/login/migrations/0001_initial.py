# Generated by Django 4.1.7 on 2023-05-01 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userlogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tempemail', models.CharField(max_length=30)),
                ('temppwd', models.CharField(max_length=30)),
            ],
        ),
    ]

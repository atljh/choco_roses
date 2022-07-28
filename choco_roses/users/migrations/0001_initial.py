# Generated by Django 4.0.6 on 2022-07-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('phone', models.CharField(max_length=14)),
                ('address', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=240)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

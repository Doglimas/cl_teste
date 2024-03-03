# Generated by Django 3.0.7 on 2020-06-22 13:13

from django.db import migrations, models
from datetime import datetime

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=9)),
                ('content', models.CharField(max_length=11)),
                ('created_datetime', models.DateTimeField(default=datetime.now)),
            ],
        ),
    ]

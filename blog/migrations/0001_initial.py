# Generated by Django 3.0 on 2019-12-15 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='touch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.EmailField(max_length=40)),
                ('subject', models.CharField(max_length=40)),
                ('message', models.TextField(max_length=150)),
            ],
        ),
    ]

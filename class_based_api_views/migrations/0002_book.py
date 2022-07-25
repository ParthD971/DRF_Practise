# Generated by Django 4.0.6 on 2022-07-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_based_api_views', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('published', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
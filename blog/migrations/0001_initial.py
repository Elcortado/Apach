# Generated by Django 4.1.2 on 2022-11-27 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=1000, null=True)),
                ('score', models.IntegerField(default=3)),
            ],
        ),
    ]

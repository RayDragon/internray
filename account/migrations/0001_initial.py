# Generated by Django 2.0 on 2018-01-05 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60)),
                ('password', models.CharField(max_length=120)),
                ('salt', models.CharField(max_length=20)),
                ('fbid', models.CharField(max_length=15, null=True)),
            ],
        ),
    ]

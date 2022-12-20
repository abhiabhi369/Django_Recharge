# Generated by Django 4.1.4 on 2022-12-11 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(max_length=50)),
                ('circle', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('data', models.CharField(max_length=50)),
                ('validity', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]

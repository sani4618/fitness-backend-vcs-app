# Generated by Django 4.1.10 on 2023-09-04 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fitnessapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='', max_length=50)),
                ('middleName', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(default='', max_length=50)),
                ('dateOfBirth', models.CharField(default='', max_length=50)),
                ('department', models.CharField(default='', max_length=50)),
                ('userName', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
                ('confirmPassword', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
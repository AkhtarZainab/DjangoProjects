# Generated by Django 5.0.1 on 2024-01-29 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=10)),
                ('LastName', models.CharField(max_length=10)),
                ('UserName', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('cpassword', models.CharField(max_length=10)),
                ('MobileNumber', models.IntegerField()),
                ('Emailid', models.EmailField(max_length=254)),
            ],
        ),
    ]

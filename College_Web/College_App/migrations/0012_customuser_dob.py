# Generated by Django 4.1.3 on 2022-11-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College_App', '0011_alter_studentresult_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='DOB',
            field=models.DateField(null=True),
        ),
    ]
# Generated by Django 3.0.5 on 2023-04-06 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0043_student_mail_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mail_id',
            field=models.CharField(default='sample@gmail.com', max_length=40),
        ),
    ]

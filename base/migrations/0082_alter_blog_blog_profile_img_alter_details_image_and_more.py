# Generated by Django 4.1.9 on 2023-07-21 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0081_alter_faculty_details_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_profile_img',
            field=models.CharField(default='https://99designs-blog.imgix.net/blog/wp-content/uploads/2018/12/Gradient_builder_2.jpg?auto=format&q=60&w=1815&h=1200&fit=crop&crop=faces', max_length=2000),
        ),
        migrations.AlterField(
            model_name='details',
            name='image',
            field=models.ImageField(default='images/user.jpg', upload_to='photo/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='draft_blog',
            name='blog_profile_img',
            field=models.CharField(default='https://i.pinimg.com/736x/37/ef/3c/37ef3c60c92222f35f37d5f9e4eacd69.jpg', max_length=2000),
        ),
        migrations.AlterField(
            model_name='faculty_details',
            name='image',
            field=models.ImageField(default='images/user.jpg', upload_to='photo/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='images/bgwebp.webp', upload_to='Gallery/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='logo',
            name='image',
            field=models.ImageField(default='images/bgwebp.webp', upload_to='logo'),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/std.webp'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/teacher.webp'),
        ),
    ]

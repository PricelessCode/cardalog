# Generated by Django 3.1.7 on 2021-07-02 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pics/male.png', upload_to='profile_pics'),
        ),
    ]
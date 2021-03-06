# Generated by Django 3.1.7 on 2021-04-28 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=100)),
                ('definition', models.CharField(max_length=150)),
                ('example', models.CharField(max_length=150)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('card_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sets.set')),
            ],
        ),
    ]

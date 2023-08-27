# Generated by Django 4.2.4 on 2023-08-27 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=60)),
                ('text', models.TextField()),
                ('likes', models.IntegerField()),
            ],
        ),
    ]
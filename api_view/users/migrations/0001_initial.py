# Generated by Django 5.0.6 on 2024-05-28 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users/')),
                ('about', models.TextField(blank=True, null=True)),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

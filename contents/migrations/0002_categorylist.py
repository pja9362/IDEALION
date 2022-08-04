# Generated by Django 3.2.2 on 2021-06-30 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoryList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, unique=True)),
                ('share', models.BooleanField(default='true')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='idea/')),
                ('author', models.CharField(default='', max_length=200)),
            ],
        ),
    ]

# Generated by Django 3.2.16 on 2023-01-18 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_recipe_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=200)),
                ('body', models.TextField(blank=True)),
            ],
        ),
    ]

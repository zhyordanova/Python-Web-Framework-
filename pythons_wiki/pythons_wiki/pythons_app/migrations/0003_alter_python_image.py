# Generated by Django 3.2.5 on 2021-07-17 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythons_app', '0002_alter_python_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='python',
            name='image',
            field=models.ImageField(upload_to='pythons'),
        ),
    ]

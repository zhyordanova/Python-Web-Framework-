# Generated by Django 3.2.5 on 2021-07-17 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phones_app', '0002_phone_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='phones')),
                ('is_selected', models.BooleanField(default=False)),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones_app.phone')),
            ],
        ),
    ]
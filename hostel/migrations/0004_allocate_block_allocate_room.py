# Generated by Django 3.2.9 on 2022-05-10 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hostel', '0003_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='allocate_room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('block_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hostel.hostel_block')),
                ('hostel_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hostel.hostel')),
                ('room', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hostel.room')),
                ('student', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='allocate_block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('block_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hostel.hostel_block')),
                ('hostel_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hostel.hostel')),
                ('warden', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

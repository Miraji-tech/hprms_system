# Generated by Django 3.2.9 on 2022-05-29 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0004_allocate_block_allocate_room'),
        ('problems_report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_report_problem',
            name='allocated_room',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hostel.allocate_room'),
        ),
        migrations.AddField(
            model_name='student_report_problem',
            name='block_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hostel.hostel_block'),
        ),
        migrations.AddField(
            model_name='student_report_problem',
            name='hostel',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hostel.hostel'),
        ),
        migrations.AddField(
            model_name='student_report_problem',
            name='room_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hostel.room'),
        ),
        migrations.AddField(
            model_name='warden_report_problem',
            name='block_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hostel.hostel_block'),
        ),
        migrations.AddField(
            model_name='warden_report_problem',
            name='hostel',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hostel.hostel'),
        ),
    ]

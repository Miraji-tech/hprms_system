# Generated by Django 3.2.9 on 2022-05-30 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems_report', '0004_alter_student_report_problem_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_report_problem',
            name='feedback',
            field=models.IntegerField(default=0),
        ),
    ]

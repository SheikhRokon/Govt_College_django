# Generated by Django 4.2.5 on 2023-09-16 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_add_student_info_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='result_file',
            field=models.FileField(blank=True, null=True, upload_to='result/'),
        ),
    ]

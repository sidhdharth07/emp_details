# Generated by Django 4.2.3 on 2023-07-18 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_detail_model',
            name='birthday',
            field=models.CharField(),
        ),
    ]
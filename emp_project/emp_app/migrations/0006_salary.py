# Generated by Django 4.2.3 on 2023-07-19 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0005_emergency_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
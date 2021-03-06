# Generated by Django 4.0.3 on 2022-03-21 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('blood_group', models.CharField(max_length=100)),
                ('admissiondate', models.DateField()),
                ('course', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
    ]

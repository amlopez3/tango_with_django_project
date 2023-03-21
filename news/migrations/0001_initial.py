# Generated by Django 2.1.5 on 2023-03-21 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('author', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('text', models.TextField()),
            ],
        ),
    ]
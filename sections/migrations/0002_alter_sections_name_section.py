# Generated by Django 4.0.6 on 2022-10-02 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sections',
            name='name_section',
            field=models.CharField(max_length=100),
        ),
    ]

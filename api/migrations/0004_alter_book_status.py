# Generated by Django 4.0.3 on 2022-03-18 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(default='available', max_length=255),
        ),
    ]

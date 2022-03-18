# Generated by Django 4.0.3 on 2022-03-18 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='api.library'),
        ),
    ]
# Generated by Django 4.2.1 on 2023-05-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_base_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

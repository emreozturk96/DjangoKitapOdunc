# Generated by Django 3.0.5 on 2020-04-19 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_auto_20200419_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('New', 'Yeni'), ('True', 'Evet'), ('False', 'Hayır')], default='New', max_length=10),
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-31 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='contactus',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='aboutus',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='company',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='setting',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='setting',
            name='facebook',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='setting',
            name='instagram',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='setting',
            name='keywords',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='setting',
            name='references',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtpemail',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtppasswords',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtpserver',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='setting',
            name='twitter',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]

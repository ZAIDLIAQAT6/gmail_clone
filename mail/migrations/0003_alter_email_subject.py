# Generated by Django 5.1.2 on 2024-12-29 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_rename_date_sent_email_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='subject',
            field=models.CharField(max_length=200),
        ),
    ]
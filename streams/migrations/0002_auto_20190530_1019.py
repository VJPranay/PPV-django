# Generated by Django 2.2 on 2019-05-30 10:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livestream',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='livestream',
            name='uid',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=255, null=True),
        ),
    ]

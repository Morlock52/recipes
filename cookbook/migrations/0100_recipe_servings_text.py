# Generated by Django 3.1.5 on 2021-01-21 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0099_auto_20210113_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='servings_text',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-21 12:22

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='home_title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

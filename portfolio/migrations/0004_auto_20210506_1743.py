# Generated by Django 3.1.7 on 2021-05-06 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_education_experience'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='cource',
            new_name='course',
        ),
    ]
# Generated by Django 3.1.7 on 2021-07-12 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_hobbies_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='趣味')),
                ('image', models.ImageField(blank=True, null=True, upload_to='hobby_images', verbose_name='イメージ画像')),
            ],
            options={
                'verbose_name_plural': 'Hobbies',
            },
        ),
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
        migrations.DeleteModel(
            name='Hobbies',
        ),
    ]

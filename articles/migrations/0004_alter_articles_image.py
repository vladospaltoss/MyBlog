# Generated by Django 4.1.5 on 2023-01-25 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(default='', upload_to='media/images/'),
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-03 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Şəkil'),
        ),
    ]

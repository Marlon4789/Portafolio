# Generated by Django 5.0.3 on 2024-03-19 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_quillpost_description_alter_quillpost_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='quillpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='quillpost_images/'),
        ),
    ]
# Generated by Django 4.2.23 on 2025-06-13 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_book_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=20, null=True),
        ),
    ]

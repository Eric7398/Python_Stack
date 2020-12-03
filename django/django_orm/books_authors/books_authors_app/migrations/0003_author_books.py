# Generated by Django 2.2 on 2020-11-05 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_author_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='books_authors_app.Book'),
        ),
    ]

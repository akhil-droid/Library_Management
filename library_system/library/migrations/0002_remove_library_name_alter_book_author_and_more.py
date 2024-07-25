# Generated by Django 5.0.7 on 2024-07-25 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='name',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='file_format',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(to='library.book'),
        ),
    ]

# Generated by Django 4.2.4 on 2024-05-27 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0003_booksborrowed_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksborrowed',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='librarian.books'),
        ),
    ]

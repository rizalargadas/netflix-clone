# Generated by Django 5.0.1 on 2024-06-03 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_tv', '0002_remove_movie_vote_count_vote_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

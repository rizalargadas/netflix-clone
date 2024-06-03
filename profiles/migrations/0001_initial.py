# Generated by Django 5.0.1 on 2024-06-02 08:24

import django.db.models.deletion
import profiles.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='profiles/images')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_kid', models.BooleanField(blank=True, default=False, null=True)),
                ('pin', models.CharField(blank=True, max_length=4, null=True)),
                ('enter_pin', models.CharField(blank=True, max_length=4, null=True)),
                ('confirm_pin', models.CharField(blank=True, max_length=4, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL)),
                ('avatar', models.ForeignKey(default=profiles.models.get_default_profile_image, on_delete=django.db.models.deletion.CASCADE, to='profiles.profileimage')),
            ],
        ),
    ]

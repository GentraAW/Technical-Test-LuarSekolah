# Generated by Django 5.1 on 2024-09-03 03:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_category_training'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased_at', models.DateTimeField(auto_now_add=True)),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='users.training')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

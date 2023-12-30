# Generated by Django 4.1.2 on 2023-12-30 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dispensa_petfood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petproduct',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='petproduct',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]

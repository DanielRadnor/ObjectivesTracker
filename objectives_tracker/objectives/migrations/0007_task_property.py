# Generated by Django 3.1.4 on 2020-12-31 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objectives', '0006_auto_20201231_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='objectives.property'),
        ),
    ]
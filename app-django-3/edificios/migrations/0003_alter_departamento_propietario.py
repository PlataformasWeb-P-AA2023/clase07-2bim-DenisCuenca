# Generated by Django 4.2.2 on 2023-07-19 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "edificios",
            "0002_propietario_remove_departamento_nombrepropietario_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="departamento",
            name="propietario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="departamentos",
                to="edificios.propietario",
            ),
        ),
    ]

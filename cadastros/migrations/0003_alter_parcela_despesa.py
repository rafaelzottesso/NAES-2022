# Generated by Django 4.0.3 on 2022-08-22 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_despesa_cadastrado_em_despesa_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcela',
            name='despesa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.despesa'),
        ),
    ]
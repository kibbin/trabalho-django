# Generated by Django 5.2.3 on 2025-06-20 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_produto_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='descricao',
        ),
    ]

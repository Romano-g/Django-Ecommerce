# Generated by Django 5.0.3 on 2024-03-05 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_alter_produto_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produto',
            options={},
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao_longa',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produto_imagens/%Y/%m/'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing',
            field=models.FloatField(verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(default=0, verbose_name='Preço Promo.'),
        ),
    ]

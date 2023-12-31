# Generated by Django 4.2.4 on 2023-09-01 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='capitulo',
            options={},
        ),
        migrations.AlterModelOptions(
            name='livro',
            options={},
        ),
        migrations.AlterModelOptions(
            name='pagina',
            options={},
        ),
        migrations.RemoveField(
            model_name='livro',
            name='author',
        ),
        migrations.AlterField(
            model_name='capitulo',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livro.livro'),
        ),
        migrations.AlterField(
            model_name='pagina',
            name='capitulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livro.capitulo'),
        ),
        migrations.AlterField(
            model_name='pagina',
            name='numero',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]

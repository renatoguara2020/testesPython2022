# Generated by Django 4.1.2 on 2022-12-31 12:20

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Funcionario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("sobrenome", models.CharField(max_length=255)),
                ("cpf", models.CharField(max_length=14)),
                ("tempo_de_servico", models.IntegerField(default=0)),
                ("remuneracao", models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            managers=[("objetos", django.db.models.manager.Manager()),],
        ),
        migrations.CreateModel(
            name="Produto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                ("descricao", models.CharField(max_length=255)),
                ("preco", models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            managers=[("objetos", django.db.models.manager.Manager()),],
        ),
        migrations.CreateModel(
            name="Venda",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_hora", models.DateTimeField(auto_now_add=True)),
                (
                    "funcionario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_app.funcionario",
                    ),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="my_app.produto"
                    ),
                ),
            ],
            managers=[("objetos", django.db.models.manager.Manager()),],
        ),
    ]

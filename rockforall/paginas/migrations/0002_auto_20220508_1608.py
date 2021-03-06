# Generated by Django 3.1.6 on 2022-05-08 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pensamento',
            name='ideia',
            field=models.TextField(verbose_name='O que você esta pensando ? Post suas idéias.'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='image',
            field=models.ImageField(default='media/forall.png', upload_to='media/perfil', verbose_name='IMAGEM PERFIL :'),
        ),
        migrations.CreateModel(
            name='SalaBatePapo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkSala', models.CharField(max_length=200, verbose_name='LINK DA SUA SALA')),
                ('SalaCriadaEm', models.DateTimeField(auto_now_add=True, verbose_name='Criada em:')),
                ('SalaModificadaem', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Postado Por:')),
            ],
        ),
    ]

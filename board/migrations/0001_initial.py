# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 10:58
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('status', models.CharField(choices=[('un', 'Неизвестно'), ('cl', 'Завершить'), ('ca', 'Отменить'), ('la', 'Отложить')], default='un', max_length=2, verbose_name='Статус')),
                ('deadline', models.DateTimeField(verbose_name='Дедлайн')),
                ('priority', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)], verbose_name='Приоритет')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='board.Task'),
        ),
    ]
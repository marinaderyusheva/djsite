# Generated by Django 4.1.3 on 2022-12-01 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rabotodateli',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_onsite', models.DateField(null=True, verbose_name='На сайте с ')),
                ('is_company', models.BooleanField(default=False, verbose_name='Человек/Компания')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Spheres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_sphere', models.CharField(choices=[('D', 'Дизайн'), ('M', 'Маркетинг'), ('P', 'Программирование')], default='D', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Vakancii',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_vakancii', models.CharField(max_length=255, verbose_name='Наименование вакансии')),
                ('about_vakancii', models.TextField(blank=True, verbose_name='О вакансии')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Обновлена')),
                ('is_published', models.BooleanField(default=True, verbose_name='Актуальность')),
                ('rabotodat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.rabotodateli')),
                ('sphere', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.spheres')),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(null=True, verbose_name='Возраст')),
                ('experience', models.IntegerField(null=True, verbose_name='Опыт работы')),
                ('about_freelancer', models.TextField(blank=True, verbose_name='О себе')),
                ('sphere', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.spheres')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('vakancii', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.vakancii')),
            ],
        ),
    ]

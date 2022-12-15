# Generated by Django 4.1.4 on 2022-12-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='freelancer',
            options={'ordering': ['sphere', 'experience'], 'verbose_name': 'Фрилансеры', 'verbose_name_plural': 'Фрилансеры'},
        ),
        migrations.AlterModelOptions(
            name='rabotodateli',
            options={'ordering': ['is_company'], 'verbose_name': 'Работодатели', 'verbose_name_plural': 'Работодатели'},
        ),
        migrations.AlterModelOptions(
            name='spheres',
            options={'ordering': ['name_sphere'], 'verbose_name': 'Cферы', 'verbose_name_plural': 'Cферы'},
        ),
        migrations.AlterModelOptions(
            name='vakancii',
            options={'ordering': ['sphere', 'time_create'], 'verbose_name': 'Вакансии', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AlterField(
            model_name='spheres',
            name='name_sphere',
            field=models.CharField(choices=[('Дизайн', 'D'), ('Маркетинг', 'M'), ('Программирование', 'P')], default='D', max_length=30),
        ),
    ]

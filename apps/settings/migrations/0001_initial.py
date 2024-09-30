# Generated by Django 5.1 on 2024-09-30 12:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='settings/', verbose_name='Фото 1')),
                ('image2', models.ImageField(upload_to='settings/', verbose_name='Фото 2')),
                ('image3', models.ImageField(upload_to='settings/', verbose_name='Фото 3')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('descriptions', ckeditor.fields.RichTextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': ' О нас',
            },
        ),
        migrations.CreateModel(
            name='About_Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя специалиста')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('occupation', models.CharField(max_length=100, verbose_name='Профессия')),
                ('phone', models.CharField(max_length=100, verbose_name='Контактные данные')),
                ('email', models.CharField(max_length=100, verbose_name='Почта')),
                ('nationality', models.CharField(max_length=100, verbose_name='Национальность')),
            ],
            options={
                'verbose_name': 'Специалисты',
                'verbose_name_plural': 'Специалиста',
            },
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='logo/', verbose_name='Фото 1')),
                ('rank', models.CharField(max_length=50, verbose_name='Звание')),
                ('year', models.IntegerField(verbose_name='Год получения')),
                ('rank_association', models.CharField(max_length=50, verbose_name='Ассоциация')),
                ('place', models.CharField(max_length=50, verbose_name='Место, где получил звание')),
                ('description', models.CharField(max_length=100, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Звание',
                'verbose_name_plural': 'Звание',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('phone', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('subject', models.CharField(max_length=155, verbose_name='Обьект')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=155, verbose_name='Локация')),
                ('phone', models.IntegerField(max_length=155, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=155, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакт',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Звание')),
                ('mini_title', models.CharField(max_length=50, verbose_name='В каком учреждении я получил образование')),
                ('year', models.IntegerField(verbose_name='Год получения')),
                ('description', models.CharField(max_length=100, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Образование',
                'verbose_name_plural': 'Образование',
            },
        ),
        migrations.CreateModel(
            name='Expirience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Звание')),
                ('mini_title', models.CharField(max_length=50, verbose_name='В каком компании получил опыт работы')),
                ('year', models.IntegerField(verbose_name='Год получения')),
                ('description', models.CharField(max_length=100, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Опыт работы',
                'verbose_name_plural': 'Опыт работы',
            },
        ),
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=100, verbose_name='Количество')),
                ('title_2', models.CharField(max_length=100, verbose_name='Краткое описание')),
            ],
            options={
                'verbose_name_plural': 'Факты',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_direction', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('main_title', models.CharField(max_length=100, verbose_name='Что и для кого был сделан проект')),
                ('image_1', models.ImageField(upload_to='portfolio/', verbose_name='Фото 1')),
                ('image_2', models.ImageField(upload_to='portfolio/', verbose_name='Фото 2')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=200, verbose_name='Про сам проект')),
                ('project_type', models.CharField(max_length=100, verbose_name='Тип проета')),
                ('сlient', models.CharField(max_length=100, verbose_name='Клиент')),
                ('duration', models.CharField(max_length=100, verbose_name='Срок разработки')),
                ('task', models.CharField(max_length=100, verbose_name='Какие направления были воздействованы')),
                ('budget', models.CharField(max_length=100, verbose_name='Бюджет')),
            ],
            options={
                'verbose_name': 'Портфолио',
                'verbose_name_plural': 'Портфолио',
            },
        ),
        migrations.CreateModel(
            name='PricePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('is_1', models.BooleanField(default=False, verbose_name='Разовый контракт')),
                ('is_2', models.BooleanField(default=False, verbose_name='Гибкий контракт')),
                ('is_3', models.BooleanField(default=False, verbose_name='Исходные файлы')),
                ('is_4', models.BooleanField(default=False, verbose_name='Поддержка')),
                ('is_5', models.BooleanField(default=False, verbose_name='Обновления')),
            ],
            options={
                'verbose_name': 'Прайс план',
                'verbose_name_plural': 'Прайс план',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='icon/', verbose_name='Фото 1')),
                ('title', models.CharField(max_length=100, verbose_name='Название проекта')),
                ('description', models.CharField(max_length=155, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проект',
            },
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quot', models.CharField(max_length=775, verbose_name='Цитата')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('company', models.CharField(max_length=50, verbose_name='Из какой компании автор')),
                ('image', models.ImageField(upload_to='image_author/', verbose_name='Фото Автора')),
            ],
            options={
                'verbose_name': 'Цитата',
                'verbose_name_plural': 'Цитата',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('image1', models.ImageField(upload_to='settings/', verbose_name='Фото 1')),
                ('image2', models.ImageField(upload_to='settings/', verbose_name='Фото 2')),
                ('image3', models.ImageField(upload_to='settings/', verbose_name='Фото 3')),
                ('image4', models.ImageField(upload_to='settings/', verbose_name='Фото 4')),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('youtube', models.URLField()),
                ('linkedin', models.URLField()),
                ('instagram', models.URLField()),
                ('run_title_1', models.CharField(max_length=155, verbose_name='Бегающий текст - 1')),
                ('run_title_2', models.CharField(max_length=155, verbose_name='Бегающий текст - 2')),
                ('footer_name_studio', models.CharField(max_length=155, verbose_name='Название студии')),
            ],
            options={
                'verbose_name': 'Настройка Главной',
                'verbose_name_plural': 'Настройка Главной',
            },
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('descriptions', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='shape', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Shape',
                'verbose_name_plural': 'Shape',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100, verbose_name='Скилл')),
                ('percent', models.IntegerField(max_length=100, verbose_name='Владение скиллом в процентах')),
            ],
            options={
                'verbose_name': 'Скилл',
                'verbose_name_plural': 'Скилл',
            },
        ),
    ]

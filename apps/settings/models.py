from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )
    image1 = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото 1'
    )
    image2 = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото 2'
    )
    image3 = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото 3'
    )
    image4 = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото 4'
    )

    facebook = models.URLField()
    twitter = models.URLField()
    youtube = models.URLField()
    linkedin = models.URLField()
    instagram = models.URLField()


    run_title_1 = models.CharField(
        verbose_name='Бегающий текст - 1',
        max_length=155,
    )

    run_title_2 = models.CharField(
        verbose_name='Бегающий текст - 2',
        max_length=155,
    )
    footer_name_studio = models.CharField(
        max_length=155,
        verbose_name="Название студии"
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Настройка Главной'
        verbose_name_plural = 'Настройка Главной'

class Shape(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='shape',
        verbose_name='Фото'
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Shape"
        verbose_name_plural = 'Shape'

class About(models.Model):
    image1 = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото 1'
    )
    image2 = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото 2'
    )
    image3 = models.ImageField(
        upload_to='settings/',
        verbose_name='Фото 3'
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = ' О нас'


class Contact(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    phone = models.CharField(
        max_length=50,
        verbose_name='Номер телефона'
    )
    subject = models.CharField(
        max_length=155,
        verbose_name='Обьект'
    )
    message = models.TextField(
        verbose_name='Сообщение'
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'

class About_Person(models.Model):
    name = models.CharField(
        max_length = 100,
        verbose_name = "Имя специалиста"
    )
    age = models.IntegerField(
        verbose_name = "Возраст"
    )
    occupation = models.CharField(
        max_length = 100,
        verbose_name = "Профессия"
    )
    phone = models.CharField(
        max_length = 100,
        verbose_name = "Контактные данные"
    )
    email = models.CharField(
        max_length = 100,
        verbose_name = "Почта"
    )
    nationality = models.CharField(
        max_length = 100,
        verbose_name = "Национальность"
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Специалисты'
        verbose_name_plural = 'Специалиста'

class Portfolio(models.Model):
    main_direction = models.CharField(
        max_length = 100,
        verbose_name = "Заголовок"
    )
    main_title = models.CharField(
        max_length = 100,
        verbose_name = "Что и для кого был сделан проект"
    )
    image_1 = models.ImageField(
        upload_to='portfolio/',
        verbose_name='Фото 1'
    )
    image_2 = models.ImageField(
        upload_to='portfolio/',
        verbose_name='Фото 2'
    )
    title = models.CharField(
        max_length = 100,
        verbose_name = "Заголовок"
    )
    description = models.CharField(
        max_length = 200,
        verbose_name = "Про сам проект"
    )
    project_type = models.CharField(
        max_length = 100,
        verbose_name = "Тип проета"
    )
    сlient = models.CharField(
        max_length = 100,
        verbose_name = "Клиент"
    )
    duration  = models.CharField(
        max_length = 100,
        verbose_name = "Срок разработки"
    )
    task = models.CharField(
        max_length = 100,
        verbose_name = "Какие направления были воздействованы"
    )
    budget = models.CharField(
        max_length = 100,
        verbose_name = "Бюджет"
    )

    def __str__(self) -> str:
        return f"Портфолио {self.id}"
    
    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'

class Fact(models.Model):
    quantity = models.CharField(
        max_length = 100,
        verbose_name = "Количество"
    )
    title_2 = models.CharField(
        max_length = 100,
        verbose_name = "Краткое описание"
    )

    def __str__(self) -> str:
        return f"Факт {self.id}"
    
    class Meta:
        verbose_name_plural = 'Факты'

class Awards(models.Model):
    image = models.ImageField(
        upload_to="logo/",
        verbose_name="Фото 1"
    )
    rank = models.CharField(
        max_length=50,
        verbose_name="Звание"
    )
    year = models.IntegerField(
        verbose_name="Год получения"
    )
    rank_association= models.CharField(
        max_length=50,
        verbose_name="Ассоциация"
    )
    place = models.CharField(
        max_length=50,
        verbose_name="Место, где получил звание"
    )
    description = models.CharField(
        max_length=100,
        verbose_name="Описание"
    )

    def __str__(self) -> str:
        return f"Звание {self.id}"
    
    class Meta:
        verbose_name = 'Звание'
        verbose_name_plural = 'Звание'


class Expirience(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Звание"
    )
    mini_title = models.CharField(
        max_length=50,
        verbose_name="В каком компании получил опыт работы"
    )
    year = models.IntegerField(
        verbose_name="Год получения"
    )
    description = models.CharField(
        max_length=100,
        verbose_name="Описание"
    )

    def __str__(self) -> str:
        return f"Опыт работы {self.id}"
    
    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'

class Education(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Звание"
    )
    mini_title = models.CharField(
        max_length=50,
        verbose_name="В каком учреждении я получил образование"
    )
    year = models.IntegerField(
        verbose_name="Год получения"
    )
    description = models.CharField(
        max_length=100,
        verbose_name="Описание"
    )

    def __str__(self) -> str:
        return f"Образование {self.id}"
    
    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'


class Skills(models.Model):
    skill = models.CharField(
        max_length=100,
        verbose_name="Скилл"
    )
    percent = models.IntegerField(
        max_length=100,
        verbose_name="Владение скиллом в процентах"
    )
    
    def __str__(self) -> str:
        return f"Скилл {self.id}"
    
    class Meta:
        verbose_name = 'Скилл'
        verbose_name_plural = 'Скилл'

class Project(models.Model):
    icon = models.ImageField(
        upload_to="icon/",
        verbose_name="Фото 1"
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Название проекта"
    )
    description = models.CharField(
        max_length=155,
        verbose_name="Описание"
    )
    
    def __str__(self) -> str:
        return f"Проект {self.id}"
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проект'

class PricePlan(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок"
    )
    price = models.IntegerField(
        verbose_name="Цена"
    )
    is_1 = models.BooleanField(
        default=False,
        verbose_name="Разовый контракт"
    )
    is_2 = models.BooleanField(
        default=False,
        verbose_name="Гибкий контракт"
    )
    is_3 = models.BooleanField(
        default=False,
        verbose_name="Исходные файлы"
    )
    is_4 = models.BooleanField(
        default=False,
        verbose_name="Поддержка"
    )
    is_5 = models.BooleanField(
        default=False,
        verbose_name="Обновления"
    )    
    
    def __str__(self) -> str:
        return f"Прайс план {self.id}"
    
    class Meta:
        verbose_name = 'Прайс план'
        verbose_name_plural = 'Прайс план'

class Quotes(models.Model):
    quot = models.CharField(
        max_length=775,
        verbose_name="Цитата"
    )
    author = models.CharField(
        max_length=50,
        verbose_name="Автор"
    )
    company = models.CharField(
        max_length=50,
        verbose_name="Из какой компании автор"
    )
    image = models.ImageField(
        upload_to="image_author/",
        verbose_name="Фото Автора"
    )

    def __str__(self) -> str:
        return f"Цитата {self.id}"
    
    class Meta:
        verbose_name = 'Цитата'    
        verbose_name_plural = 'Цитата'    

class ContactMe(models.Model):
    location = models.CharField(
        max_length=155,
        verbose_name="Локация"
    )
    phone = models.IntegerField(
        max_length=155,
        verbose_name="Номер телефона"
    )
    email = models.CharField(
        max_length=155,
        verbose_name="Email"
    )

    def __str__(self) -> str:
        return f"Контакт {self.id}"
    
    class Meta:
        verbose_name = 'Контакт'   
        verbose_name_plural = 'Контакт'   

# class Blog(models.Model):
#     image = models.ImageField(
#         upload_to="blog/",
#         verbose_name="Фото"
#     )

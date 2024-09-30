from django.db import models

# Create your models here.

class UserContact(models.Model):
    name = models.CharField(
        max_length=155, 
        verbose_name='Имя'
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    phone = models.CharField(
        max_length=20, 
        verbose_name='Телефон'
    )
    subject = models.CharField(
        max_length=155, 
        verbose_name='Тема'
    )
    message = models.TextField(
        verbose_name='Сообщение'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата создания'
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Контактные сообщения'

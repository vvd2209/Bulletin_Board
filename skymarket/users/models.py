from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    """ Роли пользователей """
    ADMIN = 'admin', _('admin')
    USER = 'user', _('user')


class User(AbstractUser):
    """ Модель представления класса Пользователь, наследуемая от абстрактного класса """
    username = None  # исключение поля "username", так как вместо него будет использовано поле "email"

    first_name = models.CharField(max_length=150, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='email')
    phone = PhoneNumberField(verbose_name='Номер телефона')
    role = models.CharField(max_length=150, default=UserRoles.USER, choices=UserRoles.choices, verbose_name='Роль пользователя')
    image = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Активность пользователя')

    USERNAME_FIELD = "email"  # указание на то, что поле "email" будет использоваться для идентификации пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']  # поля, которые будут запрашиваться при создании пользователя через команду createsuperuser

    def __str__(self):
        """ Метод представления модели в виде строки """
        return f"{self.email}"

    class Meta:
        """ Метаданные модели """
        verbose_name = "пользователь"
        verbose_name_plural = 'пользователи'

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

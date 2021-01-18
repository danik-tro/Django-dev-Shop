from django.db import models

"""
категории(без подкатегорий)
товары(с картинкой, описанием, ценой)
аккаунт пользователя
корзина
история прошлых заказов
способы доставки и оплаты
"""


class Category(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Наименование товара')
    describe = models.TextField(verbose_name='Описание товара')
    photo = models.ImageField(blank=True, verbose_name='Фото товара')
    price = models.DecimalField(verbose_name="Цена товара")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


# class History(models.Model):
#     pass


# class Cart(models.Model):
#     pass
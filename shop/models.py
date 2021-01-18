from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='Категория',
                            db_index=True)
    slug = models.SlugField(max_length=200, unique=True,
                            blank=True,
                            db_index=True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'shop:product_list_by_category',
            args=[self.slug]
        )


class Product(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='Наименование продукта',
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True)
    description = models.TextField(verbose_name='Описание продукта',
                                   blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True,
                              verbose_name='Изображение продукта')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name="Цена продукта")
    stock = models.PositiveIntegerField(verbose_name="Остаток продукта")
    available = models.BooleanField(default=True, verbose_name='Наличие товара')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'shop:product_detail',
            args=[self.id, self.slug]
        )


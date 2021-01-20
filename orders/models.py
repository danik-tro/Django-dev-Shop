from django.db import models
from shop.models import Product
from users.models import User


class Delivery(models.Model):
    name = models.CharField(max_length=50, verbose_name="Способ доставки",
                            db_index=True)
    slug = models.SlugField(max_length=50, blank=True,
                            db_index=True, unique=True)

    class Meta:
        verbose_name = 'Способ доставки'
        verbose_name_plural = 'Способы доставки'

        ordering = ('name',)

    def __str__(self):
        return self.name


class PaymentMethod(models.Model):
    name = models.CharField(max_length=50, verbose_name='Способ доставки', db_index=True)
    slug = models.SlugField(max_length=50, blank=True,
                            db_index=True, unique=True)

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'

        ordering = ('name',)

    def __str__(self):
        return self.name


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField()
    address = models.CharField(max_length=250, verbose_name='Адресс')
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100, verbose_name='Город')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    payment = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Заказчик')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Историю заказа'
        verbose_name_plural = 'Истории заказов'
        ordering = ('date',)

    def __str__(self):
        return str(self.date)


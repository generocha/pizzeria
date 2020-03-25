from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PizzaType(models.Model):
    typename = models.CharField(max_length=255)
    typedescription = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table = 'pizzatype'
        verbose_name_plural = 'pizzatypes'


class Pizza(models.Model):
    pizzaname = models.CharField(max_length=255)
    pizzatype = models.ForeignKey(PizzaType, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    pizzaprice = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    pizzaentrydate = models.DateField()
    pizzaurl = models.URLField(null=True, blank=True)
    pizzadescription = models.TextField()
    pizzaimage = models.ImageField(
        upload_to='images', null=True, blank=True)

    def memberdiscount(self):
        discountpercent = .05
        return float(self.pizzaprice) * discountpercent

    def __str__(self):
        return self.pizzaname

    class Meta:
        db_table = 'pizza'
        verbose_name_plural = 'pizzas'

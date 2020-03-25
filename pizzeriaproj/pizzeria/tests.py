from django.test import TestCase
from .models import Pizza, PizzaType
from .views import index, gettypes, getpizzas
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.


class PizzaTypeTest(TestCase):
    def test_string(self):
        type = PizzaType(typename="Vegetarian")
        self.assertEqual(str(type), type.typename)

    def test_table(self):
        self.assertEqual(str(PizzaType._meta.db_table), 'pizzatype')


class PizzaTest(TestCase):
    # set up one time sample data
    def setup(self):
        type = PizzaType(typename='Vegetarian')
        pizza = Pizza(pizzaname='Lenovo', pizzatype=type, pizzaprice='500.00')
        return pizza

    def test_string(self):
        pizz = self.setup()
        self.assertEqual(str(pizz), pizz.pizzaname)

    # test the discount property
    def test_discount(self):
        pizz = self.setup()
        self.assertEqual(pizz.memberdiscount(), 25.00)

    def test_type(self):
        pizz = self.setup()
        self.assertEqual(str(pizz.pizzatype), 'Vegetarian')

    def test_table(self):
        self.assertEqual(str(Pizza._meta.db_table), 'pizza')


class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class GetPizzasTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('pizzas'))
        self.assertEqual(response.status_code, 200)


def setUp(self):
    self.u = User.objects.create(username='myuser')
    self.type = PizzaType.objects.create(typename='Vegetarian')
    self.pizz = Pizza.objects.create(productname='pizza1', pizzatype=self.type, user=self.u,
                                     pizzaprice=500, pizzaentrydate='2020-03-25', pizzadescription="a Pizza!")


def test_pizza_detail_success(self):
    response = self.client.get(reverse('pizzadetails', args=(self.pizz.id,)))
    # Assert that self.post is actually returned by the post_detail view
    self.assertEqual(response.status_code, 200)


def test_discount(self):
    discount = self.pizz.memberdiscount()
    self.assertEqual(discount, 25.00)

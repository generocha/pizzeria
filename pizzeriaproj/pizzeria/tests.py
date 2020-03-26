from django.test import TestCase
from .models import Pizza, PizzaType
from .views import index, gettypes, getpizzas
from .forms import PizzaTypeForm, PizzaForm
from django.urls import reverse
from django.contrib.auth.models import User

# ------------------------- Pizza Type Model --------------------


class PizzaTypeTest(TestCase):
    # set up one time sample data
    def setup(self):
        pizztype = PizzaType(typename='Vegetarian',
                             typedescription='This is pizza with no meat')
        return pizztype

    def test_typename(self):
        pizztype = self.setup()
        self.assertEqual(pizztype.typename,
                         'Vegetarian')

    def test_typedescription(self):
        pizztype = self.setup()
        self.assertEqual(pizztype.typedescription,
                         'This is pizza with no meat')

    def test_table(self):
        self.assertEqual(str(PizzaType._meta.db_table), 'pizzatype')

# ------------------------- Pizza Model --------------------


class PizzaTest(TestCase):
    # set up one time sample data
    def setup(self):
        type = PizzaType(typename='Vegetarian')
        pizz = Pizza(pizzaname='pizza1',
                     pizzatype=type,
                     pizzaprice='15.00',
                     pizzadescription='This is a pizza with no meat',
                     pizzaentrydate='2020-03-25')
        return pizz

    def test_string(self):
        pizz = self.setup()
        self.assertEqual(str(pizz), pizz.pizzaname)

    # test the discount property
    def test_discount(self):
        pizz = self.setup()
        self.assertEqual(pizz.memberdiscount(), 0.75)

    def test_type(self):
        pizz = self.setup()
        self.assertEqual(str(pizz.pizzatype), 'Vegetarian')

    def test_description(self):
        pizz = self.setup()
        self.assertEqual(str(pizz.pizzadescription),
                         'This is a pizza with no meat')

    def test_entrydate(self):
        pizz = self.setup()
        self.assertEqual(str(pizz.pizzaentrydate), '2020-03-25')

    def test_table(self):
        self.assertEqual(str(Pizza._meta.db_table), 'pizza')
# ------------------------- Index View --------------------


class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

# ------------------------- Get Pizzas View --------------------


class GetPizzasTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('pizzas'))
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        self.u = User.objects.create(username='myuser')
        self.type = PizzaType.objects.create(typename='Vegetarian')
        self.pizz = Pizza.objects.create(pizzaname='pizza1', pizzatype=self.type, user=self.u,
                                         pizzaprice=15.00, pizzaentrydate='2020-03-25', pizzadescription="a Pizza!")

    def test_pizza_detail_success(self):
        response = self.client.get(
            reverse('pizzadetails', args=(self.pizz.id,)))
        # Assert that self.post is actually returned by the post_detail view
        self.assertEqual(response.status_code, 200)

    def test_discount(self):
        discount = self.pizz.memberdiscount()
        self.assertEqual(discount, 0.75)


# ------------------------- Pizza Type Form--------------------


class PizzaType_Form_Test(TestCase):
    def test_typeform_is_valid(self):
        form = PizzaTypeForm(
            data={'typename': "Vegetarian", 'typedescription': "Pizza without meat"})
        self.assertTrue(form.is_valid())

    def test_typeform_minus_descript(self):
        form = PizzaTypeForm(data={'typename': "Vegetarian"})
        self.assertTrue(form.is_valid())

    def test_typeform_empty(self):
        form = PizzaTypeForm(data={'typename': ""})
        self.assertFalse(form.is_valid())

# ------------------------- Pizza Form--------------------


class Pizza_Form_Test(TestCase):
    def test_pizzaform_is_valid(self):
        form = PizzaForm(
            data={'pizzaname': "Super Veggie", 'pizzatype': "Meat", 'user': Bob, 'pizzaprice': 18.00, 'pizzaentrydate': "2020-03-25", 'pizzadescription': "Pizza without meat"})
        self.assertTrue(form.is_valid())

    def test_pizzaform_minus_descript(self):
        form = PizzaForm(data={'pizzaname': "Super Veggie"})
        self.assertTrue(form.is_valid())

    def test_pizzaname_empty(self):
        form = PizzaForm(data={'pizzaname': ""})
        self.assertFalse(form.is_valid())

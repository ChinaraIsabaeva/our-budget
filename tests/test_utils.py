from django.test import TestCase

from tests.base import BaseTestCase
from tests.factories import *


class AggregationTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.income_one = IncomeFactory(name='One', amount=1000)
        self.income_two = IncomeFactory(name='Two', amount=1000)

    def tearDown(self):
        super().tearDown()

    def test_incomes_summed(self):
        response = self.client.get('/')
        self.assertEqual(response.context['income'], 2000.00)
        self.assertEqual(response.context['available_amount'], 2000.00)

    def test_expenses_added(self):
        ExpenseFactory(name='rent', amount=900)
        ExpenseFactory(name='utility', amount=200)
        response = self.client.get('/')
        self.assertEqual(response.context['total_expenses'], 1100.00)
        self.assertEqual(response.context['available_amount'], 900.00)

    def test_space_added(self):
        SpaceFactory(name='vacation', monthly_replenishment=200)
        response = self.client.get('/')
        self.assertEqual(response.context['total_spaces'], 0.00)
        self.assertEqual(response.context['available_amount'], 1800.00)
        self.assertEqual(response.context['total_spaces_monthly'], 200.00)

    def test_spaces_monthly_payment(self):
        SpaceFactory(name='vacation', monthly_replenishment=200)
        SpaceFactory(
            name='health checkup',
            monthly_replenishment=50,
            current_amount=450
        )
        response = self.client.get('/')
        self.assertEqual(response.context['total_spaces'], 450.00)
        self.assertEqual(response.context['available_amount'], 1750.00)
        self.assertEqual(response.context['total_spaces_monthly'], 250.00)

    def test_all_calculation(self):
        ExpenseFactory(name='rent', amount=900)
        ExpenseFactory(name='utility', amount=200)
        SpaceFactory(
            name='vacation',
            monthly_replenishment=200,
            current_amount=400
        )
        SpaceFactory(
            name='health checkup',
            monthly_replenishment=50,
            current_amount=450
        )
        response = self.client.get('/')
        self.assertEqual(response.context['income'], 2000.00)
        self.assertEqual(response.context['total_spaces'], 850.00)
        self.assertEqual(response.context['total_spaces_monthly'], 250.00)
        self.assertEqual(response.context['total_expenses'], 1100.00)
        self.assertEqual(response.context['available_amount'], 650.00)

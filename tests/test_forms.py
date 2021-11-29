from django.contrib.auth.models import User
from django.test import TestCase, Client

from tests.factories import (
    IncomeFactory,
    ExpenseFactory,
    SpaceFactory
)

from spaces.models import Space
from expenses.models import Expense


class FormsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'test_user',
            'test_user@example.com',
            'randompass',
        )
        self.client = Client()
        self.client.force_login(
            self.user
        )

    def tearDown(self):
        super().tearDown()

    def test_space_create(self):
        response = self.client.post(
            '/spaces/create/',
            {
                'name': 'vacation',
                'monthly_replenishment': 300,
                'cash': False
            },
            follow=False
        )
        self.assertRedirects(
            response,
            expected_url='/spaces/all/',
            status_code=302
        )
        space = Space.objects.get(name='vacation')
        self.assertEquals(space.monthly_replenishment, 300)

    def test_expense_create(self):
        response = self.client.post(
            '/expenses/create/',
            {
                'name': 'rent',
                'amount': 950,
                'frequency': 'm'
            },
            follow=False
        )
        self.assertRedirects(
            response,
            expected_url='/expenses/all/',
            status_code=302
        )
        space = Expense.objects.get(name='rent')
        self.assertEquals(space.amount, 950)
        self.assertEquals(space.frequency, 'm')

    def test_space_update(self):
        SpaceFactory(name='random', id=5, monthly_replenishment=50)
        new_name = "New random name"
        response = self.client.post(
            '/spaces/5/update/',
            {
                'name': new_name,
                'monthly_replenishment': 100,
            },
            follow=False
        )
        self.assertRedirects(
            response,
            expected_url='/spaces/all/',
            status_code=302
        )
        space = Space.objects.get(id=5)
        self.assertEquals(space.monthly_replenishment, 100)
        self.assertEquals(space.name, new_name)

    def test_expense_update(self):
        ExpenseFactory(id=3, name='test_expense', amount=100)
        response = self.client.post(
            '/expenses/3/update/',
            {
                'name': 'test_expense',
                'amount': 100,
                'frequency': 'w'
            },
            follow=False
        )
        print(response)
        self.assertRedirects(
            response,
            expected_url='/expenses/all/',
            status_code=302
        )
        expense = Expense.objects.get(name='test_expense')
        self.assertEquals(expense.frequency, 'w')

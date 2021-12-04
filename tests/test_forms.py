from tests.base import BaseTestCase
from tests.factories import (
    IncomeFactory,
    ExpenseFactory,
    SpaceFactory
)

from core.models import Income
from spaces.models import Space
from expenses.models import Expense


class FormsTestCase(BaseTestCase):
    def tearDown(self):
        super().tearDown()

    def test_space_create(self):
        response = self.client.post(
            '/spaces/create/',
            {
                'name': 'vacation',
                'monthly_replenishment': 300
            },
            follow=False
        )
        self.assertRedirects(
            response,
            expected_url='/spaces/all/',
            status_code=302
        )
        space = Space.objects.get(name='vacation')
        self.assertEqual(space.monthly_replenishment, 300)

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
        expense = Expense.objects.get(name='rent')
        self.assertEqual(expense.amount, 950)
        self.assertEqual(expense.frequency, 'm')

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
        self.assertEqual(space.monthly_replenishment, 100)
        self.assertEqual(space.name, new_name)

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
        self.assertEqual(expense.frequency, 'w')

    def test_income_create(self):
        response = self.client.post(
            '/incomes/create/',
            {
                'name': 'salary',
                'amount': 2000,
            },
            follow=False
        )
        self.assertRedirects(
            response,
            expected_url='/incomes/all/',
            status_code=302
        )
        income = Income.objects.get(name='salary')
        self.assertEqual(income.amount, 2000)

    def test_income_update(self):
        IncomeFactory(id=2, name='additional_income', amount=1000)
        response = self.client.post(
            '/incomes/2/update/',
            {
                'name': 'test_expense',
                'amount': 1500,
            },
            follow=False
        )
        print(response)
        self.assertRedirects(
            response,
            expected_url='/incomes/all/',
            status_code=302
        )
        income = Income.objects.get(name='test_expense')
        self.assertEqual(income.amount, 1500)

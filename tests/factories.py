from factory.django import DjangoModelFactory


class IncomeFactory(DjangoModelFactory):
    class Meta:
        model = 'core.Income'


class ExpenseFactory(DjangoModelFactory):
    class Meta:
        model = 'expenses.Expense'


class SpaceFactory(DjangoModelFactory):
    class Meta:
        model = 'spaces.Space'

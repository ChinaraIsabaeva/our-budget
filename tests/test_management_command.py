from django.core.management import call_command
from freezegun import freeze_time

from tests.base import BaseTestCase
from tests.factories import (
    SpaceFactory
)

from spaces.models import Space


class CommandTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        SpaceFactory(
            name='test_space1',
            current_amount=100,
            monthly_replenishment=50
        )
        SpaceFactory(
            name='test_space2',
            monthly_replenishment=100
        )
        SpaceFactory(
            name='test_space3',
            current_amount=125,
            monthly_replenishment=100
        )

    def tearDown(self):
        super().tearDown()

    @freeze_time("2021-10-28")
    def test_monthly_script(self):
        args = []
        opts = {}

        call_command('monthly_script', *args, **opts)
        space_1 = Space.objects.get(name='test_space1')
        space_2 = Space.objects.get(name='test_space2')
        space_3 = Space.objects.get(name='test_space3')
        response = self.client.get('/')

        print(response)

        self.assertEqual(space_1.current_amount, 150.00)
        self.assertEqual(space_2.current_amount, 100.00)
        self.assertEqual(space_3.current_amount, 225.00)
        self.assertEqual(response.context['total_spaces'], 475.00)

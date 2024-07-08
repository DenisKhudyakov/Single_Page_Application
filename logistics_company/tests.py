from django.test import TestCase

from logistics_company.models import Registry


class RegistryTestCase(TestCase):

    def setUp(self):
        Registry.objects.create(
            date="25.11.2024",
            name="Logistics Company",
            count=5,
            distance=500,
        )

    def test_registry_creation(self):
        registry = Registry.objects.get(name="Logistics Company")
        self.assertEqual(registry.name, "Logistics Company")
        self.assertEqual(registry.distance, 500)

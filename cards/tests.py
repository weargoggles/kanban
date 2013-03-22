from django.test import TestCase
from cards.models import KanbanCard, TypeQuantity
from eve.models import Type


class KanbanCardTest(TestCase):
    def setUp(self):
        self.t = Type(id=34, volume=0.01)
        self.card = KanbanCard(typeid=self.t, size=100)
        self.same_size = TypeQuantity(self.card.typeid.id, 100)
        self.larger = TypeQuantity(self.card.typeid.id, 150)

    def test_normal_consumption(self):
        self.card.consume(self.same_size)
        self.assertEqual(self.card.quantity, 100)
        self.assertEqual(self.same_size.quantity, 0)

    def test_consumption_overflow(self):
        self.card.consume(self.larger)
        self.assertEqual(self.card.quantity, 100)
        self.assertEqual(self.larger.quantity, 50)

    def test_negative_consumption(self):
        self.card.consume(TypeQuantity(self.card.typeid.id, -1))
        self.assertEqual(self.card.quantity, 0)

    def test_typeid_checking(self):
        self.assertRaisesRegexp(TypeError, 'incorrect eve type',
                                self.card.consume, TypeQuantity(33, 1))
        self.assertRaisesRegexp(TypeError, 'incorrect eve type',
                                self.card.withdraw, TypeQuantity(33, 1))
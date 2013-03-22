from django.db import models

import eve.models
# Create your models here.


class TypeQuantity(object):
    """represents a typed lump of stuff from eve. generated and consumed by jobs and market orders"""

    def __init__(self, typeid, quantity):
        self.typeid = typeid
        self.quantity = quantity


class KanbanCard(models.Model):
    typeid = models.ForeignKey(eve.models.Type)
    size = models.PositiveIntegerField(default=1)
    quantity = models.PositiveIntegerField(default=0)

    def consume(self, other):
        if isinstance(other, TypeQuantity):
            if other.typeid == self.typeid.id:
                if self.quantity + other.quantity >= self.size:
                    other.quantity -= self.size - self.quantity
                    self.quantity = self.size
                elif other.quantity < 1:
                    pass
                else:
                    self.quantity += other.quantity
                    other.quantity = 0
            else:
                raise TypeError('The supplied %s has the incorrect eve type for combination with this %s' % (
                other.__class__, self.__class__))
        else:
            raise TypeError

    def withdraw(self, other):
        if isinstance(other, TypeQuantity):
            if other.typeid == self.typeid.id:
                if self.quantity - other.quantity < 0:
                    other.quantity -= self.quantity
                    self.quantity = 0
                else:
                    self.quantity += other.quantity
                    other.quantity = 0
            else:
                raise TypeError('The supplied %s has the incorrect eve type for combination with this %s' % (
                    other.__class__, self.__class__))
        else:
            raise TypeError
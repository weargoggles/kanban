from django.db import models
from eve import get_connection

class Type(models.Model):
    """represents one of Eve's types; supplied by a fixture. add fields as necessary."""
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, null=True)
    volume = models.DecimalField(max_digits=14, decimal_places=2)

    def fetch_name(self):
        """use eveapi to (try) to get the name for the type"""
        connection = get_connection()
        result = connection.eve.TypeName(ids=self.id)
        row = result.types.Get(self.id)
        self.name = row.typeName
        self.save()
        return self.name

    def __unicode__(self):
        return self.name if self.name else unicode(self.id)
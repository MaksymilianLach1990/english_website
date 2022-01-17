from django.db import models

# Create your models here.

class IrregularVerb(models.Model):
    name_pl = models.CharField(max_length=120)
    name_en_1 = models.CharField(max_length=120)
    spell_1 = models.CharField(max_length=120)
    name_en_2 = models.CharField(max_length=120)
    spell_2 = models.CharField(max_length=120)
    name_en_3 = models.CharField(max_length=120)
    spell_3 = models.CharField(max_length=120)

    def __str__(self):
        return self.name_pl + " " + self.name_en_1
from django.db import models

class uruntakip(models.Model):
    STATUS_CHOICES = [
    ('Pekin', 'Pekin'),
    ('Pekin-Ashkabat', 'Pekin-Ashkabat'),
    ('Ashkabat', 'Ashkabat'),
]
    cargoname = models.CharField(max_length=200, null=True, blank=True)
    cargono = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, blank=True, null=True, choices=STATUS_CHOICES, default='Pekin')

    def __str__(self):
        return self.cargoname + "--->" + self.cargono + "-->" + self.status
    



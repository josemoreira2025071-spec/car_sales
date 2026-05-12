from django.db import models

class Car(models.Model):
    FUEL_CHOICES = [
        ('gasolina', 'Gasolina'),
        ('diesel', 'Diesel'),
        ('eletrico', 'Elétrico'),
        ('hibrido', 'Híbrido'),
    ]
    
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.IntegerField(default=0, help_text='Quilometragem em km')
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES, default='gasolina')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
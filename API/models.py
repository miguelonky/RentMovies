from django.db import models

# Create your models here.
class movies(models.Model) :
    Id                 = models.AutoField(primary_key=True)
    Name               = models.CharField(max_length=100)
    Descripction       = models.CharField(max_length=250)
    QuantityAvaliable  = models.IntegerField()
    Price              = models.FloatField()
    Image              = models.ImageField(upload_to='tmp',blank=True,null=True)
    def __str__(self):
        return self.Name

class rentmovie(models.Model):
    STATUS_CHOICES = (
        (1, 'Available'),
        (2, 'Rented'),
        (3, 'Out-Stock'),
    )
    movie              = models.ForeignKey(movies,null=True,blank=True)
    RequireDate        = models.DateField()
    DeliveryDate       = models.DateField()
    Quantity           = models.IntegerField()
    Cost               = models.FloatField()
    Status             = models.IntegerField(choices=STATUS_CHOICES, default=1)
    User               = models.CharField(max_length=50)

    


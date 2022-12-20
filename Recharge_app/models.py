from django.db import models

class Plans(models.Model):
    operator = models.CharField(max_length=50,null=False)   # network name
    circle = models.CharField(max_length=50,null=False)     # Location of user
    price = models.IntegerField()
    data = models.CharField(max_length=50,null=False)
    validity = models.CharField(max_length=50,null=False)
    description = models.CharField(max_length=250,null=False)

    def __str__(self):
        return self.operator+' '+self.data

class Recharge(models.Model):
    number = models.CharField(max_length=15,null=False)
    plan = models.ForeignKey(Plans,on_delete=models.CASCADE,related_name='plan')
    is_active = models.BooleanField(default=False)
    validity_expire = models.DateField(null=False)

    def __str__(self):
        return self.number


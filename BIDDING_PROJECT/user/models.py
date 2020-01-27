from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    U_idno=models.AutoField(primary_key=True)
    U_name=models.CharField(max_length=50)
    U_contact=models.IntegerField(unique=True,default=False)
    U_email=models.EmailField(unique=True,default=False)
    U_password=models.CharField(max_length=10)
    U_status=models.CharField(max_length=10)
    U_DoR=models.DateField(auto_now_add=True)

class ProductModel(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    bprice = models.FloatField()
    info = models.TextField()
    image = models.ImageField(upload_to="product/")
    status = models.CharField(max_length=20)
    user =  models.ForeignKey(UserRegistration,on_delete=models.CASCADE)








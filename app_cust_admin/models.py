from django.db import models

# Create your models here.

class User_list(models.Model) :
    fullname = models.CharField(max_length=200,null=True)
    app_id = models.IntegerField(null=True)
    profession = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length = 254,null=True)
    status = models.BooleanField(default=True)

class Meta:
        app_label = 'app_cust_admin'


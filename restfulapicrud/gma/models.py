from django.db import models
# Create your models here.
class tbl_user(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)

# Create / INsert / Add - POST
# Retrieve / Fectch - GET
# Update / Edit - PUT
# Delete / Rempve - DELETE
from django.db import models
# Create your models here.

class InstType(models.Model):
    typins=models.CharField(max_length=60, unique=True, default='new1') # Bank, Email, Govt

    def __str__(self):
        return self.typins

class Institutions(models.Model):
    typofins=models.ForeignKey(InstType, on_delete = models.CASCADE)
    nameofinst = models.CharField(max_length=50, unique = 'True', default = 'new3')

    def __str__(self):
        return self.typofins + self.nameofinst
    
    
class AccHolder(models.Model):
    nameofholder = models.CharField(max_length=20, unique = True)
    emailid = models.EmailField(max_length=30, unique = True)
    mobno = models.IntegerField(max_length = 13, unique = True)    

class credntials(models.Model):
    noh = models.ForeignKey(AccHolder, on_delete = models.CASCADE)
    noi = models.ForeignKey(Institutions, on_delete = models.CASCADE)
    noit = models.ForeignKey(InstType, on_delete = models.CASCADE)
    uid = models.CharField(max_length = 16)
    pwd = models.CharField(max_length = 24)
    secq = models.CharField(max_length = 60, default = 'whats my favorite color')
    seca = models.CharField(max_length = 20, default = 'yellow')

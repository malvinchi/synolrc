from django.db import models
# Create your models here.

class InstType(models.Model):
#<<<<<<< HEAD
    #<<<<<<< HEAD
    typins=models.CharField(max_length=60, unique=True, default = 'new1') # Bank, Email, Govt
#    instname=models.CharField(max_length=30, unique=True, default='new2') # SBI, HOTMAIL, MVD
    #=======
  
  #  >>>>>>> 8ad0486d7348401599dc843b272a7b0522a7fdf5
#>>>>>>> 370ce4c8ef956905401ef28e7c1ceb00edb32511

    def __str__(self):
        return self.typins

class Institutions(models.Model):
    typofins=models.ForeignKey('InstType', on_delete = models.CASCADE)
    nameofinst = models.CharField(max_length=50, unique = 'True', default = 'new3' )

    def __str__(self):
        return (self.nameofinst)
    
    
class AccHolder(models.Model):
    nameofholder = models.CharField(max_length=20, unique = True)
    emailid = models.EmailField(max_length=30, unique = True)
    mobno = models.IntegerField(unique = True)    

class Credntials(models.Model):
    noh = models.ForeignKey('AccHolder', on_delete = models.CASCADE)
    noi = models.ForeignKey('Institutions', on_delete = models.CASCADE)
    noit = models.ForeignKey('InstType', on_delete = models.CASCADE)
    uid = models.CharField(max_length = 16)
    pwd = models.CharField(max_length = 24)
    secq = models.CharField(max_length = 60, default = 'whats my favorite color')
    seca = models.CharField(max_length = 20, default = 'yellow')

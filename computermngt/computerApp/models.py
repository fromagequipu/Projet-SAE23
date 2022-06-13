from datetime import datetime
from django.db import models

# Create your models here.
class Machine(models.Model):
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Serveur', ('Serveur - Simple Serveur to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
        ('Routeur', ('Routeur - Use to have Internet')),
    )


    id= models.AutoField(
                primary_key= True,
                editable=False)
    nom= models.CharField(
                max_length=15) 
    maintenanceDate = models.DateField(
                )
    mach= models.CharField(
                max_length=32,
                choices=TYPE,
                default='PC'
                ) 
    def __str__(self):
        return str(self.id) + "----" + self.nom
    
    def get_name(self):
        return str(self.id) + " " + self.nom
    

class Routeur(models.Model):
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Serveur', ('Serveur - Simple Serveur to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
        ('Routeur', ('Routeur - Use to have Internet')),
    )
    id= models.AutoField(
                primary_key= True,
                editable=False)
    nom= models.CharField(
                max_length=15) 
    maintenanceDate = models.DateField(
                )
    mach= models.CharField(
                max_length=32,
                choices=TYPE,
                default='PC'
                ) 
    def __str__(self):
        return str(self.id) + "----" + self.nom
    
    def get_name(self):
        return str(self.id) + " " + self.nom

class Switch(models.Model):
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Serveur', ('Serveur - Simple Serveur to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
        ('Routeur', ('Routeur - Use to have Internet')),
    )
    id= models.AutoField(
                primary_key= True,
                editable=False)
    nom= models.CharField(
                max_length=15) 
    maintenanceDate = models.DateField(
                )
    mach= models.CharField(
                max_length=32,
                choices=TYPE,
                default='PC'
                )
    def __str__(self):
        return str(self.id) + "----" + self.nom
    
    def get_name(self):
        return str(self.id) + " " + self.nom

class Serveur(models.Model):
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Serveur', ('Serveur - Simple Serveur to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
        ('Routeur', ('Routeur - Use to have Internet')),
    )
    id= models.AutoField(
                primary_key= True,
                editable=False)
    nom= models.CharField(
                max_length=15) 
    maintenanceDate = models.DateField(
                )
    mach= models.CharField(
                max_length=32,
                choices=TYPE,
                default='PC'
                )

    def __str__(self):
        return str(self.id) + "----" + self.nom
    
    def get_name(self):
        return str(self.id) + " " + self.nom



from django.db import models

# Model Author
class Author(models.Model):
    name = models.CharField(max_length=100)

# Model Book
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

# Model Album
class Album(models.Model):
    name = models.CharField(max_length=100)

# Model Song
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

# Model Vehicle
class Vehicle(models.Model):
    reg_no = models.IntegerField()

    def __str__(self):
        return str(self.reg_no)

# Model Car
class Car(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.vehicle)

# Menambahkan GeeksModel
class GeeksModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name




   
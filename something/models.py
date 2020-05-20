from django.db import models


class Order(models.Model):
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.description


class Customer(models.Model):
    given_name = models.CharField('given_name', max_length=30)
    last_name = models.CharField('last_name', max_length=30)

    def __str__(self):
        return self.given_name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = 'Customer'


class Worker(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = 'Workers'


class Manager(models.Model):
    cooks = models.ForeignKey(Worker, on_delete=models.CASCADE)
    chef_given_name = models.CharField('given name of manager', max_length=30)
    chef_last_name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = 'Managers'


class Advertising(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Advertising"
        verbose_name_plural = "Advertisings"


class Topic(models.Model):
    toppings = models.ManyToManyField(Advertising)

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = 'Topics'

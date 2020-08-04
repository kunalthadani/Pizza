from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Menu(models.Model):
	category_list = [('Regular Pizza','Regular Pizza'),('Sicilian Pizza','Sicilian Pizza'),('Subs','Subs'),('Pasta','Pasta'),('Salad','Salad'),('Dinner Platter','Dinner Platter')]

	category = models.CharField(max_length = 64, choices = category_list)
	name = models.CharField(max_length=64)
	size = models.CharField(max_length=64,blank = True)
	cost = models.FloatField()
	no_of_toppings = models.IntegerField()
	def __str__(self):
		return f"{self.id} {self.category} {self.name} {self.size}"

class Topping(models.Model):
	name = models.CharField(max_length=64)
	def __str__(self):
		return f'{self.name}'

class Addition(models.Model):
	name = models.CharField(max_length=64)
	cost = models.FloatField()
	def __str__(self):
		return f'{self.name}'

class Order(models.Model):
	placed_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "orders")
	total = models.FloatField()
	def __str__(self):
		return f"{self.id} {self.placed_by} {self.total}"

class Order_Items(models.Model):
	order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name= "order")
	menu = models.ForeignKey(Menu,on_delete=models.CASCADE,related_name="items")
	topping = models.ManyToManyField(Topping,blank = True, related_name = "toppings")
	addition = models.ManyToManyField(Addition,blank = True, related_name = "additions")
	quantity = models.IntegerField()
	def __str__(self):
		return f"{self.id} {self.order.placed_by} {self.menu} {self.topping} {self.addition}"

class Shopping_Cart(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "cart_order")
	menu = models.ForeignKey(Menu,on_delete=models.CASCADE,related_name = "cart_items")
	topping = models.ManyToManyField(Topping,related_name = "cart_toppings")
	addition = models.ManyToManyField(Addition,blank = True,related_name = "cart_additions")
	quantity = models.IntegerField()
	def __str__(self):
		return f"{self.id} {self.user} {self.menu} {self.topping} {self.addition}"	




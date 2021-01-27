from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductsData(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    Image_Link = models.ImageField(upload_to='images/')
    Product_Price=models.IntegerField()
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return (f'{self.Title}')
    

Payment_Method = (
    ("cash", "CASH"),
    ("paytm", "PAYTM"),
    ("card", "CARD"),
)

Order_Status = (
    ("new","NEW"),
    ("paid","PAID")
)
    
class OrdersData(models.Model):
    User_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Products= models.ManyToManyField(ProductsData)
    Total_Orders = models.IntegerField()
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    Order_Status = models.CharField(max_length=20,
                                    choices=Order_Status,
                                    default='new')
    Mode_of_Payment = models.CharField(
        max_length=30,
        choices=Payment_Method,
        default='cash'
    )
    
    def __str__(self):
        return f'{self.User_Id}'
    

class Orders_Items_Data(models.Model):
    Order_Id = models.ForeignKey(OrdersData, on_delete=models.CASCADE)
    Product_Id = models.ForeignKey(ProductsData, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Price = models.IntegerField()
    
    def price(self):
        return self.Product_Id.Product_Price

    def final_price(self):
        # print('product_id price:', self.Product_id.Product_Price)
        cost = self.Quantity * self.Product_Id.Product_Price
        # print('cost:', cost)
        return cost

    def _str_(self):
        return f"{self.Product_Id}"

from django.contrib import admin
from .models import ProductsData,Orders_Items_Data,OrdersData

# Register your models here.


class ProductDataAdmin(admin.ModelAdmin):
    list_display = ('id','Title', 'Description', 'Product_Price',
                    'Image_Link','Created_at','Updated_at')




class OrdersDataAdmin(admin.ModelAdmin):
    list_display = ('id','User_Id','Total_Orders', 'Order_Status',
                    'Mode_of_Payment', 'Created_at', 'Updated_at')


class Orders_Items_DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'Order_Id', 'Product_Id', 'Quantity',
                    'Price')

admin.site.register(ProductsData,ProductDataAdmin)
admin.site.register(OrdersData,OrdersDataAdmin)
admin.site.register(Orders_Items_Data,Orders_Items_DataAdmin)


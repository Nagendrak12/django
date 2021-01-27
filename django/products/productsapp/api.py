from productsapp.models import ProductsData,OrdersData,Orders_Items_Data
from rest_framework import viewsets, permissions
from .serilizers import ProductsDataAppSerializer,OrdersDataAppSerializer,Orders_Items_DataAppSerializer,UserSerilizer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter
from django.contrib.auth.models import User
from rest_framework.response import Response

#Rest Viewset


class ProductsDataAppViewSet(viewsets.ModelViewSet):
    queryset = ProductsData.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductsDataAppSerializer
    filter_backends=(SearchFilter,OrderingFilter)
    search_fields=('Title','Description')
    
class OrdersDataAppViewSet(viewsets.ModelViewSet):
    queryset = OrdersData.objects.all()
    # permissions_classes = [
    #     permissions.AllowAny
    # ]
    serializer_class = OrdersDataAppSerializer
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated]
    
    def list(self, request):
        # queryset = User.objects.all()
        order_obj = OrdersData.objects.filter(User_Id=request.user)
        serializer = OrdersDataAppSerializer(order_obj, many=True)
        return Response(serializer.data)

    def create(self, request,  *args, **kwargs):
        data = request.data
        # userinstance=User.objects.get(id=2)
        print('user:', request.user)
        # print('username:',userinstance)
        new_order = OrdersData.objects.create(
            User_Id=request.user, Total_Orders=data['Total_Orders'], Order_Status=data['Order_Status'], Mode_of_Payment=data['Mode_of_Payment'])
        new_order.save()
        orders_obj = OrdersData.objects.filter(User_Id=request.user)
        print('orders_obj:', orders_obj)
        for product in data['Products']:
            product_obj = ProductsData.objects.get(Title=product['Title'])
            new_order.Products.add(product_obj)
        serializer = OrdersDataAppSerializer(new_order)

        return Response(serializer.data)
    
    
class Orders_Items_DataAppViewSet(viewsets.ModelViewSet):
    queryset = Orders_Items_Data.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = Orders_Items_DataAppSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerilizer
    
    # def get_permissions(self):
    #     # allow non-authenticated user to create via POST
    #     return (permissions.AllowAny() if self.request.method == 'POST' else IsStaffOrTargetUser()),

    # def perform_create(self, serializer):
    #     password = make_password(self.request.data['password'])
    #     serializer.save(password=password)

    # def perform_update(self, serializer):
    #     password = make_password(self.request.data['password'])
    #     serializer.save(password=password)

from rest_framework import serializers
from .models import ProductsData,Orders_Items_Data,OrdersData
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class ProductsDataAppSerializer(serializers.ModelSerializer):
    image_url=  serializers.SerializerMethodField('get_image_url')
    
    class Meta:
        model=ProductsData
        fields  = ['id',
                    'Title',
                    'Description',
                    'Product_Price',
                    'Created_at',
                    'Updated_at',
                    'Image_Link',
                    'image_url'
        ]

    def get_image_url(self,new_obj):
        return new_obj.Image_Link.url
        

class OrdersDataAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersData
        fields = '__all__'
        depth=1


class Orders_Items_DataAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders_Items_Data
        fields = '__all__'

class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']
        extra_kwargs = {'password':{'write_only': True, 'required': True}}#to hide the password

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)   #token generates
        Token.objects.create(user=user) #token added in database
        return user

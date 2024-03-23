import decimal
from rest_framework import serializers
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist

from main.models import Cart, Catalog, Customer, Order, OrderStatus, Product, ProductImage, ProductInCart, ProductInOrder, ProductProperty, ProductRating
from main.email_functional import send_mail


class ProductPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductProperty
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductRating
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):

    product_images = ProductImageSerializer(many=True, read_only=True)
    his_rating = ProductRatingSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
    his_rating = ProductRatingSerializer(many=True, read_only=True)
    properties = ProductPropertySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name')
        instance.price = validated_data.get('price')
        instance.description = validated_data.get('description')
        instance.available = validated_data.get('available')
        instance.discount = validated_data.get('discount')
        instance.quantity = validated_data.get('quantity')

        instance.save()

        return instance


class ProductInitialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('code_1c', 'name', 'price', 'quantity')


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ('name', 'code_1c')


class ProductInCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCart
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    
    # products = ProductInCartSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        try:
            cart = Cart.objects.get(customer=validated_data.get('customer'))
            products_in_cart = ProductInCart.objects.filter(cart=cart).delete()

            for product in validated_data.get('cart'):
                print(product)

            cart.save()

            return cart
        
        except ObjectDoesNotExist:
            cart = Cart.objects.create(customer=validated_data.get('customer'))
            cart.save()
            return cart


class CustomerSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    cart = CartSerializer

    class Meta:
        model = Customer
        fields = ('id', 'email', 'first_name', 'last_name', 
                  'is_read_pd', 'phone_number', 'address', 'date_joined', 
                  'avatar', 'likes', 'is_staff', 'password', 'personal_discount', 'cart')

    def create(self, validated_data):
        user = super(CustomerSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        cart = Cart.objects.create(customer=user)
        cart.save()
        result = send_mail(self.context['request'], user)
        try:
            status = result.get('response')
            return user

        except KeyError:
            user.delete()
            raise serializers.ValidationError('This email do not exist!')


class OrderProductSerializer(serializers.ModelSerializer):

    product = ProductSerializer(read_only=True)    

    class Meta:
        model = ProductInOrder
        fields = '__all__'


class CreateOrderProductSerializer(serializers.ModelSerializer):   

    class Meta:
        model = ProductInOrder
        fields = '__all__'        


class OrderStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderStatus
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    order_products = OrderProductSerializer(many=True, read_only=True)
    #customer = CustomerSerializer(read_only=True)
    order_status = OrderStatusSerializer()
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_total_amount(self, obj) -> decimal:
        return obj.get_total_amount()






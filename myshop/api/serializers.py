import decimal
from rest_framework import serializers

from main.models import Cart, Catalog, Customer, Order, OrderStatus, Product, ProductImage, ProductInOrder, ProductRating
from main.email_functional import send_mail


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

    class Meta:
        model = Product
        fields = '__all__'


class ProductInitialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('code_1c', 'name', 'price', 'quantity')


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ('name', 'code_1c')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'email', 'first_name', 'last_name', 'is_read_pd', 'phone_number', 'address', 'date_joined', 'avatar', 'likes', 'is_staff', 'password')

    def create(self, validated_data):
        user = super(CustomerSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        print(self.context)
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






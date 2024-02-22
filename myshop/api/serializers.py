from rest_framework import serializers

from main.models import Cart, Catalog, Customer, Order, Product, ProductImage, ProductInOrder, ProductRating


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
    class Meta:
        model = Customer
        fields = ('id', 'email', 'first_name', 'last_name', 'is_read_pd', 'phone_number', 'address', 'date_joined', 'avatar', 'likes')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderProductSerializer(serializers.ModelSerializer):

    products_in_order = ProductSerializer(many=True, read_only=True)
    order_products = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = ProductInOrder
        fields = '__all__'





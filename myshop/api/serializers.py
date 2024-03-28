import decimal
from rest_framework import serializers
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist

from main.models import Cart, Catalog, Customer, Feedback, Order, OrderStatus, Product, ProductImage, ProductInCart, ProductInOrder, ProductProperty, ProductQuestion, ProductRating
from main.email_functional import send_mail
from django.db.models import Avg


class QuestionCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'avatar')


class ProductQuestionSerializer(serializers.ModelSerializer):

    customer = QuestionCustomerSerializer(read_only=True, required=False)

    class Meta:
        model = ProductQuestion
        fields = '__all__'

    
    def create(self, validated_data):
        question = ProductQuestion.objects.create(
            product = validated_data.get('product'),
            customer = self.context.get('request').user,
            question_text = validated_data.get('question_text'),
        )
        return question


class ProductQuestionsSerializer(serializers.ListSerializer):

    product = serializers.IntegerField()
    customer = QuestionCustomerSerializer(read_only=True, required=False)
    question_text = serializers.CharField(max_length=2000)
    created = serializers.DateTimeField()
    is_show = serializers.BooleanField()


    def to_representation(self, data):
        data = data.filter(is_show=True)
        return super(ProductQuestionsSerializer, self).to_representation(data)


class FeedbackCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id', 'phone_number', 'first_name', 'last_name', 'avatar')


class ProductFeedbackSerializer(serializers.ListSerializer):
    customer = FeedbackCustomerSerializer(read_only=True, required=False)
    product = serializers.IntegerField()
    post_at = serializers.DateTimeField()
    positive = serializers.CharField(max_length=1000)
    negative = serializers.CharField(max_length=1000)
    summary = serializers.CharField(max_length=1000)
    rating = serializers.IntegerField()
    is_show = serializers.BooleanField()
    ratingex = serializers.SerializerMethodField()

    def to_representation(self, data):
        data = data.filter(is_show=True)
        return super(ProductFeedbackSerializer, self).to_representation(data)


class FeedbackSerializer(serializers.ModelSerializer):

    customer = FeedbackCustomerSerializer(read_only=True, required=False)

    class Meta:
        model = Feedback
        fields = '__all__'


    def create(self, validated_data):
        if not self.context.get('request').user:
            return None
        feedback = Feedback.objects.create(
            product=validated_data.get('product'),
            customer=self.context.get('request').user,
            positive=validated_data.get('positive'),
            negative=validated_data.get('negative'),
            summary=validated_data.get('summary'),
            rating=validated_data.get('rating'),
        )

        return feedback


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
    id = serializers.IntegerField()
    product_feedbacks = ProductFeedbackSerializer(child=FeedbackSerializer(), required=False)
    rating = serializers.SerializerMethodField()
    num_ratings = serializers.SerializerMethodField()
    questions = ProductQuestionsSerializer(child=ProductQuestionSerializer(), required=False)

    class Meta:
        model = Product
        fields = '__all__'

    def get_rating(self, obj):
        feedbacks_avg = Feedback.objects.filter(product=obj).filter(is_show=True).aggregate(Avg('rating', default=0))
        return feedbacks_avg.get('rating__avg')
    
    def get_num_ratings(self, obj):
        feedbacks_count = Feedback.objects.filter(product=obj).filter(is_show=True).count()
        return feedbacks_count


    def update(self, instance, validated_data):

        instance.name = validated_data.get('name')
        instance.price = validated_data.get('price')
        instance.description = validated_data.get('description')
        instance.available = validated_data.get('available')
        instance.discount = validated_data.get('discount')
        instance.quantity = validated_data.get('quantity')
        instance.production_origin = validated_data.get('production_origin')

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

    product = ProductSerializer()

    class Meta:
        model = ProductInCart
        fields = '__all__'

    def create(self, validated_data):
        product = Product.objects.get(pk=validated_data.get('product').get('id'))
        product_in_cart = ProductInCart.objects.create(
            product = product,
            quantity = validated_data.get('quantity'),
            fixed_price = validated_data.get('fixed_price'),
            cart = validated_data.get('cart')
        )
        product_in_cart.save()
        return product_in_cart


class CartSerializer(serializers.ModelSerializer):
    
    products = ProductInCartSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    cart = CartSerializer(required=False, read_only=True)

    class Meta:
        model = Customer
        fields = ('id', 'email', 'first_name', 'last_name', 
                  'is_read_pd', 'phone_number', 'address', 'date_joined', 
                  'avatar', 'likes', 'is_staff', 'password', 'personal_discount', 'cart')

    def create(self, validated_data):
        cart = Cart.objects.create()
        validated_data['cart']=cart
        user = super(CustomerSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        #cart = Cart.objects.create(customer=user)
        #cart.save()
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

from rest_framework import serializers
from .models import Category, Cupcategory, PopularTopic, Instructor, Student, Course,Basket,Lesson, Review, Enrollment, Cart, CartItem, Order,Banner,Teacher
from django.contrib.auth.models import User
from .models import Profile, Product
from django.contrib.auth.forms import authenticate
from .models import Description,Feedback

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name',]


class CupcategorySerializer(serializers.ModelSerializer):
    class Meta:
         model = Cupcategory
         fields = ['id', 'name', 'category']


class PopularTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularTopic
        fields ='__all__'

class InstructorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Instructor
        fields = ['id', 'user', 'bio', 'profile_picture']



class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'user', 'profile_picture', 'courses_enrolled']


class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    instructor = InstructorSerializer()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'category', 'instructor', 'price', 'created_at', 'updated_at', 'thumbnail', 'language', 'duration']


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ['id', 'student', 'course']


class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Lesson
        fields = ['id', 'course', 'title', 'video', 'duration', 'content']


class ReviewSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    course = CourseSerializer()

    class Meta:
        model = Review
        fields = ['id', 'course', 'student', 'rating', 'comment', 'created_at']


class EnrollmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    course = CourseSerializer()

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'date_enrolled', 'progress']


class CartItemSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'course', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(read_only=True)
    courses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'student', 'courses']


class OrderSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Order
        fields = ['id', 'student', 'total_amount', 'date_ordered', 'is_paid']


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'



class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('bio','user', 'first_name', 'last_name', 'birth_date','headline', 'description')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError("Invalid username or password.")
        return user


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ['id', 'user', 'text']  # или любые другие поля, которые хотите сериализовать

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Feedback
        fields = ['id', 'content', 'rating', 'created_at', 'user']
        read_only_fields = ['id', 'created_at', 'user']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
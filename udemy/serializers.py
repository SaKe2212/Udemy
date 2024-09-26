from rest_framework import serializers
from .models import Category, Instructor, Student, Course, Lesson, Review, Enrollment, Cart, CartItem, Order
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class InstructorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Instructor
        fields = ['id', 'user', 'bio', 'profile_picture', 'rating', 'experience']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['id', 'user', 'profile_picture', 'courses_enrolled']


class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    instructor = InstructorSerializer()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'category', 'instructor', 'price', 'created_at', 'updated_at', 'thumbnail', 'language', 'duration']


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
    student = StudentSerializer()
    courses = CartItemSerializer(source='cartitem_set', many=True)

    class Meta:
        model = Cart
        fields = ['id', 'student', 'courses']


class OrderSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Order
        fields = ['id', 'student', 'total_amount', 'date_ordered', 'is_paid']

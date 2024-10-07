from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)



    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cupcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cats')

    def __str__(self):
        return self.name

class PopularTopic(models.Model):
    name = models.CharField(max_length=100)
    Cupcategory = models.ForeignKey(Cupcategory, on_delete=models.CASCADE, related_name='popular_topics')

    def __str__(self):
        return self.name

class Instructor(models.Model):
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='instructors/')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    experience = models.CharField(max_length=255)
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.OneToOneField('udemy.CustomUser', on_delete=models.CASCADE)


class Student(models.Model):
    profile_picture = models.ImageField(upload_to='students/')
    courses_enrolled = models.ManyToManyField('Course', related_name='students_enrolled', blank=True)
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.OneToOneField('udemy.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(upload_to='course_thumbnails/')
    language = models.CharField(max_length=50)
    duration = models.DurationField()

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='lessons/')
    duration = models.DurationField()
    content = models.TextField()

    def __str__(self):
        return self.title

class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.student.user.username} for {self.course.title}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # progress in percentage

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.course.title}"

class Cart(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='carts')
    courses = models.ManyToManyField(Course, through='CartItem', related_name='carts')

    def __str__(self):
        return f"{self.student.user.username}'s Cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.course.title} in {self.cart.student.user.username}'s cart"

class Order(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='orders')
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.student.user.username}"

class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banners/')
    link = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

User = get_user_model()  # Получаем пользовательскую модель

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)  # Поле для даты рождения

    def __str__(self):
        return f"{self.user.username}'s Profile"

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .models import CustomUser, Profile, Description, Category, Cupcategory, PopularTopic, Instructor, Student, Course, Basket, Lesson, Review, Enrollment, Cart, CartItem, Order, Banner, Teacher
from .serializers import CategorySerializer, CupcategorySerializer, PopularTopicSerializer, InstructorSerializer, StudentSerializer, CourseSerializer, BasketSerializer, LessonSerializer, ReviewSerializer, EnrollmentSerializer, CartSerializer, CartItemSerializer, OrderSerializer, BannerSerializer, TeacherSerializer, ProfileSerializer, UserSerializer, LoginSerializer
from .forms import SignUpForm, ProfileForm, LoginForm
from rest_framework.generics import RetrieveUpdateAPIView
from django.views.generic import TemplateView



# API views
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CupcategoryViewSet(viewsets.ModelViewSet):
    queryset = Cupcategory.objects.all()
    serializer_class = CupcategorySerializer

class PopularTopicViewSet(viewsets.ModelViewSet):
    queryset = PopularTopic.objects.all()
    serializer_class = PopularTopicSerializer

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    permission_classes = [permissions.IsAuthenticated]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BasketListViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(student__user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(student__user=request.user)
        serializer = self.get_serializer(cart)
        return Response(serializer.data)

class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__student__user=self.request.user)

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(student__user=self.request.user)
        serializer.save(cart=cart)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class BannerListCreateView(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

# User registration API
class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

# User login API
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            return Response({"message": "User logged in successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Profile API
class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

class UpdateUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        new_email = data.get("email")
        if new_email and new_email != user.email:
            user.email = new_email
        new_username = data.get("username")
        if new_username and new_username != user.username:
            user.username = new_username
        new_password = data.get("password")
        confirm_password = data.get("confirm_password")
        if new_password and new_password == confirm_password:
            user.set_password(new_password)
            update_session_auth_hash(request, user)
        elif new_password and new_password != confirm_password:
            return Response({"error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)
        user.save()
        return Response({"message": "Profile updated successfully"}, status=status.HTTP_200_OK)

# User data API
class UserDataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

# Description API
class UpdateDescriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        description = Description.objects.first()
        serializer = DescriptionSerializer(description)
        return Response(serializer.data)

    def post(self, request):
        description = Description.objects.first()
        new_text = request.data.get("description")
        if new_text:
            description.text = new_text
            description.save()
            return Response({"message": "Description updated successfully"})
        return Response({"error": "Description not updated"}, status=status.HTTP_400_BAD_REQUEST)

# Views for registration, login, and profile management
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            profile, created = Profile.objects.get_or_create(user=user)
            if created:
                profile.some_field = 'default_value'
                profile.save()
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, 'udemy1/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = CustomUser.objects.filter(username=username).first()
            if user is None:
                messages.error(request, 'User does not exist. Please register first.')
                return redirect('register')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')
        else:
            messages.error(request, 'Form is not valid')
    else:
        form = LoginForm()
    return render(request, 'udemy1/login.html', {'form': form})

class HomeView(TemplateView):
    template_name = 'udemy1/home.html'

def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'udemy1/profile.html', {'form': form, 'profile': profile})

def update_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        if any(field in request.POST for field in ['headline', 'description', 'email', 'first_name', 'last_name']):
            profile.headline = request.POST.get('headline', profile.headline)
            profile.description = request.POST.get('description', profile.description)
            profile.user.email = request.POST.get('email', profile.user.email)
            profile.user.first_name = request.POST.get('first_name', profile.user.first_name)
            profile.user.last_name = request.POST.get('last_name', profile.user.last_name)
            profile.user.save()
            profile.save()
            return redirect('home')
    return render(request, 'udemy1/update_profile.html', {'profile': profile})

@login_required
def change_name(request):
    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        if new_name:
            request.user.last_name = new_name
            request.user.save()
            request.name.save()
        return redirect('update_profile')
    return render(request, 'udemy1/change_name.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password == confirm_password:
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Your password has been changed successfully.")
            return redirect('update_profile')
        else:
            messages.error(request, "Passwords do not match. Please try again.")
    return render(request, 'udemy1/change_password.html')

@login_required
def change_email(request):
    if request.method == 'POST':
        new_email = request.POST.get('new_email')
        if new_email and new_email != request.user.email:
            request.user.email = new_email
            request.user.save()
            messages.success(request, 'Your email has been updated!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or email is the same as the current one.')
    return render(request, 'udemy1/change_email.html')

@login_required
def change_headline(request):
    if request.method == "POST":
        profile = request.user.profile
        profile.headline = request.POST.get('headline')
        profile.save()
        return redirect('edit_profile')
    return render(request, 'change_headline.html')
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


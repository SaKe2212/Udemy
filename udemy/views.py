from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .models import CustomUser, Profile, Description, Category, Cupcategory, PopularTopic, Instructor, Student, Course, Basket, Lesson, Review, Enrollment, Cart, CartItem, Order, Banner, Teacher
from .serializers import CategorySerializer, CupcategorySerializer, PopularTopicSerializer, InstructorSerializer, StudentSerializer, CourseSerializer, BasketSerializer, LessonSerializer, ReviewSerializer, EnrollmentSerializer, CartSerializer, CartItemSerializer, OrderSerializer, BannerSerializer, TeacherSerializer, ProfileSerializer, UserSerializer, LoginSerializer
from .forms import SignUpForm, ProfileForm, LoginForm
from rest_framework.generics import RetrieveUpdateAPIView
from django.views.generic import TemplateView
from .forms import FeedbackForm,ProductForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Feedback
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import FeedbackSerializer, DescriptionSerializer
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .forms import ProductForm
from .serializers import ProductSerializer


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

@csrf_exempt
def profile_view(request):
    profile = Profile.objects.get(user=request.user)

    if request.headers.get('Content-Type') == 'application/json':
        if request.method == 'GET':
            return JsonResponse({
                'username': request.user.username,
                'email': profile.email,
                'first_name': profile.first_name,
                'last_name': profile.last_name,
                'bio': profile.bio,  # Пример дополнительного поля
            })
        elif request.method == 'POST':
            try:
                data = json.loads(request.body)
                profile.first_name = data.get('first_name', profile.first_name)
                profile.last_name = data.get('last_name', profile.last_name)
                profile.bio = data.get('bio', profile.bio)  # Пример
                profile.save()
                return JsonResponse({'status': 'success', 'message': 'Profile updated successfully!'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    # Обработка HTML-страницы
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
        return redirect('update_profile')
    return render(request, 'change_headline.html')



class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# HTML views
@login_required
def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')  # All feedbacks
    return render(request, 'udemy1/feedback_list.html', {'feedbacks': feedbacks})

@login_required
def create_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()
    return render(request, 'udemy1/create_feedback.html', {'form': form})

@login_required
def delete_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id, user=request.user)
    feedback.delete()
    return redirect('feedback_list')

@login_required
def update_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id, user=request.user)
    if request.method == 'POST':
        feedback.content = request.POST.get('content')
        feedback.rating = int(request.POST.get('rating', feedback.rating))
        feedback.save()
        return redirect('feedback_list')
    return render(request, 'udemy1/update_feedback.html', {'feedback': feedback})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feedback_list_api(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    serializer = FeedbackSerializer(feedbacks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_feedback_api(request):
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_feedback_api(request, feedback_id):
    feedback = Feedback.objects.filter(id=feedback_id, user=request.user).first()
    if not feedback:
        return Response({'error': 'Feedback not found or not authorized'}, status=status.HTTP_404_NOT_FOUND)
    serializer = FeedbackSerializer(feedback, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_feedback_api(request, feedback_id):
    feedback = Feedback.objects.filter(id=feedback_id, user=request.user).first()
    if not feedback:
        return Response({'error': 'Feedback not found or not authorized'}, status=status.HTTP_404_NOT_FOUND)
    feedback.delete()
    return Response({'message': 'Feedback deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# HTML Views
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product/add_product.html', {'form': form})

def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/update_product.html', {'form': form, 'product': product})


@csrf_exempt
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()

        if request.headers.get('Accept') == 'application/json':
            return JsonResponse({'message': 'Product deleted successfully.'}, status=200)
        else:
            return redirect('product_list')
    return JsonResponse({'error': 'Invalid request method. Use POST.'}, status=405)

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

# API Views
@api_view(['GET', 'POST'])
def api_product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def api_product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

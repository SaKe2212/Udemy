from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView
from .serializers import *
from .forms import SignUpForm
from .models import Profile
from django.shortcuts import render, redirect
from .forms import ProfileForm



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



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            Profile.objects.get_or_create(user=user)

            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'udemy1/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request, 'udemy1/login.html', {'form': form})


class HomeView(TemplateView):
    template_name = 'udemy1/home.html'


def profile_view(request):
    profile = Profile.objects.get(user=request.user)  # Получаем профиль текущего пользователя
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)  # Создаем форму с данными POST
        if form.is_valid():
            form.save()  # Сохраняем данные профиля
            return redirect('home')  # Редиректим на главную страницу после успешного сохранения
    else:
        form = ProfileForm(instance=profile)  # Если это GET-запрос, просто отображаем форму с текущими данными

    return render(request, 'udemy1/profile.html', {'form': form, 'profile': profile})


def update_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        # Если форма отправлена, сохраняем изменения
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу (укажите правильный url name для 'home')
    else:
        # Если GET запрос, показываем форму с текущими данными профиля
        form = ProfileForm(instance=profile)

    return render(request, 'udemy1/update_profile.html', {'form': form, 'profile': profile})


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



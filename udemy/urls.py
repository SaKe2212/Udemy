from django.urls import path
from .views import (
    CategoryViewSet, CupcategoryViewSet, PopularTopicViewSet, InstructorViewSet,
    StudentViewSet, CourseViewSet, LessonViewSet, ReviewViewSet, EnrollmentViewSet,
    CartViewSet, CartItemViewSet, OrderViewSet, BannerListCreateView,
    BasketListViewSet, TeacherViewSet, register, login_view, profile_view, update_profile, HomeView
)

from .views import ( change_name, change_password, change_email, RegisterView, LoginView, ProfileView, UserDataView,change_headline, update_description)
urlpatterns = [
    # Category paths
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category_detail'),

    # Cupcategory paths
    path('cupcategories/', CupcategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='cupcategory_list'),
    path('cupcategories/<int:pk>/', CupcategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='cupcategory_detail'),

    # Popular Topics paths
    path('popularTopics/', PopularTopicViewSet.as_view({'get': 'list', 'post': 'create'}), name='popular_topic_list'),
    path('popularTopics/<int:pk>/', PopularTopicViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='popular_topic_detail'),

    # Instructor paths
    path('instructors/', InstructorViewSet.as_view({'get': 'list', 'post': 'create'}), name='instructor_list'),
    path('instructors/<int:pk>/', InstructorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='instructor_detail'),

    # Student paths
    path('students/', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student_list'),
    path('students/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='student_detail'),

    # Course paths
    path('courses/', CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='course_list'),

    path('courses/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='course_detail'),

    # Basket paths
    path('baskets/', BasketListViewSet.as_view({'get': 'list', 'post': 'create'}), name='basket_list'),

    # Lesson paths
    path('lessons/', LessonViewSet.as_view({'get': 'list', 'post': 'create'}), name='lesson_list'),
    path('lessons/<int:pk>/', LessonViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='lesson_detail'),

    # Review paths
    path('reviews/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('reviews/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='review_detail'),

    # Enrollment paths
    path('enrollments/', EnrollmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='enrollment_list'),
    path('enrollments/<int:pk>/', EnrollmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='enrollment_detail'),

    # Cart paths
    path('cart/', CartViewSet.as_view({'get': 'retrieve'}), name='cart_detail'),
    path('cart_items/', CartItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='cart_item_list'),
    path('cart_items/<int:pk>/', CartItemViewSet.as_view({'put': 'update', 'delete': 'destroy'}), name='cart_item_detail'),

    # Order paths
    path('orders/', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='order_list'),
    path('orders/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='order_detail'),

    # Banner path
    path('banners/', BannerListCreateView.as_view(), name='banner_list_create'),

    # Auth paths
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),

    # Home path
    path('', HomeView.as_view(), name='home'),

    # Profile paths
    path('profile/', profile_view, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('change-name/', change_name, name='change_name'),
    path('change-password/', change_password, name='change_password'),
    path('change_email/', change_email, name='change_email'),
    path('change_headline/', change_headline, name='change_headline'),
    path('change_description/', update_description, name='change_description'),
    # Teacher paths
    path('teachers/', TeacherViewSet.as_view({'get': 'list', 'post': 'create'}), name='teacher_list'),
    path('teachers/<int:pk>/', TeacherViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='teacher_detail'),

    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/profile/', ProfileView.as_view(), name='profile'),
    path('api/user-data/', UserDataView.as_view(), name='user-data'),

]

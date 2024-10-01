from django.urls import path
from .views import (
    CategoryViewSet, CupcategoryViewSet, PopularTopicViewSet, InstructorViewSet,
    StudentViewSet, CourseViewSet, LessonViewSet, ReviewViewSet, EnrollmentViewSet,
    CartViewSet, CartItemViewSet, OrderViewSet, BannerListCreateView, BasketListViewSet
)

urlpatterns = [

    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category_detail'),

    path('cupcategories/', CupcategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='cupcategory_list'),
    path('cupcategories/<int:pk>/', CupcategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='cupcategory_detail'),

    path('popularTopics/', PopularTopicViewSet.as_view({'get': 'list', 'post': 'create'}), name='popular_topic_list'),
    path('popularTopics/<int:pk>/', PopularTopicViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='popular_topic_detail'),

    path('instructors/', InstructorViewSet.as_view({'get': 'list', 'post': 'create'}), name='instructor_list'),
    path('instructors/<int:pk>/', InstructorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='instructor_detail'),

    path('students/', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student_list'),
    path('students/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='student_detail'),

    path('courses/', CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='course_list'),
    path('courses/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='course_detail'),

    path('baskets/', BasketListViewSet.as_view({'get': 'list', 'post': 'create'}), name='course_list'),

    path('lessons/', LessonViewSet.as_view({'get': 'list', 'post': 'create'}), name='lesson_list'),
    path('lessons/<int:pk>/', LessonViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='lesson_detail'),

    path('reviews/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('reviews/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='review_detail'),

    path('enrollments/', EnrollmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='enrollment_list'),
    path('enrollments/<int:pk>/', EnrollmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='enrollment_detail'),

    path('cart/', CartViewSet.as_view({'get': 'retrieve'}), name='cart_detail'),
    path('cart_items/', CartItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='cart_item_list'),
    path('cart_items/<int:pk>/', CartItemViewSet.as_view({'put': 'update', 'delete': 'destroy'}), name='cart_item_detail'),

    path('orders/', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='order_list'),
    path('orders/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='order_detail'),

    path('banners/', BannerListCreateView.as_view(), name='banner_list_create'),
]

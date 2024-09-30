from django.urls import path
from .views import *

urlpatterns = [


    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category_detail'),

    path('cats/', CatViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('cats/<int:pk>/', CatViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),name='category_detail'),

    path('popularTopics/', PopularTopicViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('popularTopics/<int:pk>/', PopularTopicViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),

    path('instructors/', InstructorViewSet.as_view({'get': 'list', 'post': 'create'}), name='instructor_list'),
    path('instructors/<int:pk>/', InstructorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='instructor_detail'),

    path('students/', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student_list'),
    path('students/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='student_detail'),

    path('/courses', CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='course_list'),
    path('courses/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='course_detail'),

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

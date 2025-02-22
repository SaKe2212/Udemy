from django.urls import path, include
from .views import (
    CategoryViewSet, CupcategoryViewSet, PopularTopicViewSet, InstructorViewSet,
    StudentViewSet, CourseViewSet, LessonViewSet, ReviewViewSet, EnrollmentViewSet,
    CartViewSet, CartItemViewSet, OrderViewSet, BannerListCreateView,
    BasketListViewSet, TeacherViewSet, register, login_view, profile_view, update_profile, HomeView, UserDataView
     , create_payment, payment_page, LogoutView, 
)
from . import views
from rest_framework.routers import DefaultRouter
from .views import ( change_name, change_password, change_email, RegisterView, LoginView, ProfileView,update_feedback,delete_feedback,
create_feedback,feedback_list,feedback_list_api,delete_feedback_api,create_feedback_api,update_feedback_api, ExpenseViewSet

                     )
router = DefaultRouter()

# Подключаем маршруты для ViewSet'ов
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'cupcategories', CupcategoryViewSet, basename='cupcategory')
router.register(r'popular-topics', PopularTopicViewSet, basename='popular-topic')
router.register(r'instructors', InstructorViewSet, basename='instructor')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'baskets', BasketListViewSet, basename='basket')
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'cart-items', CartItemViewSet, basename='cart-item')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'expenses', ExpenseViewSet, basename='expense')

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
    path('logout/', views.logout_view, name='logout'),

    # Home path
    path('', HomeView.as_view(), name='home'),

    # Profile paths
    path('profile/', profile_view, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('change-name/', change_name, name='change_name'),
    path('change-password/', change_password, name='change_password'),
    path('change_email/', change_email, name='change_email'),

    # Teacher paths
    path('teachers/', TeacherViewSet.as_view({'get': 'list', 'post': 'create'}), name='teacher_list'),
    path('teachers/<int:pk>/', TeacherViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='teacher_detail'),

    #  Api
    path('api/product_list/', views.api_product_list, name='api_product_list'),
    path('api/<int:product_id>/', views.api_product_detail, name='api_product_detail'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login/'),
    path('api/profile/', views.ProfileView.as_view(), name='api/profile'),
    path('api/user-data/', UserDataView.as_view(), name='user-data'),
    path('api/', include(router.urls)),
    path('api/banners/', BannerListCreateView.as_view(), name='banner-list-create'),
    path('api/feedbacks/', feedback_list_api, name='feedback_list_api'),
    path('api/feedbacks/create/', create_feedback_api, name='create_feedback_api'),
    path('api/feedbacks/<int:feedback_id>/update/', update_feedback_api, name='update_feedback_api'),
    path('api/feedbacks/<int:feedback_id>/delete/', delete_feedback_api, name='delete_feedback_api'),
    path('api/add-product/', views.api_add_product, name='api_add_product'),
    path('api/logout/', LogoutView.as_view(), name='logout/'),

    path('feedbacks/', feedback_list, name='feedback_list'),
    path('feedbacks/create/', create_feedback, name='create_feedback'),
    path('feedbacks/<int:feedback_id>/update/', update_feedback, name='update_feedback'),
    path('feedbacks/<int:feedback_id>/delete/', delete_feedback, name='delete_feedback'),

    path('add_product/', views.add_product, name='add_product'),
    path('products/<int:product_id>/update/', views.update_product, name='update_product'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('product_list/', views.product_list, name='product_list'),

#     оплат
    path("payment/", views.payment_page, name="checkout_page"),
    path("create-checkout-session/", views.create_payment, name="create_checkout_session"),
    path("payment-success/", views.payment_success, name="payment_success"),
    path("create-payment/", views.create_payment, name="create_payment"),
]

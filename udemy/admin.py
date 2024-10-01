from django.contrib import admin
from .models import (
    Category, Cupcategory, PopularTopic, Course, Lesson, Review, Banner,
    Instructor, Student, Enrollment, Cart, CartItem, Order
)
from modeltranslation.admin import TranslationAdmin

class Media:
    js = (
        'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
        'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        'modeltranslation/js/tabbed_translation_fields.js',
    )
    css = {
        'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
    }


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    class Media(Media):
        pass

@admin.register(Cupcategory)
class CupcategoryAdmin(TranslationAdmin):
    class Media(Media):
        pass

@admin.register(PopularTopic)
class PopularTopicAdmin(TranslationAdmin):
    class Media(Media):
        pass

@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    class Media(Media):
        pass

@admin.register(Lesson)
class LessonAdmin(TranslationAdmin):
    class Media(Media):
        pass

@admin.register(Review)
class ReviewAdmin(TranslationAdmin):
    class Media(Media):
        pass

@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    class Media(Media):
        pass


admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)

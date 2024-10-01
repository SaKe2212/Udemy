from .models import Category, Cupcategory, PopularTopic, Course, Lesson, Review, Banner
from modeltranslation.translator import TranslationOptions, register

from modeltranslation.translator import TranslationOptions, register
from .models import Category

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(Cupcategory)
class CupcategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(PopularTopic)
class PopularTopicTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment',)

@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title',)

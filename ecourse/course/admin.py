from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Course, User, Tag, Lesson


# Register your models here.

class LessonTagInlineAdmin(admin.TabularInline):
    model = Lesson.tags.through

class CourseTagInlineAdmin(admin.TabularInline):
    model = Course.tags.through

class TagAdmin(admin.ModelAdmin):
    inlines = [LessonTagInlineAdmin, CourseTagInlineAdmin]

class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject']
    list_filter = ['id', 'subject']
    search_fields = ['subject']

    inlines = [LessonTagInlineAdmin, ]

    readonly_fields = ['avatar']

    def avatar(self, obj):
        if obj:
            return mark_safe(
                '<img src="/{url}" width="120" />'.format(url=obj.image.name)
            )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['id']

class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Course
        fields = '__all__'

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject']
    list_filter = ['id', 'subject']
    search_fields = ['subject']

    inlines = [CourseTagInlineAdmin, ]

    form = CourseForm

    readonly_fields = ['avatar']
    def avatar(self, obj):
        if obj:
            return mark_safe(
                '<img src="/{url}" width="120" />'.format(url=obj.image.name)
            )



admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Lesson)
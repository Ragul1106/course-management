from django.contrib import admin
from .models import Course, Teacher, Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'lesson_count', 'teacher_count']
    search_fields = ['title', 'description']
    list_filter = ['created_at', 'teachers']
    
    def lesson_count(self, obj):
        return obj.lessons.count()
    lesson_count.short_description = 'Lessons'
    
    def teacher_count(self, obj):
        return obj.teachers.count()
    teacher_count.short_description = 'Teachers'

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'course_count', 'created_at']
    search_fields = ['name', 'email']
    filter_horizontal = ['courses']
    
    def course_count(self, obj):
        return obj.courses.count()
    course_count.short_description = 'Courses'

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order', 'created_at']
    list_filter = ['course', 'created_at']
    search_fields = ['title', 'content', 'course__title']
    ordering = ['course', 'order']

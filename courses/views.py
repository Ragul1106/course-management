from django.shortcuts import render, get_object_or_404
from .models import Course, Teacher, Lesson

def course_list(request):
    courses = Course.objects.all().prefetch_related('teachers', 'lessons')
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lessons = course.lessons.all()
    teachers = course.teachers.all()
    
    context = {
        'course': course,
        'lessons': lessons,
        'teachers': teachers,
    }
    return render(request, 'courses/course_detail.html', context)

def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    course = lesson.course
    other_lessons = course.lessons.exclude(pk=pk)
    
    context = {
        'lesson': lesson,
        'course': course,
        'other_lessons': other_lessons,
    }
    return render(request, 'courses/lesson_detail.html', context)

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    courses = teacher.courses.all().prefetch_related('lessons')
    
    context = {
        'teacher': teacher,
        'courses': courses,
    }
    return render(request, 'courses/teacher_detail.html', context)

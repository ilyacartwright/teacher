from django.contrib import admin
from .models import Corses, LevelCourses, ThemesLevelCourses


class LevelCoursesInline(admin.TabularInline):
    model = LevelCourses

class ThemesLevelCoursesInline(admin.TabularInline):
    model = ThemesLevelCourses

@admin.register(Corses)
class CorsesAdmin(admin.ModelAdmin):
    inlines = [LevelCoursesInline, ThemesLevelCoursesInline, ]
    list_display = ('title', 'abbr')
from django.contrib import admin
from .models import Exercise
from adminsortable.admin import SortableAdmin


class ExerciseAdmin(SortableAdmin):
    list_display = ("id", "title", "in_prog", "speed", "repetitions", "media_file", "order")
    list_filter = ("in_prog", "speed", "repetitions")
    list_editable = ("in_prog", "speed", "repetitions")
    list_display_links = ("title",)

admin.site.register(Exercise, ExerciseAdmin)

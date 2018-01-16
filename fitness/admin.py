from django.contrib import admin
from .models import Exercise
from adminsortable.admin import SortableAdmin


class ExerciseAdmin(SortableAdmin):
    list_display = ("title", "in_prog", "speed", "repetitions", "hold_position", "media_file", "order")
    list_filter = ("in_prog", "speed", "repetitions", "hold_position")
    list_editable = ("in_prog", "speed", "repetitions", "hold_position")
    list_display_links = ("title",)

admin.site.register(Exercise, ExerciseAdmin)

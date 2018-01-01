from django.db import models
from adminsortable.models import SortableMixin

class Exercise(SortableMixin):
    title = models.CharField(max_length=100)
    text = models.TextField()
    speed = models.DecimalField(max_digits=4, decimal_places=2)
    repetitions = models.IntegerField()
    media_file = models.FileField(upload_to='fitness')
    in_prog = models.BooleanField()

    # Use https://github.com/alsoicode/django-admin-sortable for sorting
    class Meta:
        verbose_name = 'Exercise'
        verbose_name_plural = 'Exercises'
        ordering = ['order']

    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    # Show title in admin page
    def __str__(self):
        return self.title

    # Get next in_prog
    def prog_next(self):
        next = self.__class__.objects.filter(in_prog=True).filter(order__gt=self.order)
        try:
            return next[0]
        except IndexError:
            return False

    # Get prev in_prog
    def prog_prev(self):
        prev = self.__class__.objects.filter(in_prog=True).filter(order__lt=self.order).order_by('-order')
        try:
            return prev[0]
        except IndexError:
            return False

    # Get next NOT in_prog
    def notprog_next(self):
        next = self.__class__.objects.filter(in_prog=False).filter(order__gt=self.order)
        try:
            return next[0]
        except IndexError:
            return False

    # Get prev NOT in_prog
    def notprog_prev(self):
        prev = self.__class__.objects.filter(in_prog=False).filter(order__lt=self.order).order_by('-order')
        try:
            return prev[0]
        except IndexError:
            return False

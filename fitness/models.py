from django.db import models

class Exercise(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    speed = models.DecimalField(max_digits=4, decimal_places=2)
    repetitions = models.IntegerField()
    media_file = models.FileField(upload_to='fitness')
    in_prog = models.BooleanField()

    # Show title in admin page
    def __str__(self):
        return self.title

    #Get the next object by primary key order
    def get_next(self):
        next = self.__class__.objects.filter(pk__gt=self.pk)
        try:
            return next[0]
        except IndexError:
            return False

    #Get the previous object by primary key order
    def get_prev(self):
        prev = self.__class__.objects.filter(pk__lt=self.pk).order_by('-pk')
        try:
            return prev[0]
        except IndexError:
            return False

    #Get next programme object
    def prog_next(self):
        next = self.__class__.objects.filter(in_prog=True).filter(pk__gt=self.pk)
        try:
            return next[0]
        except IndexError:
            return False

    #Get prev programme object
    def prog_prev(self):
        prev = self.__class__.objects.filter(in_prog=True).filter(pk__lt=self.pk).order_by('-pk')
        try:
            return prev[0]
        except IndexError:
            return False

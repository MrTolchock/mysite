from django.db import models

class Train(models.Model):

    fahrt_bezeichner = models.CharField(max_length=20)
    bpuic = models.IntegerField()
    haltestellen_name = models.CharField(max_length=50)
    linien_text = models.CharField(max_length=20)
    betriebstag = models.DateTimeField()
    ankunftszeit = models.DateTimeField()
    an_prognose = models.DateTimeField()
    an_prognose_status = models.CharField(max_length=20)
    abfahrtszeit = models.DateTimeField()
    ab_prognose = models.DateTimeField()
    ab_prognose_status = models.CharField(max_length=20)
    faellt_aus_tf = models.CharField(max_length=20)
    ab_delay = models.CharField(max_length=20)

    def __str__(self):
        return self.title

from django.db import models

class Train(models.Model):

    fahrt_bezeichner = models.CharField(max_length=20)
    bpuic = models.IntegerField()
    haltestellen_name = models.CharField(max_length=50)
    linien_text = models.CharField(max_length=20)
    betriebstag = models.DateTimeField()
    ankunftszeit = models.DateTimeField()
    an_prognose = models.DateTimeField(null=True)
    an_prognose_status = models.CharField(max_length=20)
    abfahrtszeit = models.DateTimeField()
    ab_prognose = models.DateTimeField(null=True)
    ab_prognose_status = models.CharField(max_length=20)
    faellt_aus_tf = models.IntegerField()
    ab_delay = models.IntegerField()
    uid = models.IntegerField(primary_key=True)

    # def __str__(self):
    #     return self.fahrt_bezeichner#title

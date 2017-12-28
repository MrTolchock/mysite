from django.db import models

class Train(models.Model):

    fahrt_bezeichner = models.CharField(max_length=20)
    bpuic = models.IntegerField()
    haltestellen_name = models.CharField(max_length=50)
    linien_text = models.CharField(max_length=20)
    betriebstag = models.DateTimeField()
    ankunftszeit = models.DateTimeField(null=True)
    an_prognose = models.DateTimeField(null=True)
    an_prognose_status = models.CharField(max_length=20, null=True)
    abfahrtszeit = models.DateTimeField(null=True)
    ab_prognose = models.DateTimeField(null=True)
    ab_prognose_status = models.CharField(max_length=20, null=True)
    faellt_aus_tf = models.IntegerField()
    ab_delay = models.IntegerField(null=True)
    uid = models.IntegerField(primary_key=True)

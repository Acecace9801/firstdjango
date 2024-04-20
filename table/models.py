from django.db import models

# Create your models here.
class BettingOdds(models.Model):
    leagueid = models.AutoField(primary_key=True)
    leaguename = models.CharField(max_length=50)

    class Meta:
        db_table = 'leaguetest'
        app_label = ''

    def __str__(self):
        return self

class PinnacleHighlight(models.Model):
    id = models.AutoField(primary_key=True)
    playerone = models.CharField(max_length=50)
    playertwo = models.CharField(max_length=50)
    firstwin = models.FloatField()
    draw = models.FloatField()
    secondwin = models.FloatField()

    class Meta:
        db_table = 'pinnacle_highlight'
        app_label = ''

    def __str__(self):
        return self
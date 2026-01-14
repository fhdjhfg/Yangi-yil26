from django.db import models

# Create your models here.
class Hayvon(models.Model):
    ismi=models.CharField(max_length=255)
    yosh=models.IntegerField()
    yesa_boladi=models.BooleanField(default=True)

    def __str__(self):
        return self.ismi

class UyHayvon(models.Model):
    hayvon=models.ForeignKey(Hayvon,on_delete=models.CASCADE)
    parrandami=models.BooleanField(default=True)
    yaratilgan_vaqt=models.DateTimeField()

    def __str__(self):
        return self.parrandami



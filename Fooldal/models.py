from django.db import models


class Szemely(models.Model):
        vezeteknev = models.CharField(max_length=100)
        keresztnev = models.CharField(max_length=100)
        eletkor = models.IntegerField()
        hazas = models.BooleanField(default=False)
        elettortenet = models.TextField()
        letrehozva = models.DateField(auto_now_add=True)

        class Meta:
                verbose_name_plural = "Személyek"

        def __str__(self):
            return f"{self.vezeteknev} {self.keresztnev}"
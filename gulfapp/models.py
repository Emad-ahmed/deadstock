from django.db import models



class ExcelData(models.Model):
    product = models.CharField(max_length=500)

    def __str__(self):
        return self.product
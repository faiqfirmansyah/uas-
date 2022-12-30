from django.db import models

class servis(models.Model):
    N_register = models.CharField(max_length=10)
    Nama = models.CharField(max_length=30)
    Alamat = models.TextField()
    Keterangan = models.TextField()

    def __str__(self):
        return"{}".format(self.Nama)
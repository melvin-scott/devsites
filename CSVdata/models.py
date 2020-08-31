from django.db import models

class CSVFile(models.Model):
    file_name = models.CharField(max_length=500)
    file_path = models.FileField(upload_to='%Y/%m/%d', null=True, verbose_name='')
    file_dateadded = models.DateField('Date Added', 'Date Added', True)

    def __str__(self):
        return self.file_name + ": " + str(self.file_path)
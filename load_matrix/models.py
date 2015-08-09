from django.db import models


class FileManager(models.Manager):
    def get_last_file(self, user):
        return self.filter(user_name=user)[0]


class File(models.Model):
    class Meta:
        db_table = 'file'

    class Meta:
        ordering = ['-load_date']

    user_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    load_date = models.DateTimeField()
    objects = FileManager()

    def __str__(self):
        return self.user_name + "_" + self.title + '_'+self.load_date.__str__() + '.xls'

    def get_name_PCA_file_T(self):
        return self.user_name + "_" + self.title + '_'+self.load_date.__str__() + 'T.csv'

    def get_name_PCA_file_P(self):
        return self.user_name + "_" + self.title + '_'+self.load_date.__str__() + 'P.csv'


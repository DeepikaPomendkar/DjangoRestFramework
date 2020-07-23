from djongo import models

# Create your models here.


class employees (models.Model):
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    emp_id = models.ObjectIdField()


    def __str__(self):
        return self.emp_id
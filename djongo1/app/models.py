from djongo import models

# Create your models here.


class employees (models.Model):
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    emp_id = models.ObjectIdField()


    def __str__(self):
        return self.emp_id


# class User (models.Model):
#     user_id = models.ObjectIdField()
#     username = models.CharField(max_length=15)
#     password = models.CharField(max_length=50)
#     token = models.CharField(max_length=15)



#     def __str__(self):
#         return self.user_id



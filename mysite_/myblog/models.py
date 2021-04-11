from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=191, primary_key=True)  #
    email = models.EmailField()
    update_time = models.DateTimeField(auto_now=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    null_test = models.CharField(max_length=200, null=True)
    blank_test = models.CharField(max_length=200, null=True)

    class Meta:
        abstract = True


class Reader(Person):
    whether_vip = models.BooleanField(default=False)

    class Meta:
        db_table = "reader"
        managed = True

    def __str__(self):
        return f"id:{self.id}, {self.name}"

    # 实例
    # def lastest(self):
    #     self.__class__.object.get(pk=)


class Writer(Person):
    pass


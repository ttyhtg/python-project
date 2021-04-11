from django.db import models

# Create your models here.
class Student(models.Model):
    # db_column指定当前在数据库中的字段
    student_id = models.AutoField(primary_key=True, db_column="id")
    name = models.CharField(max_length=200)


class Book(models.Model):
    book_id = models.AutoField(primary_key=True, db_column="id")
    book_name = models.CharField(max_length=200)


class BorrowRecord(Student, Book):
    _id = models.AutoField(primary_key=True, db_column="id")
    borrow_time = models.DateTimeField(auto_now_add=True)
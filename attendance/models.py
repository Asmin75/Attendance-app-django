from django.db import models
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
# Create your models here.

class_choices = (
    ('Pre-Nursery','Pre-Nursery'),
    ('Nursery', 'Nursery'),
    ('Kindergarten', 'Kindergarten'),
    ('I','I'),
    ('II','II'),
    ('III','III'),
    ('IV','IV'),
    ('V','V'),
    ('VI','VI'),
    ('VII','VII'),
    ('VIII','VIII'),
    ('IX','IX'),
    ('X','X'),
    ('XI','XI'),
    ('XII','XII'),
)

class_attendance = (
    ('Present','Present'),
    ('Absent','Absent'),
)

class School(models.Model):
    id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    principal = models.CharField(max_length=500)

    def __str__(self):
        return self.school_name


class Teacher(models.Model):
    user = models.OneToOneField(User)
    teacher_name = models.CharField(max_length=500,null=True)
    teacher_class = models.CharField(max_length=100, choices=class_choices, default=1)
    teacher_section = models.CharField(max_length=50,null=True)
    teacher_school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def get_absolute_url(self):
        return reverse("attendance:profile", kwargs={'pk':self.pk})

    #def __str__(self):
     #   return self.teacher_name

class Student(models.Model):
    student_name = models.CharField(max_length=200)
    roll_no = models.CharField(max_length=100)
    student_teacher = models.ForeignKey(Teacher)
    present = models.IntegerField(default=0)
    absent = models.IntegerField(default=0)

    def __str__(self):
        return self.student_name + '-'  + self.student_teacher.teacher_name


    def get_absolute_url(self):
        return reverse("attendance:profile", kwargs={'pk':self.student_teacher.id})

# class Principal(models.Model):
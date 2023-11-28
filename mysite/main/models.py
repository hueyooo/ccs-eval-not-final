from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  image = models.ImageField(
    default='default.jpg', 
    upload_to='profile_pics'
  )
  role = models.CharField(max_length=10)

  def __str__(self):
    return self.first_name + " " + self.last_name

class Student(models.Model):
  user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    primary_key=True,
  )
  section = models.CharField(max_length=1000)

  def __str__(self):
    return self.user.first_name + " " + self.user.last_name

class Instructor(models.Model):
  user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    primary_key=True,
  )
  department = models.CharField(max_length=50)
  access_lvl = models.IntegerField()

  def __str__(self):
    return self.user.first_name + " " + self.user.last_name

class Subject(models.Model):
  code = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  year = models.CharField(max_length=10)
  semester = models.CharField(max_length=10)
  course = models.CharField(max_length=3)

  def __str__(self):
    return self.code + "/" + self.description + "/" + self.course
  
class EvaluatedDetail(models.Model):
  section = models.CharField(
    max_length=10
  )
  inst = models.ForeignKey(
    Instructor, 
    on_delete=models.CASCADE
  )
  subj = models.ForeignKey(
    Subject, 
    on_delete=models.CASCADE
  )

  def __str__(self):
    return self.subj.code + "/" + self.section

class Questionnaire(models.Model):
  category = models.CharField(max_length=50)
  question = models.CharField(max_length=500)

  def __str__(self):
    return self.question

class InstructorQuestionnaire(models.Model):
  category = models.CharField(max_length=50)
  question = models.CharField(max_length=500)

  def __str__(self):
    return self.question

class QuestionnaireScore(models.Model):
  question = models.ForeignKey(
    Questionnaire, 
    on_delete=models.CASCADE
  )
  score = models.IntegerField()
  author = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
  )
  evaluated = models.ForeignKey(
    Instructor,
    on_delete=models.CASCADE,
  )

class InstructorQuestionnaireScore(models.Model):
  question = models.ForeignKey(
    InstructorQuestionnaire, 
    on_delete=models.CASCADE
  )
  score = models.IntegerField()
  author = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
  )
  evaluated = models.ForeignKey(
    Instructor,
    on_delete=models.CASCADE,
  )

class Comment(models.Model):
  comment = models.TextField()
  sentiment = models.CharField(max_length=10)
  score = models.CharField(max_length=50)
  is_connected = models.BooleanField(default=True)
  author = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
  )
  evaluated = models.ForeignKey(
    Instructor,
    on_delete=models.CASCADE,
  )

class EvalSched(models.Model):
  date_from = models.DateField()
  date_to = models.DateField()
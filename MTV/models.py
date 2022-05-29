from django.db import models

# Create your models here.
class Board(models.Model): #models안의 Model을 상속
  title = models.CharField(max_length=30)
  content = models.TextField(max_length=500)
  create_date = models.DateTimeField(auto_now_add=True)
  modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)

  def __str__(self): 
    return self.title
  #원래는 반환값이 primary key인 아이디를 반환하는데 타이틀을 반환하게 오버라이딩함
  #함수구성 추가는 마이그래이션 안해도 된다.

class Question(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  create_date = models.DateTimeField(auto_now_add=True)
  modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)

  def __str__(self):
    return self.title

class Answer(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  content = models.TextField()
  create_date = models.DateTimeField(auto_now_add=True)
  modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)

  def __str__(self):
    return self.content

from secrets import choice
from tkinter import CASCADE
from django.db import models

# Create your models here.
# NotNull은 기본값으로 설정되어 있어서 명시하지 않아도 된다.
class Question(models.Model):
  question_text = models.CharField(max_length=200)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.question_text

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text
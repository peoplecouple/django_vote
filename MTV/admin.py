from django.contrib import admin
from .models import Board, Question, Answer

#관리자페이지에 정보 등록할 때 사용함
# Register your models here.
admin.site.register(Board)
admin.site.register(Question)
admin.site.register(Answer)
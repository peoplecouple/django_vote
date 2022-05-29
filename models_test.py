# 실제 외부스크립트를 작업하고 있는 장고프로젝트에 연결하는 코드
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_wsgi_application()


from MTV.models import Board

#데이터 조회
# def data_selete():
  # All Select 전체 데이터 조회
  # print(Board.objects.all())
  # print("Object Count: " + str(Board.objects.count()))

  #Condition Select
  # print(Board.objects.filter(id=1))
  # print(Board.objects.filter(id=2))
  # print(Board.objects.get(id=1))
  # print(Board.objects.get(id=2)) 없기 때문에 에러남

  # filter는 데이터의 존재유무를 확인할 때 
  # get은 내가 정확히 알고 있을 때 데이터 하나 딱 들고올 때 씀

  # print(Board.objects.filter(title__contains="Title"))
  # print(Board.objects.filter(title__contains="lala"))
  # filter만 contains 쓸 수 있다.

#데이터 생성
# def data_create():
#   Board_data = Board(title="Django Project", content="Django Project Mode")
#   Board_data.save()
#   print(Board.objects.all())

#데이터 삭제
# def data_delete():
#   Board_data = Board.objects.get(title="Django Project")
#   Board_data.delete()
#   print(Board.objects.all())

#데이터 수정
# def data_create():
#   Board_data = Board(title='Django Project', content='Django Project Model Data Create TEST')
#   Board_data.save()
#   print(Board.objects.all())

# def data_modify():
#   Board_data = Board.objects.get(title='Django Project')
#   Board_data.title = 'Django Model TEST'
#   Board_data.save()
#   print(Board.objects.all())

# def data_objects():
#   Board_object = Board.objects.get(title='Board Title')
#   print("ID(PK):", Board_object.id)
#   print("Title:", Board_object.title)
#   print("Content:", Board_object.content)
#   print("Create_Date:", Board_object.create_date)
#   print("Modify_Date:", Board_object.modify_date)


from MTV.models import Question, Answer

# 관계설정된 보드들에서 데이터 조회
# def R_selete():
#   Q = Question.objects.get(id=1)
#   print("ID(PK):", Q.id)
#   print("Title:", Q)
#   print("Content:", Q.content)
  
#   print("Answer Count:", Q.answer_set.count())
#   print("Answer List:", Q.answer_set.all())
#   print("Answer Get:", Q.answer_set.get(content__contains='Professor'))
#   print("Answer Filter:", Q.answer_set.filter(content__contains='Soccer'))
  
# 관계설정된 보드들에서 데이터 생성과 삭제 
# def R_create():
#   Q = Question.objects.get(id=1)
#   Q.answer_set.create(content='Office Worker')
#   print("Answer List:", Q.answer_set.all())

# def R_delete():
#   Q = Question.objects.get(id=1)
#   A = Answer.objects.get(content__contains='Office Worker')
#   A.delete()
#   print("Answer List:", Q.answer_set.all())

if __name__ == '__main__':
  # data_selete()
  # data_create()
  # data_delete()
  # data_create()
  # data_modify()
  # data_objects()
  # R_selete()
  # R_create()
  # R_delete()
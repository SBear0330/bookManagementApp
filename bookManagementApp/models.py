from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="도서 카테고리를 입력하세요.")
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목")
    author = models.CharField(max_length=100, verbose_name="저자")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="카테고리")
    
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="대여자")
    due_back = models.DateField(null=True, blank=True, verbose_name="대여만기일")
    # null=True는 db상 값이 비어있어도 된다 / blank=True는 화면(폼 입력 등)에서 값이 비어있어도 된다
    
    
    def __str__(self):
        return self.title # admin에서 book list를 출력할 때 default 객체 번호가 아닌 객체의 title을 출력
    
    @property # 함수를 멤버변수처럼 사용할 수 있게 해 주는 데코레이터. ex) Book.is_overdue()을 Book.is_overdue로
    def is_overdue(self):
        if self.due_back and self.due_back > date.today(): # self.due_back이 NULL이 아니어야(즉 대여자가 있어야)
            return True
    
    # 1. 기본적으로 변수(속성)는 상태 / 함수(메서드)는 동작을 정의함. but "overdue 여부"는 상태에 가깝다.
    # 2. html은 함수 뒤에 괄호 포함할 수 없음. 따라서 "로직의 결과"를 html에 뿌려줄 경우 반드시 필요
    # 3. 유지보수의 유연성 - Integer로 입력받은 price를 일괄 할인해서 보여줘야 한다면?
    #       price 변수가 사용된 다른 파일들 건드릴 필요 없이,
    #       기존 가격 데이터는 유지(_price)하고 price(): _price * (할인율) 함수로 만든 뒤 @property 붙여버리기
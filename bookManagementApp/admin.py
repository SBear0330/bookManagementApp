from django.contrib import admin
from .models import Book, Category

# Register your models here.
admin.site.register(Category) # register란 admin UI(관리 도구)와 DB를 연결. 이걸 하지 않으면 admin page에는 아무것도 뜨지 않고, 정의한 model은 db에 테이블로만 존재.

@admin.register(Book) # == admin.register.(Book, Bookadmin)
class BookAdmin(admin.ModelAdmin):
    
    # 목록에서 보여줄 field 지정
    list_display = ['title', 'author', 'category', 'borrower', 'due_back', 'is_overdue'] # 함수임에도 models.py의 @property로 인해 is_overdue 추가 가능
    
    # 필터 사이드바 추가 / 각 field별 모아보기가 가능해짐
    list_filter = ['due_back', 'category'] # is_overdue 사용 불가: db에 SQL(WHERE) 날려서 필터링하므로 실제 있는 field여야 함
    
    # 검색창 추가 / 검색 기준
    search_fields = ['title', 'author']
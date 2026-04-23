from django.shortcuts import render
from .models import Book
from django.db.models import Q

# Create your views here.
def index(request):
    query = request.GET.get('q')
    
    all_books = Book.objects.all()
    
    if query:
        all_books = all_books.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    count = all_books.count()
    
    context = {
        'library_name': '러버덕의 비밀 서재',
        'book_count': count,
        'books': all_books,
        'query': query
    }
    # 딕셔너리를 render에 'context' argument로 전달하면 loader.render_to_string이 알아서 해석하는듯? 
    # > 딕셔너리의 key와 html의 변수명을 대조하여 value로 대체
    
    # settings.py에서 TEMPLATE_DIR = BASE_DIR / 'bookManagementApp' / 'templates'로 설정해주었으니
    # 굳이 절대경로를 적어줄 필요 없이 index.html만!
    return render(request, 'index.html', context)

def hello(request):
    return render(request, 'hell.html')
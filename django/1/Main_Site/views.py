from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_singers():
    singers = [
        {'id': 1, 'name': "Океан Ельзи", 'genre': "Рок", 'lead_singers': "Святослав Вакарчук", 'slug': 'okean-elzy'},
        {'id': 2, 'name': "Бумбокс", 'genre': "Рок, Хіп-хоп", 'lead_singers': "Андрій Хливнюк", 'slug': 'bumboks'},
        {'id': 3, 'name': "Creedence Clearwater Revival", 'genre': "Рок", 'lead_singers': " Джон Фогерти", 'slug': 'cilver'},
        {'id': 4, 'name': "Cilver", 'genre': "Рок", 'lead_singers': "leon lyazidi", 'slug': 'bumboks'},
        {'id': 5, 'name': "Бумбокс", 'genre': "Рок, Хіп-хоп", 'lead_singers': "Андрій Хливнюк", 'slug': 'bumboks'}
    ]
    
    return singers

def popular_singers(request):
    html_content = """
    <meta charset="utf-8">
    <h1>Популярні співаки України</h1>
    <ul>
    """
    for singer in list_singers():
        singer_url = f"/singer/?id={singer['id']}"
        html_content += f"<li><a href = '{singer_url}'><strong>{singer['name']}</strong> - {singer['genre']} (Вокаліст: {singer['lead_singers']})</li>"
        
    html_content+= """
    
    </ul>
    """
    
    return HttpResponse(html_content, content_type = 'text/html; , charset = utf-8')

def singer_card(request):
    singer_id = request.GET.get('id')
    singer_id = int(singer_id)
    singers = list_singers()
    singer = next((s for s in singers if s['id'] == singer_id), None)
    
    html_content = f"""
    <html>
    <meta charset="utf-8">
        <body>
            <h1>{singer['name']}</h1>
            <p>Жанр: {singer['genre']}</p>
            <p>Вокаліст: {singer['lead_singers']}</p>
        </body>
    </html>
    
    """
    
    return HttpResponse(html_content, content_type = 'text/html; , charset = utf-8')
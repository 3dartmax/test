from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from .models import Notice, Board

def UploadList(request):
    template = Template("""
    <html>
		<head>
			<title>Notices List</title>
		</head>
		<body>
		    <h1>Notice List</h1>
		    <ul>
		    {% for notice in notices %}
		        <li>
		            <a href="{% url 'testupload:view' notice.id %}">
		                {{ notice.author.username }} / {{ notice.title }}
		            </a>
		             /
		            <a href="{{ notice.photo.url }}">
		                {{ notice.photo.url }}
		            <a>
		        </li>
		    {% endfor %}
		    </ul><br>
		    <h1>Board List</h1>
		    <ul>
		    {% for board in boards %}
		        <li>
		            <a href="{% url 'testupload:detail' board.id %}">
		                {{ board.title }}
		            </a>
		             /
		            <a href="{{ board.upload.url }}">
		                {{ board.upload.url }}
		            <a>
		        </li>
		    {% endfor %}
		    </ul>
		</body>
	</html>
    """)
    context = Context({'notices': Notice.objects.order_by('created_date'), 'boards': Board.objects.order_by('created_date')})
    return HttpResponse(template.render(context))


def UploadView(request, pk):
    notice = Notice.objects.get(pk=pk)
    html = '''
    <html>
		<head>
			<title>Notices View</title>
		</head>
		<body>
		    id({0}) / title({1}) / user({2}) / image({3})<br>
		     <img src="{4}" width="{5}" height="{6}">
		</body>
	</html>
    '''.format(notice.id,
                notice.title,
                notice.username(),
                notice.imagename(),
                notice.imageurl(),
                notice.imagewidth() / 5,
                notice.imageheight() / 5)
    return HttpResponse(html)


def UploadDetail(request, pk):
    board = Board.objects.get(pk=pk)
    html = '''
    <html>
		<head>
			<title>Board Detail</title>
		</head>
		<body>
		    id({0}) / title({1}) /
		    <a href="{2}">{3}</a>
		</body>
	</html>
    '''.format(board.id,
                board.title,
                board.fileurl(),
                board.filename())
    return HttpResponse(html)

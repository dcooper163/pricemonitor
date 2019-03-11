from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    person= {'firstname': 'Craig', 'lastname': 'Daniels'}
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('price/index.html')
    output = ', '.join([q.question_text for q in latest_question_list])
    
    #return HttpResponse(template.render(person, request))
    
    #return HttpResponse("Hello, world. You're at the polls index." + output)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)
    
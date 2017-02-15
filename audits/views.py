from django.shortcuts import render
from django.utils import timezone
from .models import AuditQuestions

def question_list(request):
    questions = AuditQuestions.objects.order_by('subsection_num')
    return render(request, 'audits/question_list.html', {'questions': questions})

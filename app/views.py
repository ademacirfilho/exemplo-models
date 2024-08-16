from django.shortcuts import render

from .models import Tarefa, Aluno

# Create your views here.
def index(request):
    context = {
        "tarefas": Tarefa.objects.all(),
    }

    return render(request, "index.html", context)

def alunos(request):
    context = {
        "alunos": Aluno.objects.all()
    }
    return render (request, "alunos.html", context)
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Question
from .models import Dataset, Post1
from .forms import DatasetForm, QuestionForm, Post1Form
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404



def index(request):
    latest_question_list = Post1.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('taswira/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'taswira/WebPage1.html', context)
    #return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'taswira/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

#uploading file request is handled here
def simple_upload(request):
    if request.method =="POST":
        form=QuestionForm(request.POST)
        if form.is_valid():
            dataset=form.save(commit=False)
            #do other tasks
            dataset.save()
            return HttpResponse("You have saved a dataset %s." % dataset.question_text)
            #return render(request, 'taswira/upload.html',{'form':dataset})
        else:
            return HttpResponse("You have error in the form fields.")
    else:
        form = QuestionForm()
        return render(request, 'taswira/upload.html',{'form':form})

def question_edit(request,pk):
    question= get_object_or_404(Question, pk=pk)
    if request.method =="POST":
        form=QuestionForm(request.POST,instance=question)
        if form.is_valid():
            dataset=form.save(commit=False)
            #do other tasks
            dataset.save()
            return HttpResponse("You have saved a dataset %s." % dataset.question_text)
            #return render(request, 'taswira/upload.html',{'form':dataset})
        else:
            return HttpResponse("You have error in the form fields.")
    else:
        form = QuestionForm(instance=question)
        return render(request, 'taswira/upload.html',{'form':form})

def graph(request):
    return render(request,'taswira/kumalija.html')


def post_view(request,pk):
    post= get_object_or_404(Post1, pk=pk)
    if request.method =="POST":
        post.cvs_path.delete(save=False)
        form=Post1Form(request.POST, request.FILES, instance=post)
        if form.is_valid():
                form.save()
                return HttpResponse(" The post has been edited ")
    else:
        form = Post1Form(instance=post)
        return render(request, 'taswira/upload.html',{'form':form})

def post_add(request):
    if request.method == "POST":
            form = Post1Form(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse(" new post ")
            #return render(request, 'taswira/upload.html',{'form':dataset})
            #else:
            #   return HttpResponse("You have error in the form fields.************")
    else:
        form = Post1Form()
        return render(request, 'taswira/question_view.html',{'form':form})
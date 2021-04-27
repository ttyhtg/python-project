from django.shortcuts import render, get_object_or_404
from django.db import transaction
# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse, FileResponse
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

# 用类实现restfulapi
# 只需要绑定一次path, 会根据HttpRequest.method自动选择相应的处理方法.
# class IndexView(generic.View):
#     def get(self, *args, **kwargs):
#         pass
#
#     def post(self, *args, **kwargs):
#         pass
#
#     def put(self, *args, **kwargs):
#         pass
#
#     def delete(self, *args, **kwargs):
#         pass


class IndexView(generic.TemplateView):
    template_name = "polls/index.html"

    def get_context_data(self, **kwargs):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {
            'latest_question_list': latest_question_list,
        }
        return context


def index(request):
    """
    request 就是作为参数传递进来的请求对象
    :param request:
    :return:HttpResponse 处理完请求的返回对象
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        context = {
            "question": question
        }
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


@transaction.atomic()
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def file_test(request):
    filename = "views.py"
    with open('polls/views.py', "r", encoding="utf-8") as f:
        response = FileResponse(f.read())
        response['content-type'] = "application/octet-stream"
        response['content-disposition'] = f"attachment; filename={filename}"
        return response
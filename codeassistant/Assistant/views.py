from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .langchain import askProblem
from .forms import ProblemForm
import markdown


class Home(View):
    def get(self, request):
        ai_content = request.session.get('ai_content', '')
        return render(request, 'Assistant/home.html', {'ai_content': ai_content})

    def post(self, request):
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.cleaned_data['problem']
            response = askProblem(problem)
            markdown_response = markdown.markdown(
                response, extensions=['fenced_code', 'codehilite'])
            request.session['ai_content'] = markdown_response
        ai_content = request.session.get('ai_content', '')
        return JsonResponse({'ai_content': ai_content})
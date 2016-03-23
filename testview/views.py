from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from .forms import MyForm

# 방법1-1.
# http://localhost:8000/testview/about/?id=1974&name=3dartmax
def my_view(request):
    if request.method == 'GET':
        id   = request.GET.get('id', None)
        name = request.GET.get('name', '')
        return HttpResponse('result - my_view(id({0}) / name({1})'.format(id, name))

# 방법1-2.
# http://localhost:8000/testview/about/?id=1974&name=3dartmax
class MyView(View):
    greeting = "Welcome To 3dartmax~~~!"
    def get(self, request):
        id   = request.GET.get('id', None)
        name = request.GET.get('name', '')
        return HttpResponse('{0}<br>result - MyView(id({1}) / name({2})'.format(self.greeting, id, name))

# 방법2. - Form
# http://localhost:8000/testview/vote/
class MyFormView(View):
    form_class    = MyForm
    template_name = 'testview/form_write.html'
    initial       = { 'key':'value' }
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            #print('name', form['name'].value())
            #print('title', form['title'].value())
            #print('content', form['content'].value())
            #return HttpResponseRedirect('/testview/success')
            datas = {}
            for data in form:
                datas[data.name] = data.value()
            return render(request, 'testview/form_write_ok.html', datas)
        return render(request, self.template_name, { 'form': form })

class MySuccessView(View):
    def get(self, request):
        return HttpResponse('Success - get()')
    def post(self, request):
        return HttpResponse('Success - post()')

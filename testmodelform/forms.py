from django import forms
from .views import Author, Book

# python manage.py shell에서 테스트법.
# >>> from django import forms
# >>> from testmodelform.views import Author, Book
# >>> from testmodelform.forms import DefaultTextInput
# >>> w = DefaultTextInput()
# >>> print(w)
# >>> print(w.media)
# >>> print(w.media['css'])
class DefaultTextInput(forms.TextInput):
    class Media:
        css = {
            'all': ('css/default.css')
        }

# 방법1.
class AuthorForm(forms.ModelForm):
    class Meta:
        model            = Author
        fields           = ['name', 'title', 'birth_date']  # 보여줄폼.
        localized_fields = ('name', 'birth_date',)           # 보여줄폼에 히스토리 리스트.
        #exclude         = ['title']                            # fields에서 제외시킴.
        widgets = {
            #'name': DefaultTextInput(),
            #'name': forms.Textarea(attrs={'rows': 10, 'cols': 80 }),
            #'name': forms.TextInput(attrs={'style': 'border: 1px solid #ff0000;'}),
            #'name': forms.TextInput(attrs={'style': 'background-color: #e2e2e2;'}),
            #'birth_date': forms.TextInput(attrs={'readonly': 'readonly'}),      # 읽기전용 처리.
            #'birth_date': forms.TextInput(attrs={'disabled': 'disabled'}),      # 비활성화 처리.

            # 'css/default.css'정의한 사용자 class="default"적용.
            'name': forms.TextInput(attrs={'class': 'default'}),
        }
        labels = {
            'name': '이름',
            'title': '호칭(결혼여부)',
            'birth_date': '생일'
        }
        help_texts = {
            'name': 'Some useful help text.',
        }
        error_messages = {
            'name': { 'max_length': "This writer's name is too long.", },
        }

class BookForm(forms.ModelForm):
    class Meta:
        model            = Book
        fields           = ['name', 'authors']              # 보여줄폼.
        localized_fields = ('name',)                         # 보여줄폼에 히스토리 리스트.
        widgets = {
            #'name': forms.NumberInput(attrs={'class': 'input-mini'}),
            #'name': forms.TextInput(attrs={'class': 'input-mini'}),
            'name': forms.TextInput(attrs={'style': 'background-color: #e2e2e2;'}),
        }
        labels = {
            'name': '책이름',
            'authors': '작가들',
        }
        help_texts = {
            'name': '100자 이내로 적어 주세요.',
            'authors': '최소 1명이상은 선택해 주세요.',
        }
        error_messages = {
            'name': { 'max_length': "This writer's name is too long. [ %(model_name)s / %(field_labels)s ]", },
        }

"""
from .models import TITLE_CHOICES

# 방법2.
class AuthorForm(forms.Form):
    name       = forms.CharField(max_length=100)
    title      = forms.CharField(max_length=3, widget=forms.Select(choices=TITLE_CHOICES))
    birth_date = forms.DateField(required=False)

class BookForm(forms.Form):
    name    = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
"""
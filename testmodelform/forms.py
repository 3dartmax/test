from django import forms
from .views import Author, Book
from .models import TITLE_CHOICES

# 방법1.
class AuthorForm(forms.ModelForm):
    class Meta:
        model            = Author
        fields           = ['name', 'title', 'birth_date']  # 보여줄폼.
        localized_fields = ('name', 'birth_date',)           # 보여줄폼에 히스토리 리스트.
        #exclude         = ['title']                            # fields에서 제외시킴.
        widgets = {
           'name': forms.Textarea(attrs={'rows': 10, 'cols': 80 }),
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
            'name': forms.TextInput(attrs={'class': 'input-mini'}),
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
# 방법2.
class AuthorForm(forms.Form):
    name       = forms.CharField(max_length=100)
    title      = forms.CharField(max_length=3, widget=forms.Select(choices=TITLE_CHOICES))
    birth_date = forms.DateField(required=False)

class BookForm(forms.Form):
    name    = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
"""
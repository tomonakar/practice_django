from django import forms
from .models import Day


# forms.ModelForm は model の内容から自動的にフォームを作成してくれる
# @see https://docs.djangoproject.com/ja/2.2/topics/forms/modelforms/
class DayCreateForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = '__all__'

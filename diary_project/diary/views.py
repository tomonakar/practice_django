from django.shortcuts import render, redirect
from .forms import DayCreateForm


def index(request):
    return render(request, 'diary/day_list.html')


def add(request):
    # 送信内容を基にフォーム作成. POST以外は空のフォームとする.
    form = DayCreateForm(request.POST or None)

    # methodがPOST且つバリデーションが通ればデータを保存
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('diary:index')

    # methodがPOSTではない、またはバリデーションが通らない場合
    context = {
        'form': form
    }
    return render(request, 'diary/day_form.html', context)

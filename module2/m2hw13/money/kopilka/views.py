from .models import Money
from .forms import MyForm, DateForm
from django.shortcuts import render


def index(request):
    return render(request, 'kopilka/index.html')
    
def results(request):
    date_objects = Money.objects.order_by('pub_date')[:10]
    summ = {}
    prev_sum = 0
    for obj in date_objects:
        summ[obj.id] = obj.earnings + prev_sum
        prev_sum = summ[obj.id]
    context = {'date_objects' : date_objects, 'summ' : summ}
    return render(request, 'kopilka/results.html', context)
    
def add_operation(request):

    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MyForm()

    return render(request, 'kopilka/add_operation.html', {'form': form})
    
def calculate(request):

    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            date_from = cd.get('date_from')
            date_for = cd.get('date_for')
        date_objects = Money.objects.filter(pub_date__gte = date_from).exclude(pub_date__gt = date_for).order_by('pub_date')
        
        summ = {}
        prev_sum = 0
        for obj in date_objects:
            summ[obj.id] = obj.earnings + prev_sum
            prev_sum = summ[obj.id]
        context = {'date_objects' : date_objects, 'summ' : summ}
        
        return render(request, 'kopilka/results.html', context)
    else:
        form = DateForm()
        
    return render(request, 'kopilka/calculate.html', {'form' : form})
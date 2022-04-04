from django.shortcuts import render

# Create your views here.
def lotto(request):
    import random
    pick = random.sample(range(1, 46), 7)
    context = {
        'pick':pick
    }
    return render(request, 'demo/lotto.html', context)

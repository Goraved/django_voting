from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from collections import OrderedDict

languages = ['Java', 'Python', 'C#', 'JS', 'C++', 'PHP', 'Kotlin', 'Ruby']
stats = {}


# Create your views here.
def index(request):
    my_dict = {
        'languages': languages
    }
    return render(request, 'index.html', context=my_dict)


def submit_vote(request):
    return render(request, 'index.html')


def get_query(request):
    query = request.GET['languages']
    if query not in stats:
        stats[query] = {'value': 1, 'percent': 0}
    else:
        stats[query]['value'] += 1
    for stat in stats.values():
        stat['percent'] = calculate_percentage(stat['value'])

    my_dict = {
        'languages': languages,
        'stats': OrderedDict(sorted(stats.items(), key=lambda x: x[1]['value'], reverse=True)),
        'max': max([_['value'] for _ in stats.values()]),
        'min': min([_['value'] for _ in stats.values()])
    }
    return render(request, 'index.html', context=my_dict)


def calculate_percentage(value: int) -> float:
    return value / max([_['value'] for _ in stats.values()]) * 100

from django.shortcuts import render

def index(req):
    context = {
        'key': 'value',
        'num_list': [i for i in range(1, 11)]
    }
    return render(req, "board/index.html", context)

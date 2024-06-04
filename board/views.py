from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm

def index(req):
    context = {
        'key': 'value',
        'num_list': [i for i in range(1, 11)]
    }
    return render(req, "board/index.html", context)

def test(req):
    return render(req, "board/test.html")
    

def signup(req):
    if req.method == "POST":
        ...
    else:
        form = UserCreationForm()
    return render(req, 'board/signup.html', {
        'form': form
    })
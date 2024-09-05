from django.shortcuts import render

def show_main(request):
    context = {
        'Name' : 'Daffa Abyaz',
        'Price': '30k Dollars',
        'Description': 'Strong worker, could handle any crop farm.'
    }

    return render(request, "main.html", context)

from django.shortcuts import render

def show_main(request):
    context = {
        'Name' : 'Daffa Abyaz',
        'Price': '30k Dollars',
        'Description': 'Strong worker, could handle any crop farm.',
        'Type': 'Living Tool'
    }

    return render(request, "main.html", context)

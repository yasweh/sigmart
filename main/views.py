from django.shortcuts import render

def show_main(request):
    context = {
        'Name' : '2306123456',
        'Price': 'Pak Bepe',
        'Description': 'PBP E'
    }

    return render(request, "main.html", context)

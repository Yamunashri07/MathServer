from django.shortcuts import render

def power(request):
    context = {'powerlamp': ""}

    if request.method == "POST":
        i = request.POST.get('intensity', '')
        r = request.POST.get('resistance', '')

        if i and r:
            try:
                i = float(i)
                r = float(r)
                p = (i ** 2) * r
                context['powerlamp'] = round(p, 2)  
            except ValueError:
                context['powerlamp'] = "Invalid input"

    return render(request, 'mathserverapp/math.html', context)


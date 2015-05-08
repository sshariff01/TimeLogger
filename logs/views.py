from django.shortcuts import render, redirect
from datetime import datetime
from decimal import Decimal


from forms import LogForm
from models import Tutor, Log


def home(request):
    form = LogForm()

    return render(request, 'home.html', {'form': form})

def record(request):
    if request.POST:
        errors = []
        if 'name' in request.POST:
            tutor = Tutor.objects.filter(name=request.POST['name'])

            if not tutor:
                tutor = Tutor.objects.create(
                    name=request.POST['name']
                )
                tutor.save()
            tutor = Tutor.objects.get(name=request.POST['name'])

            form = LogForm(request.POST)
            if form.is_valid():
                log = Log.objects.create(
                    tutor=tutor,
                    date=datetime.strptime(
                        request.POST['date'].encode('utf-8'),
                        "%m/%d/%Y"
                    ),
                    hours_worked=request.POST['hours_worked']
                )
                log.save()
                success = True
                form = LogForm()
                return render(request, 'home.html', {'form': form, 'errors': errors, 'success': success})
            else:
                return render(request, 'home.html', {'form': form, 'errors': errors})

        else:
            errors.append({"Please provide your name"})

    return redirect(home)

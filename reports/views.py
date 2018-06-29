from django.shortcuts import render, get_object_or_404
from reports.models import Category, Report, Answer, Label
from users.models import User
from reports.forms import CreateReport, CreateAnswer, ChangeStatus
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def all_categories(request):
    category = Category.objects.all()
    return render(request, 'categories.html', {
        'category': category
    })


@login_required
def category (request, id):
   category = get_object_or_404(Category, id=id)
   form = CreateReport
   reports = Report.objects.filter(category=category)
   if request.method == 'POST':
       form = CreateReport(request.POST)
       created_by = User.objects.get(id=request.user.id)
       if form.is_valid():
           form.instance.category = category
           form.instance.created_by = created_by
           form.save()
   return render(request, 'category.html', {
       'category': category,
       'reports': reports,
       'form': form
    })


@login_required
def report(request, id):
    thisreport = get_object_or_404(Report, id=id)
    form = CreateAnswer
    answers = Answer.objects.filter(report=thisreport)
    labels = Label.objects.filter(report=thisreport)
    assigned_for = thisreport.assigned_to.all()
    if request.method == 'POST':
        form = CreateAnswer(request.POST)
        created_by = User.objects.get(id=request.user.id)
        # form.fields['creator'] = user
        # form.fields['report'] = report
        if form.is_valid():
            form.instance.report = thisreport
            form.instance.created_by = created_by
            form.save()

    return render(request, 'report.html', {
        'user_to': assigned_for,
        'report': thisreport,
        'labels': labels,
        'answers': answers,
        'form': form
    })

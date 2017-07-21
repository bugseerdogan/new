from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .models import Planning
from .forms import UserForm,PlanForm

#def index(request):
#    all_planning=Planning.objects.all()
#    return render(request,'project/index.html',{'all_planning':all_planning})
#def detail(request,planning_id):
#    plan=get_object_or_404(Planning, pk=planning_id)
#    return render(request,'project/detail.html', {'plan':plan})
class IndexView(generic.ListView):
    template_name = 'project/index.html'

    def get_queryset(self):
        return Planning.objects.all()

class DetailView(generic.DetailView):
    model = Planning
    template_name = 'project/detail.html'
#def detail(request,planning_id):
#    user=request.user
#    plan=get_object_or_404(Planning,pk=planning_id)
#    return render(request,'project/detail.html', {'plan': plan, 'user': user})
class PlanCreate(CreateView):
      model=Planning
      fields=['title','author','publication','quality','medium','planned_date','bl','applied_date','status','notes','is_AL','is_BL']
#def PlanCreate(request):
#    if not request.user.is_authenticated():
#        return render(request, 'music/login.html')
#    else:
#        form = PlanForm(request.POST or None, request.FILES or None)
#        if form.is_valid():
#            plan = form.save(commit=False)
#            plan.user = request.user
#            return render(request, 'project/detail.html', {'plan': plan})
#        context = {
#            "form": form,
#        }
#        return render(request, 'project/planning_form.html', context)

class UserFormView(View):
    form_class = UserForm
    template_name='project/registration_from.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form': form})
    def post(self,request):
        form= self.form_class(request.POST)

        if form.is_valid():

            user=form.save(commit=False)
            username= form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user=authenticate(username=username,password=password)

            if user is not None:
                 if user.is_active:
                     login(request,user)
                     return redirect('project:index')

        return render(request, self.template_name,{'form': form})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'project/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                plans = Planning.objects.filter(user=request.user)

                return render(request, 'project/index.html', {'plans': plans})
            else:
                return render(request, 'project/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'project/login.html', {'error_message': 'Invalid login'})
    return render(request, 'project/login.html')
##############
def plans(request):
    if not request.user.is_authenticated():
        return render(request, 'project/login.html')
    else:
        try:
            plan_ids = []
            for plan in Planning.objects.filter(user=request.user):
                for plan in plan.all():
                    plan_ids.append(plan.pk)
            users_songs = Planning.objects.filter(pk__in=plan_ids)

        except Planning.DoesNotExist:
            users_plans = []
        return render(request, 'project/plans.html', {
            'plan_list': users_plans,

        })
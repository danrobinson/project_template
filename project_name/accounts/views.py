# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from emailusernames.forms import EmailUserCreationForm

class RegisterView(FormView):

    template_name = "registration/register.html"
    form_class = EmailUserCreationForm
    success_url = '/dashboard'

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)

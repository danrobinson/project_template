from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class DashboardView(TemplateView):

    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DashboardView, self).dispatch(*args, **kwargs)
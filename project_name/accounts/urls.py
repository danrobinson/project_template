from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from emailusernames.forms import EmailAuthenticationForm
from django.contrib.auth.views import login

from views import RegisterView
from decorators import not_logged_in_required

urlpatterns = patterns('',
    url(r'^/login/$', not_logged_in_required(login),
        {'authentication_form': EmailAuthenticationForm}, name='login'),
    url(r'^/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^/password/reset/$', 'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/user/password/reset/done/', 'template_name': 'registration/password_reset_form.html', 'email_template_name': 'registration/password_reset_email.html'}, name='password_reset'),
    url(r'^/password/reset/done/$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'registration/password_reset_done.html'}),
    url(r'^/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : '/user/password/done/'}),
    url(r'^/password/done/$', 'django.contrib.auth.views.password_reset_complete', {'template_name': 'registration/password_reset_complete.html'}),
    url(r'^/register/$', not_logged_in_required(RegisterView.as_view()),
        name='register'),
)
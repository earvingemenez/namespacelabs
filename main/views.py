import json

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View


class IndexView(TemplateView):

    template_name = 'main/index.html'
    context = {}

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.context)
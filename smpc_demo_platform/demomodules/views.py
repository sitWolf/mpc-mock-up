
from django.views.generic.base import TemplateView

#from .models import DemoVideos

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# decorators = [login_required, ]


# @method_decorator(decorators, name='dispatch')
class ModuleOneView(TemplateView):
    template_name = "demomodules/module-1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

# @method_decorator(decorators, name='dispatch')
class ModuleTwoView(TemplateView):
    template_name = "demomodules/module-2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


# @method_decorator(decorators, name='dispatch')
class ModuleThreeView(TemplateView):
    template_name = "demomodules/module-3.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


# @method_decorator(decorators, name='dispatch')
class ModuleFourView(TemplateView):
    template_name = "demomodules/module-4.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

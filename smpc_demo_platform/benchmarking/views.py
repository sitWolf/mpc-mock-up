from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# decorators = [login_required, ]


# @method_decorator(decorators, name='dispatch')
class BenchmarkViewAppCGOne(TemplateView):
    template_name = "benchmarking/app-x3-Z63/benchmarking-home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# @method_decorator(decorators, name='dispatch')
class BenchmarkEndView(TemplateView):
    template_name = "benchmarking/end-of-demo.html"

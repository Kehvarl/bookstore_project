from django.views.generic.base import TemplateView


# Create your views here.
class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

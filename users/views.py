from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from .forms import RegisteredUserForm
from django.views.generic.edit import CreateView
from .models import User
from orders.models import History, OrderItem


@login_required()
def profile(request):
    order_items = []
    for item in History.objects.filter(user=request.user).order_by('-date'):
        order_items.append(
            (item, OrderItem.objects.filter(order=item.order))
        )

    return render(request, 'registration/profile.html', context={
        'orders': order_items,
    })


class RegisterUserView(CreateView):
    model = User
    template_name = 'registration/register_user.html'
    form_class = RegisteredUserForm
    success_url = reverse_lazy('users:register_done')

    def form_valid(self, form):
        form.save()
        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect
        return HttpResponseRedirect(self.success_url)


class RegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'




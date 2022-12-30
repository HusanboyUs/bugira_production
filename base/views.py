from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView
from .models import Tickets
from .forms import TicketCreateForm

class home_view_template(TemplateView):
    template_name='base/index.html'

home_view=home_view_template.as_view()    

class tickets_list_view(ListView):
    model=Tickets
    template_name='base/list.html'
    context_object_name='tickets'
    paginate_by=2

    def get_queryset(self):
        title = self.request.GET.get('search-title')
        ticket_list=self.model.objects.all()
        if title:
            ticket_list=ticket_list.filter(title__icontains=title)
        return ticket_list 

ticket_list_view = tickets_list_view.as_view()

class tickets_delete_view(DeleteView):
    model=Tickets
    template_name='base/delete.html'
    context_object_name='ticketdel'
    success_url='/list'

ticket_delete=tickets_delete_view.as_view()


class ticket_detail_view(DetailView):
    model=Tickets
    template_name='base/detailCard.html'
    context_object_name='ticketdetail'

ticket_detail=ticket_detail_view.as_view()


class ticket_edit_view(UpdateView):
    pass


def createTicket(request):
    form=TicketCreateForm()
    ticket=Tickets.objects.all()
    if request.method == 'POST':
        form=TicketCreateForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            print('came here')
            instance.save()
            return redirect('tickets_list_view')
    context={'form':form}
    return render(request, 'base/create.html',context)

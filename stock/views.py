from django.shortcuts import render
from rest_framework import generics
from .models import Kospi, Kosdak, KospiInstance, KosdakInstance

# Create your views here.

def index(request):
    """ View function for home page of site """
    # Generate counts of some of the main objects
    num_kospis = Kospi.objects.all().count()
    num_kospi_instances = KospiInstance.objects.all().count()
    num_kosdaks = Kosdak.objects.all().count()
    num_kosdak_instances = KosdakInstance.objects.all().count()
    # Available copies of stocks
    num_kospi_instance_available = KospiInstance.objects.filter(status__exact='d').count()
    num_kosdak_instance_available = KosdakInstance.objects.filter(status__exact='d').count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(
        request,
        'index.html',
        context={
            'num_kospis': num_kospis, 'num_kospi_instances': num_kospi_instances,
            'num_kospi_instance_available': num_kospi_instance_available,
            'num_kosdaks': num_kosdaks, 'num_kosdak_instances': num_kosdak_instances,
            'num_kosdak_instances_available': num_kosdak_instance_available,
        }
    )
from django.views import generic

class KospiListView(generic.ListView):
    """ Generic class-based view for a list of kospis. """
    model = Kospi
    paginate_by = 10

class KospiDetailView(generic.DetailView):
    """ Generic class-based detail view for a kospis """
    model = Kospi

class KosdakListView(generic.ListView):
    """ Generic class-based view for a list of kospis. """
    model = Kosdak
    paginate_by = 10

class KosdakDetailView(generic.DetailView):
    """ Generic class-based detail view for a kospis """
    model = Kosdak

from django.contrib.auth.mixins import LoginRequiredMixin

class OwnerKospisByUserListView(LoginRequiredMixin, generic.ListView):
    """ Generic class-based view listing kospis on name to current user. """
    model = KospiInstance
    template_name = 'stock/kospiinstance_list_owned_user.html'
    paginate_by = 10

    def get_queryset(self):
        return KospiInstance.objects.filter(owner=self.request.user).filter(status__exact='h').order_by('due_back')

class OwnerKosdaksByUserListView(LoginRequiredMixin, generic.ListView):
    """ Generic class-based view listing kospis on name to current user. """
    model = KosdakInstance
    template_name = 'stock/kosdakinstance_list_owned_user.html'
    paginate_by = 10

    def get_queryset(self):
        return KosdakInstance.objects.filter(owner=self.request.user).filter(status__exact='h').order_by('due_back')

# Added as part of challenge!
from django.contrib.auth.mixins import PermissionRequiredMixin


class OwnerKospisAllListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission."""
    model = KospiInstance
    permission_required = 'stock.can_mark_returned'
    template_name = 'stock/kospiinstance_list_owned_all.html'
    paginate_by = 10

    def get_queryset(self):
        return KospiInstance.objects.filter(status__exact='o').order_by('due_back')



class OwnerKosdaksAllListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission."""
    model = KosdakInstance
    permission_required = 'stock.can_mark_returned'
    template_name = 'stock/kosdakinstance_list_owned_all.html'
    paginate_by = 10

    def get_queryset(self):
        return KosdakInstance.objects.filter(status__exact='o').order_by('due_back')


from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

# from  .form import SearchForm
from .forms import KospiSearchForm, KosdakSearchForm

# Create your views here.
@permission_required('stock.can_mark_returned')
def search_kospi_name(request, pk):
    kospi_instance = get_object_or_404(Kospi, pk=pk)

    #if post, processing data
    if request.method == 'POST':

        #Create a form_instance & binding requsted data
        kospi_company_name_form = KospiSearchForm(request.POST)

        # Chect form validate
        if kospi_company_name_form.is_valid():
            # Process data as requsted
            stock_company_name_data = kospi_instance.code.filter\
                (name=kospi_company_name_form.cleaned_company_name['company_name'])
            q_set = Kospi.objects.get(name=stock_company_name_data)
            return HttpResponseRedirect(reverse('all-kospi'))
    else:
        proposed_search_name = KospiSearchForm.company_name
        kospi_company_name_form = KospiSearchForm(initial={'company_name': proposed_search_name})

    context = {
        'form' : kospi_company_name_form,
        'stock_instance' : kospi_instance,
    }

    return render(request, 'stock/search_kospi_name.html', context)

@permission_required('stock.can_mark_returned')
def search_kosdak_name(request, pk):
    kosdak_instance = get_object_or_404(Kosdak, pk=pk)

    #if post, processing data
    if request.method == 'POST':

        #Create a form_instance & binding requsted data
        kosdak_company_name_form = KosdakSearchForm(request.POST)

        # Chect form validate
        if kosdak_company_name_form.is_valid():
            # Process data as requsted
            kosdak_company_name_data = kosdak_instance.code.filter\
                (name=kosdak_company_name_form.cleaned_company_name['company_name'])
            q_set = Kosdak.objects.get(name=kosdak_company_name_data)
            return HttpResponseRedirect(reverse('all-kosdak'))
    else:
        proposed_search_name = KosdakSearchForm.company_name
        kosdak_company_name_form = KosdakSearchForm(initial={'company_name': proposed_search_name})

    context = {
        'form' : kosdak_company_name_form,
        'stock_instance' : kosdak_instance,
    }

    return render(request, 'stock/search_kosdak_name.html', context)

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Classes created for the forms challenge
class KospiCreate(PermissionRequiredMixin, CreateView):
    model = Kospi
    fields = '__all__'
    permission_required = 'stock.can_mark_returned'


class KospiUpdate(PermissionRequiredMixin, UpdateView):
    model = Kospi
    fields = '__all__'
    permission_required = 'stock.can_mark_returned'


class KospiDelete(PermissionRequiredMixin, DeleteView):
    model = Kospi
    success_url = reverse_lazy('kospis')
    permission_required = 'stock.can_mark_returned'

class KosdakCreate(PermissionRequiredMixin, CreateView):
    model = Kosdak
    fields = '__all__'
    permission_required = 'stock.can_mark_returned'


class KosdakUpdate(PermissionRequiredMixin, UpdateView):
    model = Kosdak
    fields = '__all__'
    permission_required = 'stock.can_mark_returned'


class KosdakDelete(PermissionRequiredMixin, DeleteView):
    model = Kosdak
    success_url = reverse_lazy('kosdaks')
    permission_required = 'stock.can_mark_returned'

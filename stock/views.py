from django.shortcuts import render
from rest_framework import generics
from .models import Kospi, Kosdak, KospiInstance, KosdakInstance, Owner

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
    """ Generic class-based detail view for a kosdaks """
    model = Kosdak

class OwnerListView(generic.ListView):
    """ Generic class-based view for a list of kospis. """
    model = Owner
    paginate_by = 10

class OwnerDetailView(generic.DetailView):
    """ Generic class-based detail view for a kospis """
    model = Owner

from django.contrib.auth.mixins import LoginRequiredMixin

class OwnedKospisByUserListView(LoginRequiredMixin, generic.ListView):
    """ Generic class-based view listing kospis on name to current user. """
    model = KospiInstance
    template_name = 'stock/kospiinstance_list_owned_user.html'
    paginate_by = 10

    def get_queryset(self):
        return KospiInstance.objects.filter(user=self.request.user).filter(status__exact='h').order_by('due_back')


class OwnedKosdaksByUserListView(LoginRequiredMixin, generic.ListView):
    """ Generic class-based view listing kospis on name to current user. """
    model = KosdakInstance
    template_name = 'stock/kosdakinstance_list_owned_user.html'
    paginate_by = 10

    def get_queryset(self):
        return KosdakInstance.objects.filter(user=self.request.user).filter(status__exact='h').order_by('due_back')


# Added as part of challenge!
from django.contrib.auth.mixins import PermissionRequiredMixin


class OwnedKospisAllListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission."""
    model = KospiInstance
    permission_required = 'stock.can_mark_returned'
    template_name = 'stock/kospiinstance_list_owned_all.html'
    paginate_by = 10

    def get_queryset(self):
        return KospiInstance.objects.filter(status__exact='o').order_by('due_back')



class OwnedKosdaksAllListView(PermissionRequiredMixin, generic.ListView):
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
from stock.forms import KospiSearchForm, KosdakSearchForm

# Create your views here.
@permission_required('stock.can_mark_returned')
def search_kospi_name1(request):

    #if post, processing data
    if request.method == 'POST':

        #Create a form_instance & binding requsted data
        kospi_form = KosdakSearchForm(request.POST)

        # Chect form validate
        if kospi_form.is_valid():
            # Process data as requsted
            c_name = kospi_form.save(commit=False)
            q_data = Kospi.objects.get(name=c_name)
            print(q_data)
            return HttpResponseRedirect(q_data)
    else:
        context = {
            'form' : KospiSearchForm(),
        }
        return render(request, 'stock/search_kospi_name.html', context)

def search_kospi_name(request):
    qs = Kospi.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)
    context = {
        'object_list' : qs,
        'q' : q,
    }
    return render(request, 'stock/search_kospi_name.html', context)


@permission_required('stock.can_mark_returned')
def search_kosdak_name(request):
    qs = Kosdak.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)
    context = {
        'object_list' : qs,
        'q' : q,
    }
    return render(request, 'stock/search_kosdak_name.html', context)





def search_kosdak_name1(request):
    kosdak_instance = get_object_or_404(KosdakInstance)

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
        'kosdak_instance' : kosdak_instance,
    }

    return render(request, 'stock/search_kosdak_name.html', context)

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Classes created for the forms challenge
class OwnerCreate(PermissionRequiredMixin, CreateView):
    model = Owner
    fields = '__all__'
    initial = {'date_of_death': '05/01/2018'}
    permission_required = "stock.can_mark_returned"

class OwnerUpdate(PermissionRequiredMixin, UpdateView):
    model = Owner
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    permission_required = 'stock.can_mark_returned'

class OwnerDelete(PermissionRequiredMixin, DeleteView):
    model = Owner
    success_url = reverse_lazy('owners')
    permission_required = 'stock.can_mark_returned'

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

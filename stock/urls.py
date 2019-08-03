from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kospis/', views.KospiListView.as_view(), name='kospis'),
    path('kospi/<int:pk>/', views.KospiDetailView.as_view(), name='kospi-detail'),
    path('kosdaks/', views.KosdakListView.as_view(), name='kosdaks'),
    path('kosdak/<int:pk>/', views.KosdakDetailView.as_view(), name='kosdak-detail'),
    path('owners/', views.OwnerListView.as_view(), name='owner'),
    path('owner/<int:pk>/', views.OwnerDetailView.as_view(), name='owner-detail')
]

# Set in Owner of company
urlpatterns += [
    path('mykospis/', views.OwnedKospisByUserListView.as_view(), name='my-kospi'),
    path(r'ownnedkospi/', views.OwnedKospisAllListView.as_view(), name='all-kospi'),
    path('mykosdaks/', views.OwnedKosdaksByUserListView.as_view(), name='my-kosdak'),
    path(r'ownnedkosdak/', views.OwnedKosdaksAllListView.as_view(), name='all-kosdak'),
]

# Add URLConf searching for a stock
urlpatterns += [
    path('Kospi/search/', views.search_kospi_name, name='search_kospi_name'),
    path('Kosdak/search/', views.search_kosdak_name, name='search_kosdak_name'),
]

# Add URLConf to create, update, and delete kospi
urlpatterns += [
    path('owner/create/', views.OwnerCreate.as_view(), name='owner_create'),
    path('owner/<int:pk>/update/', views.OwnerUpdate.as_view(), name='owner_update'),
    path('owner/<int:pk>/delete/', views.OwnerDelete.as_view(), name='owner_delete'),
]
# Add URLConf to create, update, and delete kospi
urlpatterns += [
    path('kospi/create/', views.KospiCreate.as_view(), name='kospi_create'),
    path('kospi/<int:pk>/update/', views.KospiUpdate.as_view(), name='kospi_update'),
    path('kospi/<int:pk>/delete/', views.KospiDelete.as_view(), name='kospi_delete'),
]


# Add URLConf to create, update, and delete kosdak
urlpatterns += [
    path('kosdak/create/', views.KosdakCreate.as_view(), name='kosdak_create'),
    path('kosdak/<int:pk>/update/', views.KosdakUpdate.as_view(), name='kosdak_update'),
    path('kosdak/<int:pk>/delete/', views.KosdakDelete.as_view(), name='kosdak_delete'),
]
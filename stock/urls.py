from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kospis', views.KospiListView.as_view(), name='kospis'),
    path('kospi/<int:pk>', views.KospiDetailView.as_view(), name='kospi-detail'),
    path('kosdaks', views.KosdakListView.as_view(), name='kosdaks'),
    path('kosdak/<int:pk>', views.KosdakDetailView.as_view(), name='kosdak-detail'),
]

# Set in Owner of company
urlpatterns += [
    path('mykospis/', views.OwnerKospisByUserListView.as_view(), name='my-kospi'),
    path(r'ownnedkospi/', views.OwnerKospisAllListView.as_view(), name='all-kospi'),
    path('mykosdaks/', views.OwnerKosdaksByUserListView.as_view(), name='my-kosdak'),
    path(r'ownnedkosdak/', views.OwnerKosdaksAllListView.as_view(), name='all-kosdak'),
]

# Add URLConf searching for a stock
urlpatterns += [
    path('Kospi', views.search_kospi_name),
    path('Kosdak', views.search_kosdak_name),
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
##############################################
#                                            
##############################################
import os
import django
from stock.packages.get_company_code import get_path, save_dict_data
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deactBackend.settings")
django.setup()
from stock.models import Kospi, Kosdak


##  KOSPI COMPANY COdE GETTER
"""
def KospiInsert(filename):
    g_path = get_path(filename)
    g_data = save_dict_data(g_path)

    for i in range(0, len(g_data)):
        print(g_data[i][0], g_data[i][1])
        Kospi.objects.create(name=g_data[i][0], code=g_data[i][1])


FILE_NAME = 'Kospiu.csv'
KospiInsert(FILE_NAME)
"""

##  KOSDAK COMPANY COdE GETTER
"""
def KospiInsert(filename):
    g_path = get_path(filename)
    g_data = save_dict_data(g_path)

    for i in range(0, len(g_data)):
        print(g_data[i][0], g_data[i][1])
        Kosdak.objects.create(name=g_data[i][0], code=g_data[i][1], sector=g_data[i][2]  , feature=g_data[i][3])


FILE_NAME = 'Kosdaku.csv'
KospiInsert(FILE_NAME)
"""

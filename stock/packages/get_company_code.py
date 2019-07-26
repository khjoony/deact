################################################
#                                              #
################################################

import os, sys
import pandas as pd
from pathlib import Path as path

## Reading CSV FILE OF COMPANY_CODE

MY_PATH = os.path.dirname(os.path.abspath(__file__))
print(MY_PATH)
MY_PATH = path(MY_PATH)


def get_path(codefile):
    kospi_path = os.path.join(MY_PATH.parent, 'sources', codefile)
    kospi_path = path(kospi_path)
    return(kospi_path)

COMPONY_CODES = []
def save_dict_data(filepath):
    DF = pd.read_csv(filepath, encoding='utf8')

    for i in range(len(DF.회사명)):
        ## print(DF.종목코드[i])
        COMPONY_CODES.append([])
        COMPONY_CODES[i].append(DF.회사명[i])
        COMPONY_CODES[i].append(DF.종목코드[i])
        COMPONY_CODES[i].append(DF.업종[i])
        COMPONY_CODES[i].append(DF.주요제품[i])

    return(COMPONY_CODES)
    

#filepath = 'Kospiu.csv'
#cpath = get_path(filepath)
#save_dict_data(cpath)
"""
test = [[1,2], [2,3],[3,4],]
print(test[0][0])

test[2][0] = 5
test[2][1] = 6
print(test[2][0])
"""
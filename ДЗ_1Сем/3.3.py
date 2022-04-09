#Слейте воедино три словаря
from typing import Dict

dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}
dict_e = {**dict_a, **dict_b, **dict_c}
print(dict_e)

import os

from pandas import concat

from day_pages import *


arr = os.listdir('./day_pages')

print(arr)
print(globals())
def short_key(value: str) -> int:
    return value.isdigit() and int(value) or 0 


def short_by_string_range() -> list[str]:
    new_list = []
    for i in arr:
        i = i.removesuffix('.py')
        if 'default' in i:
            new_list.append(i)
            continue
        day_num = i[3:]
        new_list.append(day_num)
    new_list.sort(key=short_key)
    return new_list
 

def make_day_page() -> dict:
    result = {}
    for i in short_by_string_range() : 
        if 'default' in i:
            func = getattr(globals()['default_page'], 'page')
            result['Default'] = func
        elif i.isdigit():
            func = getattr(globals()[str(f'day{i}')], 'page')
            result[f'Day {i}'] = func
    return result

        
    
        
        
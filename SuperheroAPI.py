import requests
from decorator_HW3 import path_indicate_logger


@path_indicate_logger('log.txt')
def intelligence_counter(*args):
    superhero_list = [*args]
    count = 0
    k = ()
    for name in superhero_list:
        response = requests.get(f'https://www.superheroapi.com/api.php//search/{name}')
        intelligence = int(response.json()['results'][0]['powerstats']['intelligence'])
        if intelligence > count:
            count = intelligence
            output = [name, count]
            most_intelligence = f"самый умный {output[0]}, уровень 'intelligence' - {output[1]}"
    return most_intelligence


print(intelligence_counter('Hulk', 'Captain America', 'Thanos'))

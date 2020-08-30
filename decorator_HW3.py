import datetime
import json


def path_indicate_logger(path):
    def logger_deco(foo):
        def any_function(*args, **kwargs):
            result = f'{datetime.datetime.today()}, {foo.__name__}, args - {str(args)}, ' \
                     f'kwargs - {str(kwargs)}, {json.dumps(foo(*args, **kwargs), ensure_ascii=False)}\n'
            with open(path, 'a', encoding='UTF-8') as f:
                f.write(result)
            return result
        return any_function
    return logger_deco

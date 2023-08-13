import json
from datetime import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        log = {
            'datetime': f'{datetime.now()}',
            'args': args,
            'kwargs': kwargs,
            'function_name': old_function.__name__
        }
        res = old_function(*args, **kwargs)
        log['function_result'] = res
        with open('main.log', "a") as f:
            json.dump(log, f, indent=4)
        return res
    return new_function

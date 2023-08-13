from logger_with_path import logger


@logger('main.log')
def get_employees():
    print('get_employees')
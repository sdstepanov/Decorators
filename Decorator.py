import logging
from functools import wraps


def path_log(path):
	logging.basicConfig(filename=path,
						format='[%(asctime)s] | %(message)s',
						datefmt='%Y-%m-%d %H:%M:%S',
						level=logging.INFO,
						encoding='utf-8')

	def log(old_function):
		@wraps(old_function)
		def new_function(*args, **kwargs):
			logging.info(
				f'Вызов функции: {old_function.__name__} | Аргументы: {args} {kwargs} | Возвращаемое значение:')
			result = old_function(*args, **kwargs)
			logging.info(f'Завершение функции: {old_function.__name__} | Возвращаемое значение: {result}')
			return result

		return new_function
	return log

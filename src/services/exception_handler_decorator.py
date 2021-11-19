from src.services.logger_service import main_logger


def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer


@parametrized
def exception_handler(func, return_value_if_exception):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            main_logger.exception(e)
            return return_value_if_exception
    return inner_function

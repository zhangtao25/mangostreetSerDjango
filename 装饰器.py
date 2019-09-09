def check_token(decorator_arg):
    def _check_token(func):
        def __check_token(request, *args, **kwargs):
            print(request, args, kwargs,decorator_arg)
            return func(request, *args, **kwargs)
        return __check_token
    return _check_token

@check_token(['a','b'])
def login(request):
    print(request)

login({'session':'zzzzzzzzzz'})
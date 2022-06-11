from django.shortcuts import redirect


def adminonly(function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_admin:
                return(function(request, *args, **kwargs))
            else:
                return redirect('404')
        else:
            return redirect('log_in')
    return wrapper

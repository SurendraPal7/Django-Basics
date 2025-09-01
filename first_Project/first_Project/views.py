from django.http import HttpResponseNotFound

def handler404(request, exception):
    return HttpResponseNotFound('Page not found',status=404)
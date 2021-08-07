from django.shortcuts import render


# Create your views here.
def hello_world(request):
    """
    https://realpython.com/get-started-with-django-1/#the-structure-of-a-django-website
    In this piece of code, you’ve defined a view function called hello_world(). When this function is called, it will render an HTML file called hello_world.html.
    :param request:
    :return:
    """
    return render(request, "hello_world.html")

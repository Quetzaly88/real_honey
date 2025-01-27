from django.shortcuts import render

# Create your views here.
def index(request):
    """
    A view to retunt to indexpage
    """
    return render(request, 'home/index.html')
    
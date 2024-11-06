from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    our_services = ['Software Development', 'Website Development', 'Penetration Testing']
    price = 10000
    date = '05-11-2024'
    return render(request, 'services.html', {"services": our_services, "price":price, 'date': date})


def contacts(request):
    return render(request, 'contacts.html')
from django.http import HttpResponse
from django.template import loader
from .models import Member


# def members(request):
#     return HttpResponse("Hello world!")


# def members(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())


def members(request):
    my_members = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'my_members': my_members,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    my_member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'my_member': my_member,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


# def testing(request):
#     template = loader.get_template('template.html')
#     context = {
#         'colors': ['Red', 'Orange', 'Blue'],
#     }
#     return HttpResponse(template.render(context, request))

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'firstname': 'Linus',
#   }
#   return HttpResponse(template.render(context, request))


# def testing(request):
#     mymembers = Member.objects.all().values()
#     template = loader.get_template('template.html')
#     context = {
#         'mymembers': mymembers,
#     }
#     return HttpResponse(template.render(context, request))

# def testing(request):
#     template = loader.get_template('template.html')
#     context = {
#         'x': ['Apple', 'Banana', 'Cherry'],
#         'y': ['Apple', 'Banana', 'Cherry'],
#     }
#     return HttpResponse(template.render(context, request))

# def testing(request):
#     template = loader.get_template('template.html')
#     context = {
#         'colors': ['Red', 'Orange', 'Blue'],
#     }
#     return HttpResponse(template.render(context, request))

# def testing(request):
#     mydata = Member.objects.all()
#     template = loader.get_template('template.html')
#     context = {
#         'mymembers': mydata,
#     }
#     return HttpResponse(template.render(context, request))


from django.db.models import Q


def testing(request):
    mydata = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

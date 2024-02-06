from django.shortcuts import render

def profile(request):
    """ Display the Users Profile """
    template= 'profiles.html/profile.html'
    context = {}

    return render(request, template, context)
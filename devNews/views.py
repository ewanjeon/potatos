from django.shortcuts import render


def devnews_list(request):
    return render(request, 'devNews/devnews_list.html',{})
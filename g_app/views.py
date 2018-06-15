from django.shortcuts import render
import requests


def home(request):
    user = {}    # username is stored here only.
    print(user)

    if 'username' in request.GET:
        username = request.GET['username']
        url = 'http://api.github.com/users/%s' % username
        response = requests.get(url)          # api call
        user = response.json()

    return render(request, 'g_app/github_info.html', {'user':user})
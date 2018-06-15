from django.shortcuts import render
import requests


def home(request):
    # user = {}    # username is stored here only.
    # print(user)
    #
    # if 'username' in request.GET:
    #     username = request.GET['username']
    #     url = 'http://api.github.com/users/%s' % username
    #     response = requests.get(url)          # api call
    #     user = response.json()
    #
    # return render(request, 'g_app/github_info.html', {'user':user})

    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        search_was_successful = (response.status_code == 200)  # 200 = SUCCESS
        search_result = response.json()
        search_result['success'] = search_was_successful
        search_result['rate'] = {
            'limit': response.headers['X-RateLimit-Limit'],
            'remaining': response.headers['X-RateLimit-Remaining'],
        }
    return render(request, 'g_app/github_info.html', {'search_result': search_result})
from django.http import HttpResponse
from django.shortcuts import render
# from django.shortcuts import render_to_response

def HelloView(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    resp = render(request, "hello/view_count.html", {'view_count': num_visits})
    # resp = HttpResponse('Cookie')
    resp.set_cookie('dj4e_cookie', 'b8c83e21', max_age=1000)
    # return resp
    # num_visits = request.session.get('num_visits', 0) + 1
    # request.session['num_visits'] = num_visits
    # if num_visits > 4 : del(request.session['num_visits'])
    return resp

    # resp = HttpResponse('Cookie')
    # resp.set_cookie('dj4e_cookie', 'b8c83e21', max_age=1000)
    # # return resp
    # num_visits = request.session.get('num_visits', 0) + 1
    # request.session['num_visits'] = num_visits
    # if num_visits > 4 : del(request.session['num_visits'])
    # return HttpResponse('view count='+str(num_visits))


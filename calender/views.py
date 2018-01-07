from django.http import HttpResponseRedirect, HttpResponse
from templates.pagemaker import *
from account.models import isLogged, User

def home(request):
    pg = PageMaker(request)
    pg.add_to_body(pg.get_card("Calender", color="blue"))
    if isLogged(request):
        right = ['r', User.objects.get(id=request.session['uid']).name, '../account']
        memobox = pg.get_card("",pg.get_form("./addToDo", "Add to-do Item", "Create", [
            ['i', 'text', 'title', 'Title', 'r'],
            ['i', 'date', 'date', 'Title', 'r'],
            ['i', 'time', 'time', 'Title', 'r'],
            ['a', '', 'desc', 'Description', 'r'],
        ]), color=' w3-card-4')
        lists=get_to_do_list(request)
    else:
        lists=''
        right = ['r', 'login/signup', '../login']
        memobox = pg.get_card('Once you are logged in, you can create a list of to-do works', color='green w3-card-4')
    pg.add_to_body(pg.get_nav([
        ['Home', '../'],
        ['To-do-list', './'],
        right
    ], selected='To-do-list', color='black'))
    pg.add_to_body(pg.get_row([
        ['1/4', "<br>"+memobox],
        ['3/4', "<br>"+lists]
    ]))
    return HttpResponse(pg.get_page("Calender"))


def get_to_do_list(request):
    from .models import getAllList
    list = getAllList(request)
    items = ''
    for item in list:
        items += load('info_card.html', request, {
            'title':item.title,
            'date': item.date,
            'time': item.time,
            'body': item.desc,
            'createdon': item.createdTime,
            'id':item.id
        })
    return items + load('scriptcss.html', request, None)
#x
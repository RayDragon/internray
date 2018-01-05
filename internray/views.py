from django.http import HttpResponse, HttpResponseRedirect
from templates.pagemaker import *


def home(request):
    pg = PageMaker(request)
    pg.add_to_body(pg.get_card("InternRay", color='dark-grey'))
    from account.models import isLogged, User
    log = ['r', 'Login/Signup', './login']
    if isLogged(request):
        user = User.objects.get(id=request.session['uid'])
        log = ['r', user.name, './account/']
    pg.add_to_body(pg.get_nav([
        nav_self_item("About"),
        ['d', 'Me', [
            ['Calender', '../calender']
        ]
         ],
        log
    ], selected='About', color='black'))
    pg.add_to_body(pg.get_card("Instruction", "Click on login/signup to login....", color='green'))
    return HttpResponse(pg.get_page("Intern work"))


def login_signup(request):
    from account.models import isLogged, User
    log = ['r', 'Login/Signup', './login']
    if isLogged(request):
        return HttpResponseRedirect('./account')
    pg = PageMaker(request)
    pg.add_to_body(pg.get_card("InternRay",'Login', color='dark-grey'))
    pg.add_to_body(pg.get_nav([
        ['About', '/?nav=About'],
        log
    ], selected='Login/Signup', color='black'))
    login_form = pg.get_form("./account/login", "Login", "Sign In", [
        ['i', 'email', 'email', 'Enter a valid email', 're'],
        ['i', 'password', 'password', 'Enter any password', 'r']
    ])

    signup_form = pg.get_form("./account/signup", "Signup", "Create account", [
        ['i', 'text', 'name', 'Enter your complete name', 'r'],
        ['i', 'email', 'email', 'Enter a valid email', 're'],
        ['i', 'password', 'password', 'Enter any password', 'r' ]
    ])

    info = 4*'<br>'+pg.get_card("Hey there", 'Looks like you haven\'t signed in, please create an account or login if already created')
    pg.add_to_body(pg.get_row([
        ['1/3', info],
        ['1/3', signup_form],
        ['1/3', login_form]
    ]))

    return HttpResponse(pg.get_page("Login"))
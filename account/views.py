from templates.pagemaker import *
from .models import *


def home(request):
    if not isLogged(request):
        return HttpResponseRedirect('../login')
    pg = PageMaker(request)
    pg.add_to_body(pg.get_card("InternRay", "Account", color="dark-grey"))
    pg.add_to_body(pg.get_nav(
        [
            nav_self_item("User"),
            ['d', 'Me', [
                    ['Calender', '../calender']
                ]
             ],
            ['r', 'Logout', './logout']
        ], color="black", selected='User'))

    if pg.nav == "User":
        pg.add_to_body(user_page(request))

    return HttpResponse(pg.get_page("#Book Account"))


def user_page(request):
    pg = PageMaker(request)

    user = User.objects.get(id=request.session['uid'])
    user_details = pg.get_form("./update", '', "Update", [
            ['i', 'text', 'name', 'Change name', '', user.name],
            ['i', 'email', 'email', 'Change email', 'e', user.email],
            ['i', 'password', 'passwordNew', 'New Password', ''],
            ['i', 'password', 'passwordOld', 'Old password', 'r', ''],
        ])
    info = pg.get_card("Information", '''
        To update any values, you need to provide the old password, blank fields will not be altered<br>
        To go to to-do list, go to navigation-bar > Me > calender 
    ''', color="blue")
    pg.add_to_body("<br>"+
           pg.get_row([
               ['3/4', info],
                ['1/4', pg.get_card(user.name, "Edit Details" + user_details, color="yellow w3-card-4")],

            ], add="-padding")
        )

    return pg.get_page()



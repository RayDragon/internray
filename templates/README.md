# DjangoTemplate
It uses jquery and w3.css for loading a fast, responsive and light webpage, a sample webpage is shown as below
  main thing is to use a PageMaker class, if you want to create responsive do assign PageMaker.request value 
```python
from django.http import HttpResponse
from .templates.pagemaker import PageMaker, LOREAM


def home(request):
    pgmaker = PageMaker()
    pgmaker.request = request
    pgmaker.add_to_body(pgmaker.get_card("Schools", '', "blue"))
    pgmaker.add_to_body(pgmaker.get_nav([["Home", "."]], 'Home'))
    pgmaker.add_to_body(
        pgmaker.get_row([
            ["1/3", pgmaker.get_form("schools/addschool", "Create School", "Create School",
                                     [
                                         ['i', 'school_name', 'school_name', 'School name', 'r'],
                                         ['i', 'email', 'school_email', 'School email address', 're'],
                                         ['i', 'password', 'login_pwd', 'Login Password', 'r']

                                     ])

             ],
                        ["1/3", pgmaker.get_card("About",
                             '''
                             Get your schools and college online with almost all the new facilities<br>
                             Here is how to get them....<br>
                             <ol>
                             <li>Create account for college/school
                             <li>Create a teacher's account
                             <li>Login as a teacher
                             <li>Add class
                             <li>Add students
                             <li>Download our app to use it with ease
                             </ol>
                             ''')],
                         ["1/3", pgmaker.get_form("./schools/login", "Login to account", "Login",
                            [
                                ['i', 'email', 'login_email', 'Email Address', 're'],
                                ['i', 'password', 'login_password', 'Password', 'r']
                            ])
                         ]

                         ],
                        add=" w3-dark-grey")

    )
    pgmaker.add_to_body(pgmaker.get_form("#","Time Pass Form", "Do Time Pass",
                                         [
                                             ['i', 'text', 'Name', 'Your Name', 'r']
                                         ]))
    return HttpResponse(pgmaker.get_page())
```
# Get HTML for navbar
```python
    pgmaker.get_nav(elements, selected_element, color="blue")
    # here elements is like 
    [
      ["Name1", "Link1"],
      ["Name2", "Link2"],
      ["d","Dropdown",[
          ["dropdown1","link"],
          ["dropdown2","link"]
        ],
      ["r", "(Right aligned)Name","link"]
     ]
      
```
# Add HTML to page
```python
pgmaker.add_to_body(HTML)
```
# Get complete page's HTML
```python
pgmaker.get_page()
```
